import stuffs
import ultis
import json

from numpy import random
from time import sleep



def search_trending_post(driver):

    output = []
    links = ultis.Ultility().post_searcher(driver)
    list = []
    for post_url in links:
        if "photo" in post_url:
            print("Post đổi ảnh đại diện, ảnh bìa nên bỏ qua")
            continue
        elif "group" not in post_url:
            split = post_url.split("&eav=", 1)
            list.append(split[0])
        else:
            split = post_url.split("refid", 1)
            list.append(split[0])
    content = ""
    comment = []
    for out in list:
        print("\n" + str(out))
        sleep(random.uniform(5, 7))
        content = stuffs.scraping(out, driver).find_post_content()
        sleep(random.uniform(5, 7))
        comment = stuffs.scraping(out, driver).find_comment()
        sleep(random.uniform(5, 7))
        like, haha, love, sad, wow, tt = stuffs.scraping(out, driver).find_post_reaction()
        dict = {
            "Content": content,
            "Comment list": comment,
            "Reactions": {
                "Like": like,
                "Haha": haha,
                "Love": love,
                "Sad": sad,
                "Wow": wow,
                "Thương thương": tt
            }
        }
        output.append(dict)
    with open('output.json', 'w', encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
    
def search_post_in_group(driver):
    group_link = input("Nhap link den group (mbasic): ")
    group_link = str(group_link).replace("www.facebook", "mbasic.facebook")
    main = stuffs.scraping(group_link,driver).find_posts()
    
    list = []
    for story_link in main:
        sleep(random.uniform(5, 7))
        post_url = story_link.get_attribute("href")
        if "photo" in post_url:
            print("Post đổi ảnh đại diện, ảnh bìa nên bỏ qua")
            continue
        elif "group" not in post_url:
            split = post_url.split("&eav=", 1)
            list.append(split[0])
        else:
            split = post_url.split("refid", 1)
            list.append(split[0])
    with open("post_links.json", "w", encoding="utf-8") as f:
        f.write(json.dumps(list))
    output = []
    content = ""
    comment = []    
    for out in list:
        print("\n" + str(out))
        sleep(random.uniform(5, 7))
        content = stuffs.scraping(out, driver).find_post_content()
        sleep(random.uniform(5, 7))
        comment = stuffs.scraping(out, driver).find_comment()
        sleep(random.uniform(5, 7))
        like, haha, love, sad, wow, tt = stuffs.scraping(out, driver).find_post_reaction()
        dict = {
            "Content": content,
            "Comment list": comment,
            "Reactions": {
                "Like": like,
                "Haha": haha,
                "Love": love,
                "Sad": sad,
                "Wow": wow,
                "Thương thương": tt
            }
        }
        output.append(dict)
    with open('output.json', 'w', encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
    
def search_for_page(driver):
    links = ultis.Ultility().page_searcher(driver)
    output = []
    content = ""
    comment = []   
    for link in links:
        print(link)
    for page in links:
        main = stuffs.scraping(page,driver).find_posts()
        list = []
        for story_link in main:
            sleep(random.uniform(5, 7))
            post_url = story_link.get_attribute("href")
            if "photo" in post_url:
                print("Post đổi ảnh đại diện, ảnh bìa nên bỏ qua")
                continue
            elif "group" not in post_url:
                split = post_url.split("&eav=", 1)
                list.append(split[0])
            else:
                split = post_url.split("refid", 1)
                list.append(split[0])
        with open("post_links.json", "w", encoding="utf-8") as f:
            f.write(json.dumps(list))
         
        for out in list:
            print("\n" + str(out))
            sleep(random.uniform(5, 7))
            content = stuffs.scraping(out, driver).find_post_content()
            sleep(random.uniform(5, 7))
            comment = stuffs.scraping(out, driver).find_comment()
            sleep(random.uniform(5, 7))
            like, haha, love, sad, wow, tt = stuffs.scraping(out, driver).find_post_reaction()
            dict = {
                "Content": content,
                "Comment list": comment,
                "Reactions": {
                    "Like": like,
                    "Haha": haha,
                    "Love": love,
                    "Sad": sad,
                    "Wow": wow,
                    "Thương thương": tt
                }
            }
            output.append(dict)
    with open('output.json', 'w', encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
        
def search_for_post_details(driver):
    output = []
    content = ""
    comment = []
    out = input("Nhap post URL: ")
    sleep(random.uniform(5, 7))
    content = stuffs.scraping(out, driver).find_post_content()
    sleep(random.uniform(5, 7))
    comment = stuffs.scraping(out, driver).find_comment()
    sleep(random.uniform(5, 7))
    like, haha, love, sad, wow, tt = stuffs.scraping(out, driver).find_post_reaction()
    dict = {
        "Content": content,
        "Comment list": comment,
        "Reactions": {
            "Like": like,
            "Haha": haha,
            "Love": love,
            "Sad": sad,
            "Wow": wow,
            "Thương thương": tt
        }
    }
    output.append(dict)
    with open('output.json', 'w', encoding="utf-8") as f:
        json.dump(output, f, indent=4, ensure_ascii=False)
try:
    driver = ultis.Ultility().login()
    while(1):
        print("1. Tim bai viet theo trend")
        print("2. Tim bai viet trong nhom")
        print("3. Tim fanpage theo tu khoa")
        print("4. Tim thong tin cua 1 bai viet")
        print("5. Thoat")
        choice = input("Lua chon cua ban: ")
        if choice == "1":
            print("You chose option 1.")
            search_trending_post(driver)
        elif choice == "2":
            print("You chose option 2.")
            search_post_in_group(driver)
        elif choice == "3":
            print("You chose option 3.")
            search_for_page(driver)
        elif choice == "4":
            print("You chose option 4.")
            search_for_post_details(driver)
        elif choice == "5":
            print("Exiting...")    
            break
        else:
            print("Gia tri khong hop le")
    print("Driver quit inside try block")
    driver.quit()
finally:
    print("Driver quit outside try block")
    driver.quit()