# -*- coding:utf-8 -*-
from selenium import webdriver
import json
import time


driver=webdriver.Chrome()
url="http://listings.findthecompany.com/l/7647344/Wal-Mart-Stores-Inc-in-Bentonville-AR"
driver.get(url)
# wait sometime
time.sleep(15)

first_group_xpath="/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div[2]/div/div/div/div/div/div[2]/div/div/div[1]/div"
employee_xpath=""
sales_volumes_xpath=""
net_income_xpath=""
market_cap_xpath=""
description_xpath=""
location_xpath="/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div[3]/section[1]/div[2]/div[2]/div/div/div/div[2]/div/div"
key_executives_xpath="/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div[3]/section[1]\
/div[2]/div[3]/div/div/div/div[1]/div/div/div/div/div[1]/table/tbody/tr"

# get all td the even index is the key and the odd index is value .
# the index 0 is key 1 is value 2 is key ...
key_facts_xpath="/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div[3]/section[1]/div[2]/div[4]/div/div[1]/div/div\
//table//td"
contact_xpath="/html/body/div[1]/div[2]/div/div/div[4]/div[3]/div[3]/section[1]/div[2]/div[4]/div/div[2]/div/div//table//td"

first_group=driver.find_elements_by_xpath(first_group_xpath)
employee=first_group[0].text
sales_volumes=first_group[1].text
net_income=first_group[2].text
market_cap=first_group[3].text
location=driver.find_element_by_xpath(location_xpath).text

key_executives=driver.find_elements_by_xpath(key_executives_xpath)

key_persons=[]
for person in key_executives:
    tmp_person={}

    info=person.find_elements_by_xpath("/td")
    tmp["name"]=info[1]
    tmp["position"]=info[2]
    tmp["year"]=info[3]
    tmp["totoal_annual_comp"]=info[4]
    tmp["change_in_comp"]=info[5]
    key_persons.append(tmp_person)

key_facts=driver.find_elements_by_xpath(key_facts_xpath)

facts={}
for i in range(0,len(key_facts),2):
    facts[key_facts[i].text]=key_facts[i+1].text

contact=driver.find_elements_by_xpath(contact_xpath)

contacts={}
for i in range(0,len(contact),2):
    contacts[contact[i].text]=contact[i+1].text

print employee

print facts

print contacts


# sales_volumes=driver.find_element_by_xpath(sales_volumes_xpath)
# net_income=driver.find_element_by_xpath(net_income_xpath)
# market_cap=driver.find_element_by_xpath(market_cap_xpath)
# description=driver.find_element_by_xpath(description_xpath)
# location=driver.find_element_by_xpath(location_xpath)
# key_executives=driver.find_element_by_xpath(key_executives_xpath)
# key_facts=driver.find_element_by_xpath(key_facts_xpath)
# contact=driver.find_element_by_xpath(contact_xpath)
