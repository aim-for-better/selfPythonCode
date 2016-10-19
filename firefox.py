# -*- encoding: utf-8 -*-
from selenium import webdriver
import json
import time

driver=webdriver.Chrome()
base_url="http://listings.findthecompany.com/ajax_search?_len=100&"
mid_url="&app_id=1662&_sortfld=sales_volume_us&_sortdir=DESC&"

url_file=open("condition_parameter.txt","r")
count=0
company_url_file=open("company_url_file.txt","a+")
log_file=open("log.txt","a+")
for last_url in url_file;
    total_page=11
    for page in range(total_page):
        entire_url=base_url+"page="+page+mid_url+last_url
        driver.get(entire_url)
        time.sleep(10)  # very import or will get nothing by find
        res=str(driver.find_element_by_xpath("/html/body/pre").text).encode("utf-8")
        json_data=json.load(res)
        companies_data=json_data["data"]["data"]
        for company in companies_data:
            company_info={"name": company[1].encode("utf-8"),
                   "logo_url": str(_company_logo_base_url + (company[0][0] if len(company[0]) > 0 else "")).encode(\
                       "utf-8"),
                   "details_url": str(_company_details_base_url + str(company[9]) + "/" + str(company[10])).encode(\
                       "utf-8"),
                   "total_employees": str(company[3]["raw"]).encode("utf-8")
                   }
            company_url_file.write(json.JSONEncoder(company_info)+"\n")
        driver.close()
        if len(companies_data)<100:
            break
    driver.quit()
    time.sleep(20)
    count+=1
    log_file.write(count+"\n")



# url1="http://listings.findthecompany.com/ajax_search?_len=20&page=0&app_id=1662&_sortfld=sales_volume_us&_sortdir=DESC&_fil%5B0%5D%5Bfield%5D=sic_all_divisions&_fil%5B0%5D%5Boperator%5D=%3D&_fil%5B0%5D%5Bvalue%5D=D&_fil%5B1%5D%5Bfield%5D=phys_country_code&_fil%5B1%5D%5Boperator%5D=%3D&_fil%5B1%5D%5Boptional%5D=false&_fil%5B1%5D%5Bvalue%5D=805&_tpl=srp&head%5B%5D=_i_1&head%5B%5D=company_name&head%5B%5D=_GC_address&head%5B%5D=total_employees&head%5B%5D=employees_here&head%5B%5D=sales_volume_us&head%5B%5D=year_started&head%5B%5D=citystate&head%5B%5D=localeze_classification&head%5B%5D=id&head%5B%5D=_encoded_title&head%5B%5D=name_state_tit&head%5B%5D=phys_address&head%5B%5D=phys_city&head%5B%5D=phys_state&head%5B%5D=phys_country_code&head%5B%5D=phys_zip"
# url2="http://www.baidu.com"
# driver.get(url1)
# file=open("z.json","w")
# time.sleep(8)
# x=str(driver.find_element_by_xpath("/html/body/pre").text).encode("utf-8")
# file.write(json.dumps(x))
# jsondata=json.load(file)
# print len(jsondata)
# driver.close()
# driver.quit()
