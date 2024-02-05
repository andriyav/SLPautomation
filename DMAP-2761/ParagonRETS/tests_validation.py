import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pyautogui
from selenium.webdriver.support.ui import Select
from value_provider import ValueProvider

GOOGLE_USER = '//*[@id="identifierId"]'
LOGIN_BTN = '//*[@id="nav-home"]/div/table/tbody/tr[2]/td/div/input'
NEXT_BTN = '//*[@id="identifierNext"]/div/button'
NEXT_BTN_2 = '//*[@id="passwordNext"]/div/button'
PASSWORD_INPUT = '//*[@id="password"]/div[1]/div/div[1]/input'
SOURCE_ID = '//*[@id="sources"]'
APP_SOURCE_BTN = '//*[@id="applySource"]'
IMPLIS_LINK = '//a[text()="Multiple Listings Services"]'
METADATA_SELECT = '//*[@id="metadataSelect"]'
RULE_FIELD = '//*[@id="rulesAutocomplete"]'
RULE_SELECTOR = '//*[@id="foo"]'
RULE_CREATE_BTN = '//*[@id="addForm"]/div/input'
IMPLIS_WAIT_MAP = '#listing_mapper_mls_key__0'


def get_classes_numbers(source):
    options = webdriver.ChromeOptions()
    CHROME_USER_DIR = "C:/Users/aandrusy/AppData/Local/Google/Chrome/UserData/aandrusy"
    options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
    options.add_argument("profile-directory=Default")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    time.sleep(1)
    driver.get("https://stage-slp.data.kw.com/mapper_tool#no-filter")
    login_btn = driver.find_element(By.XPATH, LOGIN_BTN)
    login_btn.click()
    driver.maximize_window()
    time.sleep(5)
    driver.implicitly_wait(30)
    select_element = driver.find_element(By.XPATH, SOURCE_ID)
    select = Select(select_element)
    select.select_by_value(source)  # source id
    driver.implicitly_wait(30)
    apply_source_button = driver.find_element(By.XPATH, APP_SOURCE_BTN)
    apply_source_button.click()
    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, IMPLIS_LINK)
    driver.execute_script("document.body.style.zoom='50 %'")
    time.sleep(5)
    classes = ValueProvider.get_classes()
    driver.implicitly_wait(10)
    select_element_type = driver.find_element(By.XPATH, METADATA_SELECT)
    select_el = Select(select_element_type)
    select_el.select_by_index(1)
    time.sleep(10)
    return len(select_el.options)


def slp_automation_mapp(source, clas):
    options = webdriver.ChromeOptions()
    CHROME_USER_DIR = "C:/Users/aandrusy/AppData/Local/Google/Chrome/UserData/aandrusy"
    options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
    options.add_argument("profile-directory=Default")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    time.sleep(1)
    driver.get("https://stage-slp.data.kw.com/mapper_tool#no-filter")
    login_btn = driver.find_element(By.XPATH, LOGIN_BTN)
    login_btn.click()
    time.sleep(4)
    driver.maximize_window()
    driver.implicitly_wait(30)
    select_element = driver.find_element(By.XPATH, SOURCE_ID)
    select = Select(select_element)
    select.select_by_value(source)  # source id
    driver.implicitly_wait(30)
    apply_source_button = driver.find_element(By.XPATH, APP_SOURCE_BTN)
    apply_source_button.click()

    driver.implicitly_wait(60)
    driver.find_element(By.XPATH, IMPLIS_LINK)
    driver.implicitly_wait(10)
    select_element_type = driver.find_element(By.XPATH, METADATA_SELECT)
    select_el = Select(select_element_type)
    select_el.select_by_index(clas)  # class id from 1
    driver.implicitly_wait(30)
    driver.find_element(By.CSS_SELECTOR, IMPLIS_WAIT_MAP)
    class_text = driver.find_element(By.CSS_SELECTOR, "#metadataSelect").text
    time.sleep(2)
    lease = driver.find_element(By.CSS_SELECTOR,
                                '#nav-home > div > table > tbody > tr.master_schema.kw_listing.lease_price')
    class_text_spl = class_text.split('\n')
    return [lease.text, class_text_spl]


class AuthenticationTestCase(TestCase):

    def test_slp_automation_mapp(self):
        sources = ValueProvider.get_list_of_sources()
        successfully_mapped = []
        wrong_mapped = []
        deleted_classes = []
        for source in sources:
            classes = get_classes_numbers(source)
            for clas in range(1, classes):
                with self.subTest(source=source):
                    try:
                        actual = slp_automation_mapp(source, clas)
                        self.assertEqual(actual[0],
                                         'lease_price\n+\n[add]\nCreateObjectMapper(json_path={"list_price":"L_AskingPrice","prop_type":"L_Class","sale_rent":"L_SaleRent"},skip_values=[])\n[add]\n[add]\nLeasePriceMatrix()\n[add]')
                        successfully_mapped.append(source + f" class {clas}-{actual[1][clas]}")
                    except AssertionError as e:
                        wrong_mapped.append(source + f" class {clas}-{actual[1][clas]}")
                        print(f"AssertionError in test for source {source} class {clas}-{actual[1][clas]}: {str(e)}")
                        # Log the failure or take specific actions for the failed test
                    except Exception as e:
                        deleted_classes.append(source + f" class {clas}-{actual[1][clas]}")
                        print(f"Error in test for source {source} class {clas}-{actual[1][clas]}: {str(e)}")

        print(f"The following sources were mapped successfully {successfully_mapped}")
        print(f"There are issues with mapping in sources {wrong_mapped}")
        print(f"deleted classes {deleted_classes}")
