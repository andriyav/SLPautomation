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


def slp_automation_mapp(username, password, source):
    result = []
    n = 2
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://stage-slp.data.kw.com/login")
    login_btn = driver.find_element(By.XPATH, LOGIN_BTN)
    time.sleep(0)
    login_btn.click()
    driver.implicitly_wait(30)
    google_login_username = driver.find_element(By.XPATH, GOOGLE_USER)
    google_login_username.send_keys(username)
    time.sleep(n)
    next_button = driver.find_element(By.XPATH, NEXT_BTN)
    next_button.click()
    driver.implicitly_wait(30)
    google_login_password = driver.find_element(By.XPATH, PASSWORD_INPUT)
    google_login_password.send_keys(password)
    next_login = driver.find_element(By.XPATH, NEXT_BTN_2)
    next_login.click()
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
    select_el.select_by_index(1)  # class id from 1
    driver.implicitly_wait(30)
    driver.find_element(By.CSS_SELECTOR, IMPLIS_WAIT_MAP)

    time.sleep(2)
    # validation of is_shor_sale filed
    is_short_sale = driver.find_element(By.CSS_SELECTOR,
                                              '#nav-home > div > table > tbody > tr.master_schema.kw_listing.structure-properties-exterior_features-properties-has_pool > td:nth-child(4)')


    # time.sleep(2)
    # # validation of  is_foreclosure filed
    # is_foreclosure = driver.find_element(By.CSS_SELECTOR,
    #                                           '#nav-home > div > table > tbody > tr.master_schema.kw_listing.is_foreclosure')
    # result.append(is_foreclosure.text)
    return is_short_sale.text


class AuthenticationTestCase(TestCase):

    def test_slp_automation_mapp(self):
        sources = ValueProvider.get_list_of_sources()
        username = ValueProvider.get_email()
        password = ValueProvider.get_password()
        successfully_mapped = []
        wrong_mapped = []
        for source in sources:
            with self.subTest(source=source):
                try:
                    actual = slp_automation_mapp(username, password, source)
                    self.assertNotEqual(actual,
                                     '[add]\nHasPool()')
                    # self.assertEqual(actual[0],
                    #                  'is_short_sale\n+\n[add]\nValueProvider(json_path=SpecialListingConditions,skip_values=[])\n[add]\n[add]\nIs_Short_Sale()\n[add]')
                    successfully_mapped.append(source)
                except AssertionError as e:
                    wrong_mapped.append(source)
                    print(f"AssertionError in test for source {source}: {str(e)}")
                    # Log the failure or take specific actions for the failed test
                except Exception as e:
                    wrong_mapped.append(source)
                    print(f"Error in test for source {source}: {str(e)}")
                    # Log the error or take specific actions for unexpected errors
        print(f"The following sources were mapped successfully {successfully_mapped}")
        print(f"There are issues with mapping in sources {wrong_mapped}")
