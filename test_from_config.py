import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pyautogui
from selenium.webdriver.support.ui import Select
from value_provider import ValueProvider
from selenium.webdriver.support import expected_conditions as EC

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


def mapper(driver, field, mappers_provider, metadata):
    timeout = 10
    wait = WebDriverWait(driver, timeout)
    driver.implicitly_wait(30)

    map = driver.find_element(By.CSS_SELECTOR,
                              f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{field} > td:nth-child(2) > div > span")
    element_loc = (By.CSS_SELECTOR,
                   f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{field} > td:nth-child(2) > div > span")
    wait.until(EC.element_to_be_clickable(element_loc))
    map.click()
    driver.implicitly_wait(30)
    select_element_mapper = driver.find_element(By.CSS_SELECTOR, "#foo")
    select_vp = Select(select_element_mapper)
    select_vp.select_by_index(mappers_provider)  # mapper id from 0
    time.sleep(1)
    json_mapper_path = driver.find_element(By.XPATH,
                                           "/ html / body / div[3] / div / div / div[2] / div[2] / form / div / div[2] / div / input")

    time.sleep(1)
    json_mapper_path.send_keys(metadata)
    time.sleep(1)
    try:
        driver.find_element(By.XPATH, "/html/body/ul[2]/li/div")
    except Exception as e:
        return ["metadata issue!", "metadata issue!"]
    mapper_create_btn = driver.find_element(By.CSS_SELECTOR, MAPPER_CREATE_BTN)
    time.sleep(3)
    mapper_create_btn.click()
    time.sleep(3)
    print('mapper')


def rule(driver, field, rules):
    driver.find_element(By.CSS_SELECTOR,
                        f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{field} > td:nth-child(4) > div > span").click()
    time.sleep(1)
    select_element_rule = driver.find_element(By.XPATH, RULE_SELECTOR)
    select_rule = Select(select_element_rule)
    select_rule.select_by_index(rules)  # rule id from 0
    driver.implicitly_wait(30)
    time.sleep(1)
    button_create = driver.find_element(By.XPATH, RULE_CREATE_BTN)
    button_create.click()
    time.sleep(1)
    print('Rules')

def transforms(driver, field, transform):
    driver.find_element(By.CSS_SELECTOR,
                        f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{field} > td:nth-child(3) > div > span").click()
    time.sleep(1)
    select_element_trans = driver.find_element(By.XPATH, RULE_SELECTOR)
    select_trans = Select(select_element_trans)
    select_trans.select_by_index(transform)  # rule id from 0
    driver.implicitly_wait(30)
    time.sleep(1)
    button_create = driver.find_element(By.XPATH, RULE_CREATE_BTN)
    button_create.click()
    time.sleep(1)
    print('trans')

def enhancers(driver, field, enhancer, const):
    sel = driver.find_element(By.CSS_SELECTOR,
                              f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{field} > td:nth-child(5) > div > span")
    time.sleep(2)
    sel.click()
    time.sleep(2)
    select_element_mapper = driver.find_element(By.CSS_SELECTOR, "#foo")
    select_vp = Select(select_element_mapper)
    select_vp.select_by_index(enhancer)  # mapper id from 0
    time.sleep(2)
    json_mapper_path = driver.find_element(By.XPATH,
                                           "/html/body/div[3]/div/div/div[2]/div[2]/form/div/div[2]/div/input")
    time.sleep(2)
    json_mapper_path.send_keys(const)
    time.sleep(2)
    mapper_create_btn = driver.find_element(By.CSS_SELECTOR, "#addForm > div > input")
    time.sleep(2)
    mapper_create_btn.click()
    pyautogui.moveTo(1100, 230)
    pyautogui.click()
    print('enhancers')

def slp_automation_mapp(username, password, source, clas):
    global mapper
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://stage-slp.data.kw.com/login")

    pyautogui.keyDown('ctrl')
    j: int = 1
    for j in range(4):
        pyautogui.press('-')
        time.sleep(1)
    pyautogui.keyUp('ctrl')


    login_btn = driver.find_element(By.XPATH, LOGIN_BTN)
    login_btn.click()
    driver.implicitly_wait(30)
    google_login_username = driver.find_element(By.XPATH, GOOGLE_USER)
    google_login_username.send_keys(username)
    time.sleep(3)
    next_button = driver.find_element(By.XPATH, NEXT_BTN)
    next_button.click()
    driver.implicitly_wait(30)
    google_login_password = driver.find_element(By.XPATH, PASSWORD_INPUT)
    google_login_password.send_keys(password)
    next_login = driver.find_element(By.XPATH, NEXT_BTN_2)
    next_login.click()
    time.sleep(10)
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
    driver.execute_script("document.body.style.zoom='50 %'")
    time.sleep(5)
    classes = ValueProvider.get_classes()
    driver.implicitly_wait(10)
    select_element_type = driver.find_element(By.XPATH, METADATA_SELECT)
    select_el = Select(select_element_type)
    select_el.select_by_index(clas)  # class id from 1
    driver.implicitly_wait(30)
    driver.find_element(By.CSS_SELECTOR, IMPLIS_WAIT_MAP)
    time.sleep(10)
    configs = ValueProvider.get_mapping_configuration()
    print(source)
    for config in configs:
        driver.implicitly_wait(30)
        field = config.get("field")
        mappers_provider = config.get("MappersProvider")
        metadata = config.get("Metadata")
        rules = config.get("Rules")
        rules2 = config.get("Rules2")
        rules3 = config.get("Rules3")
        enhancer = config.get("Enhancers")
        const = config.get("Const")
        transform = config.get("Transforms")
        map0 = driver.find_element(By.CSS_SELECTOR,
                                   f"#nav-home > div > table > tbody > tr.master_schema.kw_listing.{field}")
        scroll_script = "arguments[0].scrollIntoView({behavior: 'auto', block: 'center', inline: 'center'});"
        driver.execute_script(scroll_script, map0)
        if config.get("MappersProvider") is not None:
            mapper(driver, field, mappers_provider, metadata)
        if config.get("Rules") is not None:
            rule(driver, field, rules)
            if config.get("Rules2") is not None:
                rule(driver, field, rules2)
                if config.get("Rules3") is not None:
                    rule(driver, field, rules3)
        if config.get("Transforms") is not None:
            transforms(driver, field, transform)
        if config.get("Enhancers") is not None:
            enhancers(driver, field, enhancer, const)
        time.sleep(15)
        datetime_before_save = driver.find_element(By.XPATH, DATE_TIME_BEFORE_SAVE)
        datetime_before_save_result = datetime_before_save.text
        button_save_map = driver.find_element(By.CSS_SELECTOR, "#btn_save_map")
        button_save_map.click()
        time.sleep(2)
        pyautogui.FAILSAFE = False
        pyautogui.moveTo(1100, 230)
        pyautogui.click()
        time.sleep(30)
        datetime_after_save = driver.find_element(By.XPATH, DATE_TIME_AFTER_SAVE)
        datetime_after_save_result = datetime_after_save.text
        result = [datetime_before_save_result, datetime_after_save_result]
        return result

class AuthenticationTestCase(TestCase):

    def test_slp_automation_mapp(self):
        sources = ValueProvider.get_list_of_sources()
        classes = ValueProvider.get_classes()
        username = ValueProvider.get_email()
        password = ValueProvider.get_password()
        successfully_mapped = []
        wrong_mapped = []
        for source in sources:
            for clas in classes:
                with self.subTest(source=source):
                    try:
                        actual = slp_automation_mapp(username, password, source, clas)
                        self.assertNotEqual(actual[1], actual[0])
                        successfully_mapped.append(source + f" class {clas}")
                    except AssertionError as e:
                        wrong_mapped.append(source)
                        print(f"AssertionError in test for source {source} class {clas}: {str(e)}")
                        # Log the failure or take specific actions for the failed test
                    except Exception as e:
                        wrong_mapped.append(source)
                        print(f"Error in test for source {source} class {clas}: {str(e)}")
                    # Log the error or take specific actions for unexpected errors
        print(f"The following sources were mapped successfully {successfully_mapped}")
        print(f"There are issues with mapping in sources {wrong_mapped}")
