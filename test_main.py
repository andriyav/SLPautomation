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
IS_SHORT_SALE_RULE = "#nav-home > div > table > tbody > tr.master_schema.kw_listing.is_short_sale > td:nth-child(4) > div > span"
IS_FORECLOSURE_RULE = "#nav-home > div > table > tbody > tr.master_schema.kw_listing.is_foreclosure > td:nth-child(4) > div > span"
IS_SHORT_SALE_MAPPER = "#nav-home > div > table > tbody > tr.master_schema.kw_listing.is_short_sale > td:nth-child(2) > div > span"
IS_FORECLOSURE_MAPPER = "#nav-home > div > table > tbody > tr.master_schema.kw_listing.is_foreclosure > td:nth-child(2) > div > span"
MAPPER = "#foo"
MAPPER_JSON_PATH = "#jsonform-3-elt-json_path"
MAPPER_JSON_PATH2 = "#jsonform-5-elt-json_path"
MAPPER_CREATE_BTN = "#addForm > div > input"
FALSE_COST_IS_SHORT_SALE = "#listing_enhance_is_short_sale__0"
FALSE_COST_IS_FORECLOSURE = "#listing_enhance_is_foreclosure__0"
DEL_BTN_COST_1 = "#jsonform-11-elt-counter-12"
DEL_BTN_COST_2 = "#jsonform-13-elt-counter-14"
DATE_TIME_BEFORE_SAVE = '//*[@id="last_edited"]/i'
SAVE_MAP_BTN = '//*[@id="btn_save_map"]'
DATE_TIME_AFTER_SAVE = '//*[@id="last_edited"]/i'
IMPLIS_WAIT_MAP = '#listing_mapper_mls_key__0'
LIST_CATEGORY = '#nav-home > div > table > tbody > tr.master_schema.kw_open_house.required.mls_id'


# nav-home > div > table > tbody > tr.master_schema.kw_listing.required.list_category > td:nth-child(2)
# nav-home > div > table > tbody > tr.master_schema.kw_listing.required.list_category > td:nth-child(2) > div > span
# listing_mapper_list_category__0
# listing_rule_list_category__0
# listing_rule_list_category__1
# nav-home > div > table > tbody > tr.master_schema.kw_listing.required.list_category > td:nth-child(2) > div > span
# nav-home > div > table > tbody > tr.master_schema.kw_listing.required.list_category_id > td:nth-child(4) > div > span
# listing_rule_list_category_id__0


def get_mapper_selector():
    # nav-home > div > table > tbody > tr.master_schema.kw_listing.required.list_category > td:nth-child(2)
    general_selector = ValueProvider.get_mapping_configuration()
    mapper = general_selector["field"]
    mapper_selector = f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.required.{mapper} > td:nth-child(2) > div > span"
    result = mapper_selector
    return result

def get_rule_selector():
    # nav-home > div > table > tbody > tr.master_schema.kw_listing.required.list_category > td:nth-child(2)
    general_selector = ValueProvider.get_mapping_configuration()
    mapper = general_selector["field"]
    mapper_selector = f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{mapper} > td:nth-child(4) > div > span"
    result = mapper_selector
    return result




def slp_automation_mapp(username, password, source):
    global mapper
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

    configs = ValueProvider.get_mapping_configuration()
    time.sleep(2)
    n = 3
    for config in configs:

        if config.get("MappersProvider") is not None:
            mapper = config.get("field")
            driver.find_element(By.CSS_SELECTOR, f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.required.{mapper} > td:nth-child(2) > div > span").click()
            print(config["MappersProvider"])
            time.sleep(4)
            select_element_mapper = driver.find_element(By.CSS_SELECTOR, "#foo")
            select_vp = Select(select_element_mapper)
            select_vp.select_by_index(config.get("MappersProvider"))  # mapper id from 0
            time.sleep(2)
            json_mapper_path = driver.find_element(By.CSS_SELECTOR, f"#jsonform-{n}-elt-json_path")
            n += 2
            time.sleep(2)
            json_mapper_path.send_keys(config.get("Metadata"))
            time.sleep(2)
            try:
                driver.find_element(By.XPATH, "/html/body/ul[2]/li/div")
            except Exception as e:
                return ["metadata issue!", "metadata issue!"]
            mapper_create_btn = driver.find_element(By.CSS_SELECTOR, MAPPER_CREATE_BTN)
            time.sleep(3)
            mapper_create_btn.click()
            time.sleep(3)

        if config.get("Rules") is not None:
            driver.find_element(By.CSS_SELECTOR, f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.required.{mapper} > td:nth-child(4) > div > span").click()
            time.sleep(2)
            select_element_rule = driver.find_element(By.XPATH, RULE_SELECTOR)
            select_rule = Select(select_element_rule)
            select_rule.select_by_index(config.get("Rules"))  # rule id from 0
            driver.implicitly_wait(30)
            time.sleep(3)
            button_create = driver.find_element(By.XPATH, RULE_CREATE_BTN)
            n += 3
            button_create.click()
            time.sleep(5)






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
                    self.assertEqual(actual, 'fff')
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
