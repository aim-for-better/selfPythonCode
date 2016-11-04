# -*- coding:utf-8 -*-
import json
import pymysql







def getInventor(db_connection,patent_id):
    """
    if you want get the inventor ,you first need get the patent_id from table patent
    then, go to table patent_inventor find the inventor_id by patent_id,
    finally go to table inventor find the inventor by inventor_id
    """

    # query patent_inventor
    query_inventor_id="SELECT inventor_id FROM patent_inventor \
    WHERE patent_inventor.patent_id=%s"
    patent_inventor_cur=db_connection.cursor
    patent_inventor_cur.execute(query_inventor_id,patent_id)
    # cur.execute(query_inventor_id,patent_id)
    patent_inventor=cur.fetchone()
    if patent_inventor:
        inventor_id=patent_inventor[0]

        # query inventor
        query_inventor="SELECT * FROM inventor WHERE inventor.id=%s"
        inventor_cur.execute(query_inventor,inventor_id)
        inventor=inventor_cur.fetchone()
        if inventor:
            location_id=inventor[0]


def getInventor(patentId):
    inventor = []  # 保存inventor
    sql1 = 'SELECT inventor_id FROM patent_inventor WHERE patent_inventor.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        sql2 = 'SELECT * FROM inventor WHERE inventor.id="' + result1[0] + '"'
        curs2 = conn.cursor()
        curs2.execute(sql2)
        result2 = curs2.fetchone()
        if result2:
            i = {}  # 保存inventor属性的字典
            i['name_first'] = result2[1]
            i['name_last'] = result2[2]
            sql3 = 'SELECT location_id FROM location_inventor WHERE inventor_id="' + result2[0] + '"'
            curs3 = conn.cursor()
            curs3.execute(sql3)
            result3 = curs3.fetchone()
            curs3.close()
            location = {}
            if result3:
                sql4 = 'SELECT * FROM r_location2 WHERE location_id="' + result3[0] + '" limit 1'
                curs4 = conn.cursor()
                curs4.execute(sql4)
                result4 = curs4.fetchone()
                if result4:
                    loc = {}
                    loc['lat'] = result4[5]
                    loc['lon'] = result4[6]
                    location['city'] = result4[2]
                    location['state'] = result4[3]
                    location['country'] = result4[4]
                    location['loc'] = loc
                curs4.close()
            i['location'] = location
            inventor.append(i)
        curs2.close()
        result1 = curs1.fetchone()
    curs1.close()
    return inventor


def getAssignee(patentId):
    assignee = []
    sql1 = 'SELECT assignee_id FROM patent_assignee WHERE patent_assignee.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        a = {}
        sql2 = 'SELECT * FROM assignee WHERE assignee.id="' + result1[0] + '"'
        curs2 = conn.cursor()
        curs2.execute(sql2)
        result2 = curs2.fetchone()
        curs2.close()
        if result2:
            a['type'] = result2[1]
            a['name_first'] = result2[2]
            a['name_last'] = result2[3]
            a['organization'] = result2[4]
            sql3 = 'SELECT location_id FROM location_assignee WHERE assignee_id="' + result2[0] + '"'
            curs3 = conn.cursor()
            curs3.execute(sql3)
            result3 = curs3.fetchone()
            curs3.close()
            location = {}
            if result3:
                sql4 = 'SELECT * FROM r_location2 WHERE location_id="' + result3[0] + '" limit 1'
                curs4 = conn.cursor()
                curs4.execute(sql4)
                result4 = curs4.fetchone()
                if result4:
                    loc = {}
                    loc['lat'] = result4[5]
                    loc['lon'] = result4[6]
                    location['city'] = result4[2]
                    location['state'] = result4[3]
                    location['country'] = result4[4]
                    location['loc'] = loc
                curs4.close()
            a['location'] = location
        assignee.append(a)
        result1 = curs1.fetchone()
    curs1.close()
    return assignee


def getLawer(patentId):
    lawyer = []
    sql1 = 'SELECT lawyer_id FROM patent_lawyer WHERE patent_lawyer.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        l = {}
        sql2 = 'SELECT * FROM lawyer WHERE lawyer.id="' + result1[0] + '"'
        curs2 = conn.cursor()
        curs2.execute(sql2)
        result2 = curs2.fetchone()
        curs2.close()
        if result2:
            l['name_first'] = result2[1]
            l['name_last'] = result2[2]
            l['organization'] = result2[3]
            l['country'] = result2[4]
        lawyer.append(l)
        result1 = curs1.fetchone()
    curs1.close()
    return lawyer


def getApplication(patentId):
    application = {}
    sql1 = 'SELECT * FROM application WHERE application.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    if result1:
        a = {}
        a['series_code'] = result1[2]
        a['number'] = result1[3]
        a['country'] = result1[4]
        a['date'] = result1[5]
        application = a
    curs1.close()
    return application


def getForeigncitation(patentId):
    foreigncitation = []
    sql1 = 'SELECT * FROM foreigncitation WHERE foreigncitation.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        f = {}
        f['date'] = result1[2]
        f['number'] = result1[3]
        f['country'] = result1[4]
        f['category'] = result1[5]
        f['sequence'] = result1[6]
        foreigncitation.append(f)
        result1 = curs1.fetchone()
    curs1.close()
    return foreigncitation


def getUsapplicationcitation(patentId):
    usapplicationcitation = []
    sql1 = 'SELECT * FROM usapplicationcitation WHERE usapplicationcitation.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        u = {}
        u['application_id'] = result1[2]
        u['date'] = result1[3]
        u['name'] = result1[4]
        u['kind'] = result1[5]
        u['number'] = result1[6]
        u['country'] = result1[7]
        u['category'] = result1[8]
        u['sequence'] = result1[9]
        usapplicationcitation.append(u)
        result1 = curs1.fetchone()
    curs1.close()
    return usapplicationcitation


def getUspatentcitation(patentId):
    uspatentcitation = []
    sql1 = 'SELECT * FROM uspatentcitation WHERE uspatentcitation.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        u = {}
        u['citation_id'] = result1[2]
        u['date'] = result1[3]
        u['name'] = result1[4]
        u['kind'] = result1[5]
        u['country'] = result1[6]
        u['category'] = result1[7]
        u['sequence'] = result1[8]
        uspatentcitation.append(u)
        result1 = curs1.fetchone()
    curs1.close()
    return uspatentcitation


def getOtherreference(patentId):
    otherreference = []
    sql1 = 'SELECT * FROM otherreference WHERE otherreference.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        o = {}
        o['text'] = result1[2]
        o['sequence'] = result1[3]
        otherreference.append(o)
        result1 = curs1.fetchone()
    curs1.close()
    return otherreference


def getUsreldoc(patentId):
    usreldoc = []
    sql1 = 'SELECT * FROM usreldoc WHERE usreldoc.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        u = {}
        u['rel_id'] = result1[2]
        u['doctype'] = result1[3]
        u['status'] = result1[4]
        u['date'] = result1[5]
        u['number'] = result1[6]
        u['kind'] = result1[7]
        u['country'] = result1[8]
        u['relationship'] = result1[9]
        u['sequence'] = result1[10]
        usreldoc.append(u)
        result1 = curs1.fetchone()
    curs1.close()
    return usreldoc


def getIpcr(patentId):
    ipcr = []
    sql1 = 'SELECT * FROM ipcr WHERE ipcr.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        i = {}
        i['classification_level'] = result1[2]
        i['section'] = result1[3]
        i['ipc_class'] = result1[4]
        i['subclass'] = result1[5]
        i['main_group'] = result1[6]
        i['subgroup'] = result1[7]
        i['symbol_position'] = result1[8]
        i['classification_value'] = result1[9]
        i['classification_status'] = result1[10]
        i['classification_data_source'] = result1[11]
        i['action_date'] = result1[12]
        i['ipc_version_indicator'] = result1[13]
        i['sequence'] = result1[14]
        ipcr.append(i)
        result1 = curs1.fetchone()
    curs1.close()
    return ipcr


def getUspc(patentId):
    uspc = []
    sql1 = 'SELECT * FROM uspc_current WHERE uspc_current.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        u = {}
        u['sequence'] = result1[3]
        # 得到mainclass
        sql2 = 'SELECT * FROM mainclass_current WHERE id="' + result1[2] + '"'
        curs2 = conn.cursor()
        curs2.execute(sql2)
        result2 = curs2.fetchone()
        mainclass = {}
        if result2:
            mainclass['title'] = result2[1]
        u['mainclass'] = mainclass
        curs2.close()
        #得到subclass
        sql3 = 'SELECT * FROM subclass_current WHERE id="' + result1[3] + '"'
        curs3 = conn.cursor()
        curs3.execute(sql3)
        result3 = curs3.fetchone()
        subclass = {}
        if result3:
            subclass['title'] = result3[1]
        u['subclass'] = subclass
        curs3.close()
        uspc.append(u)
        result1 = curs1.fetchone()
    curs1.close()
    return uspc


def getNber(patentId):
    nber = []
    sql1 = 'SELECT * FROM nber WHERE nber.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        n = {}
        # 得到category
        sql2 = 'SELECT * FROM nber_category WHERE id="' + result1[2] + '"'
        curs2 = conn.cursor()
        curs2.execute(sql2)
        result2 = curs2.fetchone()
        category = {}
        if result2:
            category['title'] = result2[1]
        n['category'] = category
        curs2.close()
        #得到subcategory
        sql3 = 'SELECT * FROM nber_subcategory WHERE id="' + result1[3] + '"'
        curs3 = conn.cursor()
        curs3.execute(sql3)
        result3 = curs3.fetchone()
        subcategory = {}
        if result3:
            subcategory['title'] = result3[1]
        n['subcategory'] = subcategory
        curs3.close()
        nber.append(n)
        result1 = curs1.fetchone()
    curs1.close()
    return nber


def getCpc(patentId):
    cpc = []
    sql1 = 'SELECT * FROM cpc_current WHERE cpc_current.patent_id="' + patentId + '"'
    curs1 = conn.cursor()
    curs1.execute(sql1)
    result1 = curs1.fetchone()
    while result1:
        c = {}
        c['section_id'] = result1[2]
        c['category'] = result1[6]
        c['sequence'] = result1[7]
        # 得到subsection
        sql2 = 'SELECT * FROM cpc_subsection WHERE id="' + result1[3] + '"'
        curs2 = conn.cursor()
        curs2.execute(sql2)
        result2 = curs2.fetchone()
        subsection = {}
        if result2:
            subsection['title'] = result2[1]
        c['subsection'] = subsection
        curs2.close()
        #得到group
        sql3 = 'SELECT * FROM cpc_group WHERE id="' + result1[4] + '"'
        curs3 = conn.cursor()
        curs3.execute(sql3)
        result3 = curs3.fetchone()
        group = {}
        if result3:
            group['title'] = result3[1]
        c['group'] = group
        curs3.close()
        # 得到subgroup
        sql4 = 'SELECT * FROM cpc_subgroup WHERE id="' + result1[5] + '"'
        curs4 = conn.cursor()
        curs4.execute(sql4)
        result4 = curs4.fetchone()
        subgroup = {}
        if result4:
            subgroup['title'] = result4[1]
        c['subgroup'] = subgroup
        curs3.close()
        cpc.append(c)
        result1 = curs1.fetchone()
    curs1.close()
    return cpc


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
