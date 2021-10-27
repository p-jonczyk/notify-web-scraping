from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import shinden
import const

PATH = const.driver_path
chrome_options = Options()
# runs driver in background
chrome_options.add_argument("--headless")
# hides consol info
chrome_options.add_argument("log-level=3")
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)


def main():
    shinden.shinden_info(driver)


if __name__ == '__main__':
    main()
