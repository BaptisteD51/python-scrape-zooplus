from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

import re
import time

def scrape_back():
    lang = input("Language code (two lower case letters):")
    admin_url = input("The url to the Magazine admin (with the slash at the end):")

    user_name = input("Your Wordpress username:")
    password = input("Your Wordpress password:")

    driver = webdriver.Chrome()
    driver.get(admin_url+"wp-admin/edit.php?post_status=publish&post_type=post&lang=de&admin_bar=1")

    login_field = driver.find_element(By.ID, "user_login")
    password_field = driver.find_element(By.ID, "user_pass")
    submit_button = driver.find_element(By.ID, "wp-submit")

    login_field.send_keys(user_name)
    password_field.send_keys(password)
    submit_button.click()

    pages_number = driver.find_element(By.CLASS_NAME, 'total-pages').get_attribute("innerHTML")
    pages_number = int(pages_number)

    trs = []

    for i in range(1, pages_number+1):
        driver.get(admin_url + "wp-admin/edit.php?post_status=publish&post_type=post&lang=de&admin_bar=1&paged="+str(i))
        elmts = driver.find_elements(By.CSS_SELECTOR, "#the-list tr")
        for elmt in elmts:
            html = elmt.get_attribute("innerHTML")
            trs.append(html)


    pairs = []

    for tr in trs:
        soup = BeautifulSoup(tr, 'html.parser')
        german_url = soup.select_one("span.view a").get("href")
        edit_url = soup.select_one("a[data-language='"+lang+"']").get("href")
        regex = r"[0-9]+"
        match = re.search(regex, edit_url)
        id = match[0]
        german_title = soup.select_one("a.row-title").getText()
        pair = {"german_url":german_url,"id":id,"german_title":german_title}
        print(pair)
        pairs.append(pair)


    print(pairs)

    def write_csv(pairs):
        f = open("results-back.csv", "a", encoding="utf-8")
        for pair in pairs:
            f.write(pair["german_url"]+",\""+pair["german_title"]+"\","+pair["id"]+"\n")


    write_csv(pairs)

    driver.close()