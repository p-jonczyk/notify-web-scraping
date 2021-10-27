from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from dotenv import load_dotenv
import os
import time
import const

load_dotenv()

SHIN_USER = os.getenv('SHIN_USER', 'default_user')
SHIN_PASSWORD = os.getenv('SHIN_PASSWORD', 'default_pass')


def shinden_login(driver):
    """Login user to shinden.pl

    Parameter:
    driver: webdriver 
    """

    driver.get(const.shinden_login_url)

    print("----SHINDEN INFO----\n")

    try:
        privacy_accept = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".details_footer--1RwcL button:nth-child(2)")), const.msg_timed_out)
        privacy_accept.click()
        cookies_accept = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "cb-enable")), "Timed out waiting for element")
        cookies_accept.click()
    except NoSuchElementException:
        driver.quit()

    login = driver.find_element(
        By.CSS_SELECTOR, ".l-main-contantainer input:nth-child(2)")
    login.send_keys(SHIN_USER)
    password = driver.find_element(
        By.CSS_SELECTOR, ".l-main-contantainer input:nth-child(4)")
    password.send_keys(SHIN_PASSWORD)
    password.send_keys(Keys.RETURN)


def shinden_info(driver):
    """Gets user watch list from shinden.pl

    Parameter:
    driver: webdriver """

    shinden_login(driver)
    driver.get(const.shinden_user_watch_list)
    to_watch_list = driver.find_elements(By.CLASS_NAME, "media-item")
    count = len(to_watch_list)
    user_name = driver.find_element(
        By.CSS_SELECTOR, "aside.mobile-close img").get_attribute("alt")
    print(user_name, "\n")
    for i in range(1, count):
        title = driver.find_element(
            By.CSS_SELECTOR, f"li:nth-child({i}) h4 a")
        number_of_episode = driver.find_element(
            By.CSS_SELECTOR, f"li:nth-child({i}) .episodes td:nth-child(1)")
        title_of_episode = driver.find_element(
            By.CSS_SELECTOR, f"li:nth-child({i}) .episodes td:nth-child(2)")
        language_of_episode = driver.find_elements(
            By.CSS_SELECTOR, f"li:nth-child({i}) .episodes td:nth-child(3) span")

        languages = [elem.get_attribute("title")
                     for elem in language_of_episode]

        print(f"{i}: {title.text}")
        print(
            f"    Episode -> {number_of_episode.text}. {title_of_episode.text}")
        print(f"    Languages -> {' / '.join(languages)}\n")
