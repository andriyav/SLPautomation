import re
import time
from datetime import datetime
from selenium.webdriver.support import expected_conditions as EC
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
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
DASHBOARD_SLECTOR = "#navbarNav > ul.navbar-nav.me-auto.mb-2.mb-lg-0 > li:nth-child(2) > a"
KW_SOURCE_ID = 'body > div.col-5.center > form > div:nth-child(1) > div:nth-child(1) > input'
PHOTO_CHECK = 'body > div.col-5.center > form > div:nth-child(2) > div:nth-child(3) > input[type=checkbox]'
OH_CHECK = 'body > div.col-5.center > form > div:nth-child(2) > div:nth-child(4) > input[type=checkbox]'
SUBMIT_DB = '#submit'
VIEW_BT ='/html/body/div[4]/div[3]/div[2]/table/tbody[1]/tr[2]/td[11]/p[4]'
RAW = '/html/body/div[4]/div[3]/div[2]/table/tbody[1]/tr[2]/td[11]/div/div/div/nav/div/a[1]'
FRAME = '/html/body/div[4]/div[3]/div[2]/table/tbody[1]/tr[2]/td[11]/div/div/div'
KW_UPDATE_AT = ':contains("kw_updated_at")'
ALL_LISTING = '/html/body/div[4]/div[3]/div[2]/table/tbody/tr[1]'



def slp_automation_mapp(source, clas):
    options = webdriver.ChromeOptions()
    CHROME_USER_DIR = "C:/Users/aandrusy/AppData/Local/Google/Chrome/UserData/aandrusy"
    options.add_argument(f"user-data-dir={CHROME_USER_DIR}")
    options.add_argument("profile-directory=Default")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(60)
    time.sleep(1)
    driver.get("https://prod-slp.data.kw.com/last_listing")
    login_btn = driver.find_element(By.XPATH, LOGIN_BTN)
    login_btn.click()
    time.sleep(4)
    driver.maximize_window()
    select_element = driver.find_element(By.XPATH, SOURCE_ID)
    select = Select(select_element)
    select.select_by_value(source)  # source id
    apply_source_button = driver.find_element(By.XPATH, APP_SOURCE_BTN)
    apply_source_button.click()
    driver.find_element(By.XPATH, IMPLIS_LINK)
    time.sleep(5)
    click_DB = driver.find_element(By.CSS_SELECTOR, "#navbarNav > ul.navbar-nav.me-auto.mb-2.mb-lg-0 > li:nth-child(2) > a")
    click_DB.click()
    button_DB = driver.find_element(By.CSS_SELECTOR,
                                   "#navbarNav > ul.navbar-nav.me-auto.mb-2.mb-lg-0 > li.nav-item.dropdown.show > div > a")
    button_DB.click()
    kw_source_id = driver.find_element(By.CSS_SELECTOR, KW_SOURCE_ID)
    kw_source_id.send_keys(source)
    photo_check = driver.find_element(By.CSS_SELECTOR, PHOTO_CHECK)
    photo_check.click()
    oh_check = driver.find_element(By.CSS_SELECTOR, OH_CHECK)
    oh_check.click()
    submit = driver.find_element(By.CSS_SELECTOR, SUBMIT_DB)
    submit.click()
    header_element = driver.find_element(By.XPATH, '//th[text()="Modified Date"]')
    time.sleep(5)
    # Click on the header to activate sorting
    header_element.click()
    header_element.click()
    time.sleep(5)
    view_data = driver.find_element(By.XPATH, VIEW_BT)
    view_data.click()
    raw = driver.find_element(By.XPATH, RAW)
    raw.click()
    all_listing = driver.find_element(By.XPATH, ALL_LISTING)
    text_all_listing = all_listing.text
    text_splited = text_all_listing.split(" ")
    # kw_id = text_splited[19]
    perent_kw_updated_at = driver.find_element(By.CLASS_NAME, "jsonview").find_element(By.XPATH, "//a[contains(text(), 'kw_updated_at')]")
    li_locator = perent_kw_updated_at.find_element(By.XPATH, 'ancestor::li')
    span_element_kw_updated_at = li_locator.find_element(By.XPATH, './/span[@class="string"]')
    kw_updated_at_result = driver.execute_script('return arguments[0].textContent;', span_element_kw_updated_at)

    perent_kw_updated_by = driver.find_element(By.CLASS_NAME, "jsonview").find_element(By.XPATH, "//a[contains(text(), 'kw_updated_by')]")
    li_locator_kw_updated_by = perent_kw_updated_by.find_element(By.XPATH, 'ancestor::li')
    span_element_kw_updated_by = li_locator_kw_updated_by.find_element(By.XPATH, './/span[@class="string"]')
    kw_updated_by_result = driver.execute_script('return arguments[0].textContent;', span_element_kw_updated_by)
    time.sleep(1)

    perent_list_address = driver.find_element(By.CLASS_NAME, "jsonview").find_element(By.XPATH,
                                                                                       "//a[contains(text(), 'list_address')]")
    li_locator_list_address = perent_list_address.find_element(By.XPATH, 'ancestor::li')
    span_element_list_address = li_locator_list_address.find_element(By.XPATH, './/span[@class="string"]')
    list_address_result = driver.execute_script('return arguments[0].textContent;', span_element_list_address)
    time.sleep(2)


    a_coordinates_gp = driver.find_element(By.CLASS_NAME, "jsonview").find_element(By.XPATH, '//a[@class="prop" and contains(text(), "coordinates_gp")]')
    span_num_element_gp = a_coordinates_gp.find_element(By.XPATH, "following-sibling::*[2]")
    coordinates_gp_result = driver.execute_script('return arguments[0].textContent;', span_num_element_gp)


    a_coordinates_gs = driver.find_element(By.CLASS_NAME, "jsonview").find_element(By.XPATH,
                                                                                   '//a[@class="prop" and contains(text(), "coordinates_gs")]')
    span_num_element_gs = a_coordinates_gs.find_element(By.XPATH, "following-sibling::*[2]")
    coordinates_gs_result = driver.execute_script('return arguments[0].textContent;', span_num_element_gs)
    print(coordinates_gs_result)

    # a1709214111658176a > div > ul > li:nth-child(66) > a




    return [kw_updated_at_result[1:11], kw_updated_by_result[1:-1], list_address_result, coordinates_gp_result]


class AuthenticationTestCase(TestCase):

    def test_slp_automation_mapp(self):

        sources = ValueProvider.get_list_of_sources()
        successfully_mapped = []
        wrong_mapped = []
        deleted_classes = []
        for source in sources:
            # classes = get_classes_numbers(source)
            for clas in range(1, 2):

                with self.subTest(source=source):
                    try:
                        current_date = datetime.now()
                        expected_date = current_date.strftime("%Y-%m-%d")
                        actual = slp_automation_mapp(source, clas)
                        self.assertEqual(actual[0],
                                         expected_date)
                        self.assertEqual(actual[1],
                                         "slp_v5")
                        self.assertIsNotNone(actual[2])
                        pattern = r'"lat":\s*([-+]?\d*\.\d+|\d+)\s*,"lon":\s*([-+]?\d*\.\d+|\d+)'
                        match = re.match(pattern, actual[3])
                        self.assertTrue(bool(match))
                        successfully_mapped.append(source + f" class {clas}-{actual}")
                    except AssertionError as e:
                        wrong_mapped.append(source + f" class {clas}-{actual}")
                        print(f"AssertionError in test for source {source} class {clas}-{actual}: {str(e)}")
                        # Log the failure or take specific actions for the failed test
                    except Exception as e:
                        deleted_classes.append(source + f" class {clas}-{actual}")
                        print(f"Error in test for source {source} class {clas}-{actual}: {str(e)}")

        print(f"The following sources were mapped successfully {successfully_mapped}")
        print(f"There are issues with mapping in sources {wrong_mapped}")
        print(f"deleted classes {deleted_classes}")
