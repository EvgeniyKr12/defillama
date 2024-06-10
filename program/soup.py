import time
from bs4 import BeautifulSoup
from selenium import webdriver
from fake_useragent import UserAgent
from selenium.webdriver.chrome.service import Service


def get_soup(url):
    ua = UserAgent()
    user_agent = ua.random

    service = Service(executable_path='program/settings/chromedriver-win64/chromedriver.exe')
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(service=service, options=chrome_options)
    try:
        driver.get(url=url)
        time.sleep(1)
        # driver.execute_script("document.body.style.zoom='80%'")
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        soup = BeautifulSoup(driver.page_source, 'lxml')
    except Exception as ex:
        print(ex)
        soup = ''
    finally:
        driver.close()
        driver.quit()

    return soup
