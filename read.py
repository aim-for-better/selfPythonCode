#-*- coding:utf-8 -*-
def getLastLineFile(file):
    count=0
    for line in file:
        count+=1
        if count<=30:
            print line
    return count

file=open("../company_url_file.txt","r")
file2=open("D:/patentsviewdata/tsvfile/nber.tsv")
print getLastLineFile(file)
