# -*- coding:utf-8 -*-
from selenium import webdriver
import json
import time


driver=webdriver.Chrome()
url="http://listings.findthecompany.com/l/7647344/Wal-Mart-Stores-Inc-in-Bentonville-AR"
driver.get(url)
# wait sometime
# time.sleep(15)
div_list = driver.find_element_by_xpath('//div[@class="ddh-field"]')
div_list=driver.find_element_by_xpath('//div[@class="card-sec-body"]')
div_list=driver.find_element_by_xpath("//section[@'data-section-id'=0]/div[1]")
print div_list
print driver.title