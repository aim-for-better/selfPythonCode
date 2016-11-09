# -*- coding:utf-8 -*-
import json
import pymysql


def get_inventor(db_connection,patent_id):

    """
    if you want get the inventor ,you first need get the patent_id from table patent
    then, go to table patent_inventor find the inventor_id by patent_id,
    finally go to table inventor find the inventor by inventor_id
    """

    # query patent_inventor
    inventor_array=[]
    query_inventor_id="SELECT inventor_id FROM patent_inventor \
    WHERE patent_inventor.patent_id=%s"
    patent_inventor_cur=db_connection.cursor()
    patent_inventor_cur.execute(query_inventor_id,patent_id)
    # cur.execute(query_inventor_id,patent_id)
    patent_inventor=patent_inventor_cur.fetchone()
    while patent_inventor:
        inventor_id=patent_inventor[0]

        # query inventor
        query_inventor="SELECT * FROM inventor WHERE inventor.id=%s"
        inventor_cur=db_connection.cursor()
        inventor_cur.execute(query_inventor,inventor_id)
        inventor=inventor_cur.fetchone()
        location_inventor_cur.close()
        if inventor:
            tmp_inventor={} # as a temp value store a inventor
            tmp_inventor["name_first"]=inventor[1]
            tmp_inventor["name_last"]=inventor[2]
            query_location_inventor="SELECT location_id FROM location_inventor WHERE inventor_id=%s"
            location_inventor_cur=db_connection.cursor()
            location_inventor_cur.execute(query_location_inventor,inventor[0])
            location_inventor=location_inventor_cur.fetchone()
            location_inventor_cur.close()
            tmp_location={}
            if  location_inventor:
                query_location="SELECT * FROM location WHERE id=%s limit 1;"
                location_cur=db_connection.cursor()
                location_cur.execute(query_location,location_inventor[0])
                location=location_cur.fetchone()
                if location:
                    loc={}
                    loc["lat"]=location[4]
                    loc["lon"]=location[5]
                    tmp_location["city"]=location[1]
                    tmp_location["state"]=location[2]
                    tmp_location["country"]=location[3]
                    tmp_location["loc"]=loc
                location_cur.close()
            tmp_inventor["location"]=tmp_location
            inventor_array.append(tmp_inventor)
        patent_inventor=patent_inventor_cur.fetchone()
    patent_inventor_cur.close()
    return inventor_array


def get_assignee(db_connection,patent_id):

    """
    if you want get the assignee ,you first need get the patent_id from table patent
    then, go to table patent_assignee find the assignee_id by patent_id,
    finally go to table assignee find the assignee by assignee_id
    :param db_connection:
    :param patent_id:
    :return:
    """
    assignee_array=[] #store assignee
    query_patent_assignee="SELECT assignee_id FROM patent_assignee WHERE \
patent_assignee.patent_id=%s"
    patent_assignee_cur=db_connection.cursor()
    patent_assignee_cur.execute(query_patent_assignee,patent_id)
    patent_assignee=patent_assignee_cur.fetchone()
    while patent_assignee:
        query_assignee="SELECT * FROM assignee WHERE assignee.id=%s"
        assignee_cur=db_connection.cursor()
        assignee_cur.execute(query_assignee,patent_assignee[0])
        assignee=assignee_cur.fetchone()

        assignee_cur.close()

        if assignee:
            tmp_assignee = {}
            tmp_assignee["type"]=assignee[1]
            tmp_assignee["name_first"]=assignee[2]
            tmp_assignee["name_last"]=assignee[3]
            tmp_assignee["organization"]=assignee[4]
            query_location_assignee = "SELECT location_id FROM location_assignee WHERE assignee_id=%s"
            location_assignee_cur = db_connection.cursor()
            location_assignee_cur.execute(query_location_assignee, assignee[0])
            location_assignee = location_assignee_cur.fetchone()
            location_assignee_cur.close()
            tmp_location = {}
            if location_assignee:
                query_location = "SELECT * FROM location WHERE id=%s limit 1;"
                location_cur = db_connection.cursor()
                location_cur.execute(query_location, location_assignee[0])
                location = location_cur.fetchone()
                if location:
                    loc = {}
                    loc["lat"] = location[4]
                    loc["lon"] = location[5]
                    tmp_location["city"] = location[1]
                    tmp_location["state"] = location[2]
                    tmp_location["country"] = location[3]
                    tmp_location["loc"] = loc
                location_cur.close()
            tmp_assignee["location"] = tmp_location
            assignee_array.append(tmp_assignee)
        patent_assignee=patent_assignee_cur.fetchone()
    patent_assignee_cur.close()
    return assignee_array


def get_lawyer(db_connection,patent_id):
    """
     if you want get the lawyer ,you first need get the patent_id from table patent
    then, go to table patent_lawyer find the lawyer_id by patent_id,
    finally go to table lawyer find the lawyer by lawyer_id
    :param db_connection:
    :param patent_id:
    :return:
    """
    lawyer_array=[]
    query_patent_lawyer="SELECT lawyer_id FROM patent_lawyer WHERE\
     patent_lawyer.patent_id=%s"
    patent_lawyer_cur=db_connection.cursor()
    patent_lawyer_cur.execute(query_patent_lawyer,patent_id)
    patent_lawyer=patent_lawyer_cur.fetchone()
    while  patent_lawyer:
        query_lawyer="SELECT * FROM lawyer WHERE lawyer.id=%s"
        lawyer_cur=db_connection.cursor()
        lawyer_cur.execute(query_lawyer,patent_lawyer[0])
        lawyer=lawyer_cur.fetchone()

        lawyer_cur.close()
        if lawyer:
            tmp_lawyer={}
            tmp_lawyer["name_first"]=lawyer[1]
            tmp_lawyer["name_last"]=lawyer[2]
            tmp_lawyer["organization"]=lawyer[3]
            tmp_lawyer["country"]=lawyer[4]
            lawyer_array.append(tmp_lawyer)
        patent_lawyer=patent_lawyer_cur.fetchone()

    patent_lawyer_cur.close()
    return lawyer_array


def get_application(db_connection,patent_id):

    application={}
    query_application="SELECT * FROM application WHERE application.patent_id=%s"
    application_cur=db_connection.cursor()
    application_cur.execute(query_application,patent_id)
    tmp_application=application_cur.fetchone()

    if tmp_application:
        application["series_code"]=tmp_application[2]
        application["number"]=tmp_application[3]
        application["country"]=tmp_application[4]
        application["date"]=tmp_application[5]
    application_cur.close()
    return  application


def  get_usapplicationcitation(db_connection,patent_id):

    usapplicationcitation_array = []
    query_usapplicationcitation="SELECT * FROM usapplicationcitation WHERE \
    usapplicationcitation.patent_id=%s"
    usapplicationcitation_cur=db_connection.cursor()
    usapplicationcitation_cur.execute(query_usapplicationcitation,patent_id)

    usapplicationcitation=usapplicationcitation_cur.fetchone()

    while usapplicationcitation:
        tmp_usapplicationcitation={}
        tmp_usapplicationcitation["application_id"] = usapplicationcitation[2]
        tmp_usapplicationcitation['date'] = usapplicationcitation[3]
        tmp_usapplicationcitation['name'] =usapplicationcitation[4]
        tmp_usapplicationcitation['kind'] =usapplicationcitation[5]
        tmp_usapplicationcitation['number'] = usapplicationcitation[6]
        tmp_usapplicationcitation['country'] = usapplicationcitation[7]
        tmp_usapplicationcitation['category'] =usapplicationcitation[8]
        tmp_usapplicationcitation['sequence'] = usapplicationcitation[9]

        usapplicationcitation_array.append(tmp_usapplicationcitation)

        usapplicationcitation=usapplicationcitation_cur.fetchone()

    usapplicationcitation_cur.close()

    return usapplicationcitation_array


def get_uspatentcitation(db_connection,patent_id):

    uspatentcitation_array=[]
    query_uspantentcitation="SELECT * FROM uspatentcitation WHERE \
    uspantentcitation.patent_id=%s"

    uspatentcitation_cur=db_connection.cursor()

    uspatentcitation_cur.execute(query_uspantentcitation,patent_id)

    uspatentcitation=uspatentcitation_cur.fetchone()

    while uspatentcitation:
        tmp_uspatentcitation={}
        tmp_uspatentcitation['citation_id'] = uspatentcitation[2]
        tmp_uspatentcitation['date'] = uspatentcitation[3]
        tmp_uspatentcitation['name'] = uspatentcitation[4]
        tmp_uspatentcitation['kind'] = uspatentcitation[5]
        tmp_uspatentcitation['country'] = uspatentcitation[6]
        tmp_uspatentcitation['category'] = uspatentcitation[7]
        tmp_uspatentcitation['sequence'] = uspatentcitation[8]

        uspatentcitation_array.append(tmp_uspatentcitation)

        uspatentcitation=uspatentcitation_cur.fetchone()

    uspatentcitation_cur.close()
    return uspatentcitation_array


def get_otherreference(db_connection,patent_id):
    otherreference_array=[]

    query_otherreference="SELECT * FROM otherreference WHERE \
    otherreference.patent_id=%s"

    otherreference_cur=db_connection.cursor()

    otherreference_cur.execute(query_otherreference,patent_id)

    otherreference=otherreference_cur.fetchone()

    while otherreference:
        tmp_otherreference={}
        tmp_otherreference['text'] = otherreference[2]
        tmp_otherreference['sequence'] = otherreference[3]

        otherreference_array.append(tmp_otherreference)
        otherreference=otherreference_cur.fetchone()

    otherreference_cur.close()

    return otherreference_array


def get_usreldoc(db_connection,patent_id):

    usreldoc_array=[]
    query_usreldoc="SELECT * FROM usreldoc WHERE usreldoc.patent_id=%s"
    usreldoc_cur=db_connection.cursor()
    usreldoc_cur.execute(query_usreldoc,patent_id)
    usreldoc=usreldoc_cur.fetchone()
    while usreldoc:
        tmp_usreldoc={}
        tmp_usreldoc['rel_id'] = usreldoc[2]
        tmp_usreldoc['doctype'] = usreldoc[3]
        tmp_usreldoc['status'] = usreldoc[4]
        tmp_usreldoc['date'] = usreldoc[5]
        tmp_usreldoc['number'] = usreldoc[6]
        tmp_usreldoc['kind'] = usreldoc[7]
        tmp_usreldoc['country'] = usreldoc[8]
        tmp_usreldoc['relationship'] = usreldoc[9]
        tmp_usreldoc['sequence'] = usreldoc[10]

        usreldoc_array.append(tmp_usreldoc)

        usreldoc=usreldoc_cur.fetchone()

    usreldoc_cur.close()

    return usreldoc_array


def get_ipcr(db_connection,patent_id):
    ipcr_array = []
    query_ipcr = "SELECT * FROM ipcr WHERE ipcr.patent_id=%s"
    ipcr_cur=db_connection.cursor()
    ipcr_cur.execute(query_ipcr,patent_id)
    ipcr = ipcr_cur.fetchone()
    while ipcr:
        tmp_ipcr = {}
        tmp_ipcr['classification_level'] = ipcr[2]
        tmp_ipcr['section'] = ipcr[3]
        tmp_ipcr['ipc_class'] = ipcr[4]
        tmp_ipcr['subclass'] = ipcr[5]
        tmp_ipcr['main_group'] = ipcr[6]
        tmp_ipcr['subgroup'] = ipcr[7]
        tmp_ipcr['symbol_position'] = ipcr[8]
        tmp_ipcr['classification_value'] = ipcr[9]
        tmp_ipcr['classification_status'] = ipcr[10]
        tmp_ipcr['classification_data_source'] = ipcr[11]
        tmp_ipcr['action_date'] = ipcr[12]
        tmp_ipcr['ipc_version_indicator'] = ipcr[13]
        tmp_ipcr['sequence'] = ipcr[14]
        ipcr_array.append(tmp_ipcr)
        ipcr = ipcr_cur.fetchone()
    ipcr_cur.close()
    return ipcr_array


def get_uspc(db_connection,patent_id):
    uspc_array=[]
    query_uspc="SELECT * FROM uspc_current WHERE uspc_current.patent_id=%s"
    uspc_cur=db_connection.cursor()

    uspc_cur.execute(query_uspc,patent_id)
    uspc=uspc_cur.fetchone()
    while uspc:
        tmp_uspc={}

        query_mainclass_current="SELECT * FROM mainclass_current WHERE id=%"
        mainclass_current_cur=db_connection.cursor()
        mainclass_current_cur.execute(query_mainclass_current,uspc[2])
        mainclass_current=mainclass_current_cur.fetchone()

        tmp_mainclass_current={}
        if mainclass_current:
            tmp_mainclass_current["title"]=mainclass_current[1]
        tmp_uspc["mainclass"]=tmp_mainclass_current
        mainclass_current_cur.close()

        query_subclass_current = "SELECT * FROM subclass_current WHERE id=%"
        subclass_current_cur = db_connection.cursor()
        subclass_current_cur.execute(query_subclass_current, uspc[3])
        subclass_current = subclass_current_cur.fetchone()

        tmp_subclass_current = {}
        if subclass_current:
            tmp_subclass_current["title"] = subclass_current[1]
        tmp_uspc["subclass"] = tmp_subclass_current
        subclass_current_cur.close()
        uspc_array.append(tmp_uspc)
        uspc=uspc_cur.fetchone()
    uspc_cur.close()
    return uspc_array


def get_nber(db_connection,patent_id):

    nber_array=[]
    query_nber="SELECT * FROM nber WHERE nber.patent_id=%s"

    nber_cur=db_connection.cursor()
    nber_cur.execute(query_nber,patent_id)
    nber=nber_cur.fetchone()

    while nber:
        tmp_nber={}

        query_nber_category="SELECT * FROM nber_category WHERE id=%s"
        nber_category_cur=db_connection.cursor()
        nber_category_cur.execute(query_nber_category,nber[2])

        nber_category=nber_category_cur.fetchone()

        tmp_category={}
        if nber_category:
            tmp_category["title"]=nber_category[1]
        tmp_nber["category"]=tmp_category
        nber_category_cur.close()

        query_nber_category = "SELECT * FROM nber_category WHERE id=%s"
        nber_category_cur = db_connection.cursor()
        nber_category_cur.execute(query_nber_category, nber[2])

        nber_category = nber_category_cur.fetchone()

        tmp_category = {}
        if nber_category:
            tmp_category["title"] = nber_category[1]
        tmp_nber["category"] = tmp_category
        nber_category_cur.close()

        query_nber_subcategory = "SELECT * FROM nber_subcategory WHERE id=%s"
        nber_subcategory_cur = db_connection.cursor()
        nber_subcategory_cur.execute(query_nber_subcategory, nber[3])

        nber_subcategory = nber_subcategory_cur.fetchone()

        tmp_subcategory = {}
        if nber_subcategory:
            tmp_subcategory["title"] = nber_subcategory[1]
        tmp_nber["subcategory"] = tmp_subcategory
        nber_subcategory_cur.close()
        nber_array.append(tmp_nber)

        nber=nber_cur.fetchone()
    nber_cur.close()

    return  nber_array


def get_cpc(db_connection,patent_id):

    cpc_array=[]
    query_cpc="SELECT * FROM cpc_current WHERE cpc_current.patent_id=%s"

    cpc_cur=db_connection.cursor()
    cpc_cur.execute(query_cpc,patent_id)
    cpc=cpc_cur.fetchone()
    while cpc:
        tmp_cpc={}
        tmp_cpc['section_id'] = cpc[2]
        tmp_cpc['category'] = cpc[6]
        tmp_cpc['sequence'] = cpc[7]
        # get subsection
        query_subsection="SELECT * FROM cpc_subsection WHERE id=%s"
        subsection_cur=db_connection.cursor()
        subsection_cur.execute(query_subsection,cpc[3])
        subsection=subsection_cur.fetchone()

        tmp_subsection={}
        if subsection:
            tmp_subsection["title"]=subsection[1]
        tmp_cpc["subsection"]=tmp_subsection
        subsection_cur.close()

        query_groub = "SELECT * FROM cpc_groub WHERE id=%s"
        groub_cur = db_connection.cursor()
        groub_cur.execute(query_groub, cpc[4])
        groub = groub_cur.fetchone()

        tmp_groub = {}
        if groub:
            tmp_groub["title"] = groub[1]
        tmp_cpc["groub"] = tmp_groub
        groub_cur.close()
        # get subgroup
        query_subgroub = "SELECT * FROM cpc_subgroub WHERE id=%s"
        subgroub_cur = db_connection.cursor()
        subgroub_cur.execute(query_subgroub, cpc[5])
        subgroub = subgroub_cur.fetchone()

        tmp_subgroub = {}
        if subgroub:
            tmp_subgroub["title"] = subgroub[1]
        tmp_cpc["subgroub"] = tmp_subgroub
        subgroub_cur.close()
        cpc_array.append(tmp_cpc)
        cpc=cpc_cur.fetchone()
    cpc_cur.close()

    return cpc_array

if __name__ == '__main__':
    conn = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='', db='patent2', charset='utf8')
    conn1 = pymysql.Connect(host='127.0.0.1', port=3306, user='root', passwd='', db='patent2', charset='utf8')

    try:
        f = open('patent.json', 'w')
        curs = conn1.cursor()
        sql = 'select * from patent limit 4800000,300000'
        # sql = 'select * from patent limit 5'
        # sql = 'select * from patent WHERE id="7876855"' #测试usapplicationcitation
        # sql = 'select * from patent WHERE id="3930281"' #测试inventor？
        curs.execute(sql)
        result = curs.fetchone()
        des = curs.description
        count =0
        while result:
            d = {}
            count=count+1
            print count
            for i in range(0, len(des)):
                d[des[i][0]] = result[i]
            inventor = getInventor(d['id'])
            d['inventor'] = inventor
            assignee = getAssignee(d['id'])
            d['assignee'] = assignee
            lawyer = getLawer(d['id'])
            d['lawyer'] = lawyer
            application = getApplication(d['id'])
            d['application'] = application
            foreigncitation = getForeigncitation(d['id'])
            d['foreigncitation'] = foreigncitation
            usapplicationcitation = getUsapplicationcitation(d['id'])
            d['usapplicationcitation'] = usapplicationcitation
            uspatentcitation = getUspatentcitation(d['id'])
            d['uspatentcitation'] = uspatentcitation
            otherreference = getOtherreference(d['id'])
            d['otherreference'] = otherreference
            usreldoc = getUsreldoc(d['id'])
            d['usreldoc'] = usreldoc
            ipcr = getIpcr(d['id'])
            d['ipcr'] = ipcr
            uspc = getUspc(d['id'])
            d['uspc'] = uspc
            nber = getNber(d['id'])
            d['nber'] = nber
            cpc = getCpc(d['id'])
            d['cpc'] = cpc
            # j = json.dumps(d, cls=MyEncoder)
            j = json.dumps(d, default=json_serial)
            index = {'index':{}}
            index = json.dumps(index)
            f.write(index+'\n')
            f.write(j+'\n')
            # print d['assignee']
            result = curs.fetchone()
        curs.close()
        f.close()
    # except Exception, e:
    #     print e
    finally:
        conn.close()
