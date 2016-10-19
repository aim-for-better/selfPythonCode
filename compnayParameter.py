import json


'''
This module mainly  generate the filter conditions of the target URL.
mainly conditions is _fil parameters :
"sic_all_divisions":"A-J"  "field,operator value"
"sic_all_2digit":"10-99"
"sic_all_4digit":"1011"
"collection_sales_volume_us":"1-10"   "field,operator value[]"
"collection_total_employees":"1-8"
"collection_employees_here":"1-8"
"status_id":"0-2"
"pub_pri_id":"0,1"   "field,operator optional value"
the entire URL as the follow:
("http://listings.findthecompany.com/ajax_search?_len=20&page=0&app_id=1662\
&_sortfld=sales_volume_us&_sortdir=DESC&_fil[0][field]=sic_all_divisions
&_fil[0][operator]==&_fil[0][value]=J&_fil[1][field]=sic_all_2digit\
&_fil[1][operator]==&_fil[1][value]=97&_fil[2][field]=sic_all_4digit\
&_fil[2][operator]==&_fil[2][value]=9721\
&_fil[3][field]=collection_sales_volume_us&_fil[3][operator]==\
&_fil[3][value][]=1&_fil[3][value][]=3&_fil[3][value][]=10\
&_fil[4][field]=collection_total_employees&_fil[4][operator]==\
&_fil[4][value][]=1&_fil[4][value][]=8 \
&_fil[5][field]=collection_employees_here&_fil[5][operator]==\
&_fil[5][value][]=1&_fil[5][value][]=8&_fil[6][field]=status_id\
&_fil[6][operator]==&_fil[6][value][]=2&_fil[6][value][]=0\
&_fil[7][field]=pub_pri_id&_fil[7][operator]==&_fil[7][optional]=false&_fil[7][value]=1\
&_fil[8][field]=phys_country_code&_fil[8][operator]==&_fil[8][optional]=false\
&_fil[8][value]=805&_tpl=srp&head[]=_i_1&head[]=company_name\
&head[]=_GC_address&head[]=total_employees&head[]=employees_here\
&head[]=sales_volume_us&head[]=year_started&head[]=citystate\
&head[]=localeze_classification&head[]=id&head[]=_encoded_title\
&head[]=name_state_tit&head[]=phys_address&head[]=phys_city&head[]=phys_state\
&head[]=phys_country_code&head[]=phys_zip
")
'''


prefix_url="http://listings.findthecompany.com/ajax_search?_len=100&page=0&app_id=1662\
&_sortfld=sales_volume_us&_sortdir=DESC&"

suffix_url="&_tpl=srp&head[]=_i_1&head[]=company_name\
&head[]=_GC_address&head[]=total_employees&head[]=employees_here\
&head[]=sales_volume_us&head[]=year_started&head[]=citystate\
&head[]=localeze_classification&head[]=id&head[]=_encoded_title\
&head[]=name_state_tit&head[]=phys_address&head[]=phys_city&head[]=phys_state\
&head[]=phys_country_code&head[]=phys_zip"
rawdata={
"A":{},
"B":
{"10":["11","21","41","44","61","81","94","99"],
"12":["21","22","31","41"],
"13":["11","21","81","82","89"],
"14":["11","22","23","29","42","46","55","59","74","75","79","81","99"],
 },
"C":
{
"15":["21","22","31","41","42"],
"16":["11","22","23","29"],
"17":["11","21","31","41","42","43","51","52",
      "61","71","81","91","93","94","95","96","99"],
},
"D":
{
"20":["11","13","15","21","22","23","24","26","32",\
      "33","34","35","37","38","41","43","44","45","46",\
      "47","48","51","52","53","61","62","63","64","66",\
      "67","68","74","75","76","77","79","82","83","84","85",\
      "86","87","91","92","95","96","97","98","99"],
"21":["11","21","31","41"],
"22":["11","21","31","41","51","52","53","54","57","58","59",\
      "61","62","69","73","81","82","84","95","96","97","98","99"],
"23":["11","21","23","25","26","29","31","35","37","39","41",\
      "42","53","61","69","71","81","84","85","86","87","89",\
      "91","92","93","94","95","96","97","99"],
"24":["11","21","26","29","31","34","35","36","39","41","48",\
      "49","51","52","91","93","99"],
"25":["11","12","14","15","17","19","21","22","31","41","42",\
      "91","99"],
"26":["11","21","31","52","53","55","56","57","71","72","73",\
      "74","75","76","77","78","79"],
"27":["11","21","31","32","41","52","54","59","61","71","82",\
      "89","91","96"],
"28":["12","13","16","19","21","22","23","24","33","34","35",\
      "36","41","42","43","44","51","61","65","69","71","72",\
      "73","74","75","91","92","93","95","99"],
"29":["11","51","52","92","99"],
"30":["11","21","52","53","61","69","81","82","83","84","85",\
      "86","87","88","89"],
"31":["11","31","42","43","44","49","51","61","71","72","99"],
"32":["11","21","29","31","41","51","53","55","59","61","62",\
      "63","64","69","71","72","73","74","75","81","91","92",\
      "95","96","97","99"],
"33":["12","13","15","16","17","21","22","24","25","31","34",\
      "39","41","51","53","54","55","56","57","63","64","65",\
      "66","69","98","99"],
"34":["11","12","21","23","25","29","31","32","33","41","42",\
      "43","44","46","48","49","51","52","62","63","65","66",\
      "69","71","79","82","83","84","89","91","92","93","94",\
      "95","96","97","98","99"],
"35":["11","19","23","24","31","32","33","34","35","36","37",\
      "41","42","43","44","45","46","47","48","49","52","53",\
      "54","55","56","59","61","62","63","64","65","66","67",\
      "68","69","71","72","75","77","78","79","81","82","85",\
      "86","89","92","93","94","96","99"],
"36":["12","13","21","24","25","29","31","32","33","34","35",\
      "39","41","43","44","45","46","48","51","52","61","63",\
      "69","71","72","74","75","76","77","78","79","91","94",\
      "95","99"],
"37":["11","13","14","15","16","21","24","28","31","32","43",\
      "51","61","64","69","92","95","99"],
"38":["12","21","22","23","24","25","26","27","29","41","42",\
      "43","44","45","51","61","73"],
"39":["11","14","15","31","42","44","49","51","52","53","55",\
      "61","65","91","93","95","96","99"]
},
"E":
{
"40":["11","13"],
"41":["11","19","21","31","41","42","51","73"],
"42":["12","13","14","15","21","22","25","26","31"],
"43":["11"],
"44":["12","24","32","49","81","82","89","91","92","93","99"],
"45":["12","13","22","81"],
"46":["12","13","19"],
"47":["24","25","29","31","41","83","85","89"],
"48":["12","13","22","32","33","41","99"],
"49":["11","22","23","24","25","31","32","39","41","52","53","59","61","71"]
},
"F":
{
"50":["12","13","14","15","21","23","31","32","33","39","43","44","45","46",\
      "47","48","49","51","52","63","64","65","72","74","75","78","82","83",\
      "84","85","87","88","91","92","93","94","99"],
"51":["11","12","13","22","31","36","37","39","41","42","43","44","45","46",\
      "47","48","49","53","54","59","62","69","71","72","81","82","91","92",\
      "93","94","98","99"]
},
"G":
{
"52":["11","31","51","61","71"],
"53":["11","31","99"],
"54":["11","21","31","41","51","61","99"],
"55":["11","21","31","41","51","61","71","99"],
"56":["11","21","32","41","51","61","99"],
"57":["12","13","14","22","31","34","35","36"],
"58":["12","13"],
"59":["12","21","32","41","42","43","44","45","46","47","48","49","61","62",\
      "63","83","84","89","92","93","94","95","99"]
},
"H":
{
"60":["11","19","21","22","29","35","36","61","62","81","82","91","99"],
"61":["11","41","53","59","62","63"],
"62":["11","21","31","82","89"],
"63":["11","21","24","31","51","61","71","99"],
"64":["11"],
"65":["12","13","14","15","17","19","31","41","52","53"],
"67":["12","19","22","26","32","33","92","94","98","99"]
},
"I":
{
"70":["11","21","32","33","41"],
"72":["11","12","13","15","16","17","18","19","21","31","41","51","61","91",\
      "99"],
"73":["11","12","13","19","22","23","31","34","35","36","38","42","49","52",\
      "53","59","61","63","71","72","73","74","75","76","77","78","79","81",\
      "82","83","84","89"],
"75":["13","14","15","19","21","32","33","34","36","37","38","39","42","49"],
"76":["22","23","29","31","41","92","94","99"],
"78":["12","19","22","29","32","33","41"],
"79":["11","22","29","33","41","48","91","92","93","96","97","99"],
"80":["11","21","31","41","42","43","49","51","52","59","62","63","69","71",\
      "72","82","92","93","99"],
"81":["11"],
"82":["11","21","22","31","43","44","49","99"],
"83":["22","31","51","61","99"],
"84":["12","22"],
"86":["11","21","31","41","51","61","99"],
"87":["11","12","13","21","31","32","33","34","41","42","43","44","48"],
"88":[],
"89":["99"]
},
"J":
{
"91":["11","21","31","99"],
"92":["11","21","22","23","24","29"],
"93":["11"],
"94":["11","31","41","51"],
"95":["11","12","31","32"],
"96":["11","21","31","41","51","61"],
"97":["11","21"],
"99":[]
}
}
collection_sales_volume_us=["1","2","3","4","5","6","7","8","9","10"]
collection_total_employees=["1","2","3","4","5","6","7","8"]
collection_employees_here=["1","2","3","4","5","6","7","8"]
status_id=["0","1","2"]
pub_pri_id=["0","1"]
print len(rawdata)

# for x in sorted(rawdata.keys()):
#     print "first parameter is :",x
#     if len(rawdata[x])==0:
#         continue
#     for y in rawdata[x].keys():
#         print "second parameter is :",y
#         for z in rawdata[x][y]:
#             print "third parameter is :",y+z


def combineSuffixCondition(count,prefix_condition):
    for volume in collection_sales_volume_us:
        count2=count+1
        tmp="_fil["+str(count2)+"]"
        condition_url=tmp+"[field]=collection_sales_volume_us&"+tmp+\
        "[operator]==&"+tmp+"[value]="+volume+"&"
        for total_employees in collection_total_employees:
            count3=count2+1
            tmp="_fil["+str(count3)+"]"
            condition_url2=tmp+"[field]=collection_total_employees&"+tmp+\
            "[operator]==&"+tmp+"[value]="+total_employees+"&"
            count4=count3+1
            tmp="_fil["+str(count4)+"]"
            condition_url3=tmp+"[field]=phys_country_code&"+tmp+"[operator]==&"\
            +tmp+"[optional]=false&"+tmp+"[value]=805"
            suffix_condition=condition_url+condition_url2+condition_url3

            entire_condition=prefix_condition+suffix_condition+suffix_url
            yield entire_condition.encode("utf-8")
            # for employees_here in collection_employees_here:
            #     count4=count3+1
            #     tmp="_fil["+str(count4)+"]"
            #     condition_url3=tmp+"[field]=collection_employees_here&"+tmp+\
            #     "[operator]==&"+tmp+"[value]="+employees_here+"&"
            #     for st_id in status_id:
            #         count5=count4+1
            #         tmp="_fil["+str(count5)+"]"
            #         condition_url4=tmp+"[field]=status_id&"+tmp+\
            #         "[operator]==&"+tmp+"[value]="+st_id+"&"
            #         for pp_id in pub_pri_id:
            #             count6=count5+1
            #             tmp="_fil["+str(count6)+"]"
            #             condition_url5=tmp+"[field]=pub_pri_id&"+tmp+\
            #             "[operator]==&"+tmp+"[optional]=false&"+tmp+"[value]="+pp_id+"&"

                        # combine phys_country_code
                        # count7=count6+1   #use
                        # tmp="_fil["+str(count7)+"]"
                        # condition_url6=tmp+"[field]=phys_country_code&"+tmp+"[operator]==&"\
                        # +tmp+"[optional]=false&"+tmp+"[value]=805"
                        # suffix_condition=condition_url+condition_url2+condition_url3\
                        # +condition_url4+condition_url5+condition_url6
                        #
                        # entire_condition=prefix_condition+suffix_condition+suffix_url
                        # yield entire_condition.encode("utf-8")

def combineCondition():
    for sic_all_divisions in sorted(rawdata.keys()):
        condition_url=""
        count=0
        tmp="_fil["+str(count)+"]"
        condition_url+=tmp+"[field]=sic_all_divisions&"+tmp+"[operator]==&"+tmp\
        +"[value]="+sic_all_divisions+"&"
        if len(rawdata[sic_all_divisions])!=0:
            for sic_all_2digit in sorted(rawdata[sic_all_divisions].keys()):
                count=1
                tmp="_fil["+str(count)+"]"
                condition_url2=tmp+"[field]=sic_all_2digit&"+tmp+"[operator]==&"\
                +tmp+"[value]="+sic_all_2digit+"&"
                if len(rawdata[sic_all_divisions][sic_all_2digit])!=0:
                    for sic_all_4digit in rawdata[sic_all_divisions][sic_all_2digit]:
                        count=2
                        tmp="_fil["+str(count)+"]"
                        condition_url3=tmp+"[field]=sic_all_4digit&"+tmp+\
                        "[operator]==&"+tmp+"[value]="+sic_all_2digit+sic_all_4digit+"&"

                        prefix_condition=condition_url+condition_url2+condition_url3
                        yield combineSuffixCondition(count,prefix_condition)
                else:
                    prefix_condition=condition_url+condition_url2
                    yield combineSuffixCondition(count,prefix_condition)

        else:
            prefix_condition=condition_url
            yield combineSuffixCondition(count,prefix_condition)
def storeConditionParameter():
    file=open("condition_parameter.txt","w")
    condition_list=list(combineCondition())
    print "the condition list is :",len(condition_list)
    print condition_list[0]
    index=0
    for x in condition_list:
        for y in list(x):
            file.write(y+"\n")


if __name__=="__main__":
    storeConditionParameter()
