# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 23:19:38 2019

@author: Emanuel&Mara
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
url = 'http://automationpractice.com/index.php'
driver = webdriver.Chrome(executable_path=r"C:\drivers\chromedriver.exe")
driver.get(url)
print(driver.title)
print(driver.current_url)
search = driver.find_element_by_name('search_query')
search.send_keys('Dress')
time.sleep(1)
button = driver.find_element_by_class_name('button-search')
button.click()
time.sleep(1)
#xpath = '//*[@id="center_column"]/ul/li[1]/div/div[2]/h5/a'
xpath = '//*[@id="center_column"]/ul/li[2]/div/div[2]/h5/a'
item = driver.find_element_by_xpath(xpath)
item.click()
time.sleep(1)
description = driver.find_element_by_tag_name('h1')
print(description.text)

#driver.close()