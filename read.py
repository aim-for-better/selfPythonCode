#-*- coding:utf-8 -*-
def getLastLineFile(file):
    count=0
    for line in file:
        count+=1
    return count

file=open("../company_url_file.txt","r")
print getLastLineFile(file)
