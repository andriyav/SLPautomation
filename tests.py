import time
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pyautogui
from selenium.webdriver.support.ui import Select
def login_selenium(username, password):
    n = 2
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get("https://stage-slp.data.kw.com/login")
    login_btn = driver.find_element(By.XPATH, '//*[@id="nav-home"]/div/table/tbody/tr[2]/td/div/input')
    time.sleep(0)
    login_btn.click()
    time.sleep(0)
    google_login_username = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
    google_login_username.send_keys(username)
    time.sleep(n)
    next_button = driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button')
    next_button.click()
    time.sleep(2)
    google_login_password = driver.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')
    google_login_password.send_keys(password)
    next_login = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button')
    next_login.click()
    time.sleep(2)
    driver.maximize_window()
    select_element = driver.find_element(By.XPATH, '//*[@id="sources"]')
    select = Select(select_element)
    select.select_by_value("387") #sorce id
    time.sleep(2)
    apply_source_button = driver.find_element(By.XPATH, '//*[@id="applySource"]')
    apply_source_button.click()
    driver.implicitly_wait(30)
    source_name = driver.find_element(By.XPATH, '//a[text()="Multiple Listings Services"]')
    driver.implicitly_wait(10)
    select_element_type = driver.find_element(By.XPATH, '//*[@id="metadataSelect"]')
    select_el = Select(select_element_type)
    select_el.select_by_index(3) #class id from 1
    time.sleep(10)
    listing_rule_commissions = driver.find_element(By.XPATH, '//*[@id="nav-home"]/div/table/tbody/tr[27]/td[4]/div/span')
    driver.implicitly_wait(30)
    listing_rule_commissions.click()
    listing_rule_commissions = driver.find_element(By.XPATH,
                                                   '//*[@id="rulesAutocomplete"]')
    listing_rule_commissions.click()
    select_element_rule = driver.find_element(By.XPATH, '//*[@id="foo"]')
    select_rule = Select(select_element_rule)
    select_rule.select_by_index(1) #rule id from 0
    button_create = driver.find_element(By.XPATH, '//*[@id="addForm"]/div/input')
    button_create.click()
    datetime_before_save = driver.find_element(By.XPATH, '//*[@id="last_edited"]/i')
    datetime_before_save_result = datetime_before_save.text
    button_save_map = driver.find_element(By.XPATH, '//*[@id="btn_save_map"]')
    button_save_map.click()
    time.sleep(2)
    pyautogui.FAILSAFE = False
    pyautogui.moveTo(1100, 230)
    pyautogui.click()
    time.sleep(12)
    datetime_after_save = driver.find_element(By.XPATH, '//*[@id="last_edited"]/i')
    datetime_after_save_result = datetime_after_save.text
    result = [datetime_before_save_result, datetime_after_save_result]

    return result



class AuthenticationTestCase(TestCase):

    def test_1_login_correct(self):
        correct_username = "a_andrusyk-itssv@kw.com"
        correct_password = "Components12!"
        actual = login_selenium(correct_username, correct_password)
        self.assertNotEqual(actual[1], actual[0])

    def test_2_login_correct(self):
        correct_username = "-------"
        correct_password = "-------"
        actual = login_selenium(correct_username, correct_password)
        self.assertNotEqual(actual[1], actual[0])



