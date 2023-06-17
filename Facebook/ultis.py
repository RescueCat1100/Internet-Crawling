from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException

from numpy import random
from time import sleep

import stuffs

class Ultility():
    def __init__(self) -> None:
        pass
    
    def login(self):
        
        ffOptions = webdriver.FirefoxOptions()
        ffOptions.add_argument('--user-data-dir=Profiles')
        ffOptions.add_argument('--headless')
        ffOptions.add_argument('--disable-gpu')
        ffOptions.add_argument("--disable-xss-auditor")
        ffOptions.add_argument('--disable-dev-shm-usage')
        ffOptions.add_argument('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')


        driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()), options=ffOptions)
        
        driver.get("https://mbasic.facebook.com")
        
        sleep(random.uniform(2, 5))
        try:
            username = driver.find_element(By.NAME, 'email')
        except NoSuchElementException:
            print("Element email not found, cannot log in")
        else:
            username.clear()
            username.send_keys("account here")

        sleep(random.uniform(2, 5))
        try:
            password = driver.find_element(By.NAME, 'pass')
        except NoSuchElementException:
            print("Element password not found, cannot log in")
        else:
            password.clear()
            password.send_keys("password here")

        sleep(random.uniform(2, 5))
        try:
            login = driver.find_element(By.NAME, 'login')
        except NoSuchElementException:
            print("Element login button not found, cannot log in")
        else:
            login.click()

        sleep(random.uniform(2, 5))
        try:
            not_now = driver.find_element(By.CSS_SELECTOR, 'a[href*="/cancel/"]')
        except NoSuchElementException:
            print("Element skip not found, cannot log in")
        else:
            not_now.click()

        return driver
    
    def page_searcher(self, driver):
        search_link = "https://mbasic.facebook.com/search/pages/?q="
        input_string = input("Nhập để tìm kiếm: ")
        search_link += input_string
        print(search_link)
        driver.get(search_link)
        search_results = driver.find_element(By.ID, "BrowseResultsContainer")
        a_elements = search_results.find_elements(By.XPATH, ".//a[img]")
        links = []
        for a_element in a_elements:
            output = a_element.get_attribute("href")
            if "?fan" not in output: # Bỏ qua đường dẫn nút like
                if "eav" in output:
                    output = output.split("eav")[0]
                    if "refid" in output:
                        output = output.split("refid")[0]
                        links.append(output)
                        #print(output)
                elif "refid" in output:
                    output = output.split("refid")[0]
                    if "eav" in output:
                        output = output.split("eav")[0]
                        links.append(output)
                        #print(output)
                        
        return links
    
    def post_searcher(self, driver):
        search_link = "https://mbasic.facebook.com/search/posts/?source=filter&isTrending=1&q="
        input_string = input("Nhập để tìm kiếm: ")
        search_link += input_string
        print(search_link)
        output = []
        for i in range(2):
            sleep(random.uniform(5, 7))
            driver.get(search_link)
            links = driver.find_elements(By.LINK_TEXT, "Full Story")
            for link in links:
                link = link.get_attribute("href")
                output.append(link)
            search_link = driver.find_element(By.XPATH, "//div[@id='see_more_pager']//descendant::a").get_attribute("href")                       
        return output
    