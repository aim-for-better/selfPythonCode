# -*- encoding: utf-8 -*-
from selenium import webdriver
import json
import time

def getLastLineFile(file):
    content=""
    for line in file:
        content=line
    return content

driver=webdriver.Chrome()
base_url="http://listings.findthecompany.com/ajax_search?_len=100&"
mid_url="&app_id=1662&_sortfld=sales_volume_us&_sortdir=DESC&"
company_base_url="http://listings.findthecompany.com/l/"
url_file=open("../condition_parameter.txt","r")
count=0
company_url_file=open("../company_url_file.txt","a+")
log_file=open("../log.txt","r+") # "r+" confirm start from 0
last_count=int(getLastLineFile(log_file))
try:
    for last_url in url_file:
        if count<last_count:
            count+=1
            continue
        total_page=10
        for page in range(total_page):
            entire_url=base_url+"page="+str(page)+mid_url+last_url
            driver.get(entire_url)
            time.sleep(15)  # very import or will get nothing by find
            try:
                # If  ip is limited then wait one hour
                while True:
                    if str(driver.title).rstrip(" ")=="Rate Limited":
                        time.sleep(3600)
                        driver.get(entire_url)
                        time.sleep(15)
                    else:
                        break
                res=str(driver.find_element_by_xpath("/html/body/pre").text).encode("utf-8")

                json_data=json.loads(res)
                # Two case will step into the following while loop:
                # First case: the request is normal ,but the time is short,
                # So,res is empty and the json_data isn't dict
                # Second case: the ip is limited: so res is not json
                while not isinstance(json_data,dict):
                    driver.get(entire_url)
                    time.sleep(20)
                    res=str(driver.find_element_by_xpath("/html/body/pre").text).encode("utf-8")
                    json_data=json.loads(res)

                companies_data=json_data["data"]["data"]
                while not isinstance(companies_data,list):
                    time.sleep(20)
                    json_data=json.loads(res)
                    companies_data=json_data["data"]["data"]
                for company in companies_data:
                    company_info={"name": company[1].encode("utf-8"),
                           "details_url": str(company_base_url + str(company[9]) + "/" +\
                            str(company[10])).encode( "utf-8"),
                            "total_employees":str(company[3]["raw"]).encode("utf-8"),
                            "employees_here":str(company[4]["raw"]).encode("utf-8"),
                            "sales_volume":str(company[5]["formatted"]).encode("utf-8"),
                            # "location":" ".join([x.encode("utf-8") for x in company[12:])
                            "location": " ".join([x.encode("utf-8") for x in company[12:]])
                           }
                    company_url_file.write(json.dumps(company_info)+"\n")
                    print "finish write one company URL \n "
                # driver.close()
                print "finish crawl %s page company URL \n "% page
                if len(companies_data)<100:
                    break
            except:
                print "something wrong"
                continue
        # driver.quit()
        # time.sleep(60)
        count+=1
        log_file.write(str(count)+"\n")
        print "finish crawl %s condition URL, \n"%count
finally:
    url_file.close()
    log_file.close()
