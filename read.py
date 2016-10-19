#coding=utf-8
f1 =open('condition_parameter.txt','r')
a=0
for line in f1:
	if a==0:
		print line
		a+=1
