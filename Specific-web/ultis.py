from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException

from numpy import random
from time import sleep
import json
ffOptions = webdriver.FirefoxOptions()
ffOptions.add_argument('--headless')
ffOptions.add_argument('--disable-gpu')
ffOptions.add_argument("--disable-xss-auditor")
ffOptions.add_argument('--disable-dev-shm-usage')
ffOptions.add_argument(
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')

llist = []
lists = []

driver = webdriver.Firefox(service=Service(
    GeckoDriverManager().install()), options=ffOptions)
driver.get("http://suckhoeviet.gov.vn/tra-cuu-thong-tin-dinh-duong/tong-quat")
links = driver.find_elements(By.XPATH, "//h3//descendant::a")

for link in links:
    lists.append(link.get_attribute('href'))
for link in lists:
    driver.get(link)
    data = driver.find_elements(
        By.XPATH, "//div[contains(@class, 'content')]/descendant::p")
    title = driver.find_element(By.XPATH, "//h1").text
    print(title)
    content = [element.text for element in data]
    ddict = {
        "Title": title,
        "Content": content
    }
    llist.append(ddict)
with open('data.json', 'w', encoding="utf-8") as f:
    json.dump(llist, f, indent=4, ensure_ascii=False)
