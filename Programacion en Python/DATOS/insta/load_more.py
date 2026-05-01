# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup
import urllib

driver = webdriver.Chrome('./chromedriver')  # or webdriver.Firefox()
driver.get("https://www.instagram.com/luisdelcastillo.official/")

wait = WebDriverWait(driver, 10)
while True:
    try:
        load_more = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Cargar más')))
    except TimeoutException:
        break

    load_more.click()

def instagram():
    list_ = []
    result_list = []
    html =  urllib.urlopen(instagram_url).read()
    soup = BeautifulSoup(html,'html.parser')
    likes =  soup.find_all('body')
    string = str(likes)
    for i in range(0,len(string)):
        if string[i:i+10] == '"caption":':
            jackpot =  string[i+10:i+500]
            list_.append(jackpot)
    for i in range(0, len(list_)):
        number = ''
        print list_[i]
        """for j in range(0,len(list_[i])):
            if list_[i][j] in '0123456789':
                number = number + list_[i][j]
        result_list.append(int(number))"""

    return result_list

instagram_url = 'https://www.instagram.com/luisdelcastillo.official/'

instagram()


"""for item in driver.find_elements_by_css_selector("div.gig-item h3 a.gig-link-main"):
    print item.text.strip()"""