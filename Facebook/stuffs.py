from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


import ultis
import requests

from numpy import random
from time import sleep

class scraping():
    def __init__(self, url, driver):
        self.url = url
        self.driver = driver    

    def find_posts(self):
        print("start")
        driver = self.driver
        print("logged in")
        driver.get(self.url)
        print("redirecting...")
        story_links = driver.find_elements(By.LINK_TEXT, "Full Story")
        print("done")
        return story_links
    
    
    def find_comment(self):
        driver = self.driver
        url_string = self.url
        url_string += "&p="
        temp = 0
        check = 1
        output = []
        
        while (check):
            try: 
                sleep(random.uniform(7, 10))
                url = url_string
                url += str(temp)
                print("redirecting to " + str(url))
                #sleep(random.uniform(7, 10))
                #driver.get(url)
                print("redirected")
                sleep(random.uniform(7, 10))
                users = driver.find_elements(By.XPATH, '//h3[not(@class)]')
                #users_non_blank = [str(user.text).strip() for user in users if str(user.text).strip()]
                for user in users:
                    if str(user.text).strip():
                        print(user.text)
                        comment = user.find_element(By.XPATH, './following-sibling::div[1]')
                        print(comment.text)
                        dict = {
                            "User": user.text,
                            "Comment": comment.text
                        }
                        output.append(dict)
                print(len([str(user.text).strip() for user in users if str(user.text).strip()]))
                check = len([str(user.text).strip() for user in users if str(user.text).strip()])
                view_more = driver.find_element(By.XPATH, '//div[contains(@id, "see_next_")]//descendant::a')
                view_more.click()
                temp += 10
                
            except NoSuchElementException:
                print("Không tìm được HTML element mong muốn \
                      \nCó thể tài khoản bị tạm timeout hoặc kết nối có vấn đề \
                      \nCần kiểm tra lại thủ công")
                break
            
        return output

    def find_post_content(self):
        driver = self.driver
        url = self.url
        sleep(random.uniform(7, 10))
        driver.get(url)
        sleep(random.uniform(7, 10))
        contents = driver.find_elements(By.TAG_NAME, 'p')
        output = ""
        if len(contents):
            print("Nội dung post raw")
            for content in contents:
                output += str(content.text) + "\n"
        else:
            print("Nội dung có format khác thường \
                  \nNếu không có gì xuất hiện, có lẽ đó chỉ là ảnh")
            contents = driver.find_elements(By.XPATH, '//span[contains(@style, "font-size:")]')
            for content in contents:
                output += str(content.text) + "\n"
        return output
    
    def find_post_reaction(self):
        url = self.url
        driver = self.driver
        if "group" in url:
            token = str(url).split("/")[-2]
            print(token)
        else:
            token = str(url).split("&")[0].split("=")[1]
            print(token)
        url_string = "https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier="
        url_string += token
        print(url_string)
        sleep(random.uniform(7, 10))
        driver.get(url_string)
        number_of_tt = 0
        number_of_wow = 0
        number_of_haha = 0
        number_of_like = 0
        number_of_love = 0
        number_of_sad = 0
        # LIKE
        try:
            image = driver.find_element(By.XPATH, '//img[contains(@src, \
            "An_UvxJXg9tdnLU3Y5qjPi0200MLilhzPXUgxzGjQzUMaNcmjdZA6anyrngvkdub33NZzZhd51fpCAEzNHFhko5aKRFP5fS1w_lKwYrzcNLupv27.png")]')
            number_of_like = image.find_element(By.XPATH, './following-sibling::span').text
            print("So luong like " + str(number_of_like))
        except NoSuchElementException:
            print("Khong co like nao ca")
        # LOVE
        try:
            image = driver.find_element(By.XPATH, '//img[contains(@src, \
            "An-SJYN61eefFdoaV8pa0G_5_APCa0prZaqkZGXpCFeUCLCg89UPOqSkSZxJkLy0hAKKpUIPEB91mo9yBBfcAqcwmpEu5jN_jmJufFtJoVJCUklu.png")]')
            number_of_love = image.find_element(By.XPATH, './following-sibling::span').text
            print("So luong love " + str(number_of_love))
        except NoSuchElementException:
            print("Khong co love nao ca")
        # HAHA
        try:
            image = driver.find_element(By.XPATH, '//img[contains(@src, \
            "An_F9bJG7govfshSMBkvcRLcxT0jmiXVYKtr7lgH5AHgUrjjpZ1OD0xyxXYgf7arc0lWgCdrR_KN4Mg7RSN3Gm3W6Gg03N1tQ-ZXzVvFJ_KvvB4.png")]')
            number_of_haha = image.find_element(By.XPATH, './following-sibling::span').text
            print("So luong haha " + str(number_of_haha))
        except NoSuchElementException:
            print("Khong co haha nao ca")
        # SAD
        try:
            image = driver.find_element(By.XPATH, '//img[contains(@src, \
            "An-0mG6nK_Uk-eBw_Z5hXaQPl2Il-GAtgNisMF_CPi6qvu85Lx2-5PalMJvS7fIbuodHct0V3tJrvSxzau9mOcNxqVhoiy8lxxQ9edz-6r6_o9YroQ.png")]')
            number_of_sad = image.find_element(By.XPATH, './following-sibling::span').text
            print("So luong sad " + str(number_of_sad))
        except NoSuchElementException:
            print("Khong co sad nao ca")
        # WOW
        try:
            image = driver.find_element(By.XPATH, '//img[contains(@src, \
            "An_0KlxkBZwTJgSV9p2pDQkaZcuO9nFP4R72nyZmCnWKIxG_MSUbtZ_uBFHkKhQVvjgeou7ijfWCAKaRfSRFqQS9RcziMUL4BTtfpxJ2KfylUgpq.png")]')
            number_of_wow = image.find_element(By.XPATH, './following-sibling::span').text
            print("So luong sad " + str(number_of_wow))
        except NoSuchElementException:
            print("Khong co wow nao ca")
        # Thuong
        try:
            image = driver.find_element(By.XPATH, '//img[contains(@src, \
            "An-9fyYLftTy_Mg2cJpugh-vEVNfbtI-fVn4FNS7K-sgIMu9pT62Tb1u9Dfm-xYLtjbLQk-yVHp_IlY_4iMVYp0xLpO7sJvbxbC2OIiRxzS02cOuKEoo.png")]')
            number_of_tt = image.find_element(By.XPATH, './following-sibling::span').text
            print("So luong thuong thuong " + str(number_of_tt))
        except NoSuchElementException:
            print("Khong co thuong thuong nao ca")
            
        return number_of_like, number_of_haha, number_of_love, number_of_sad, number_of_wow, number_of_tt

        