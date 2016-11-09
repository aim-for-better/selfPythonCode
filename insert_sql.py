# -*-coding:utf-8-*-
import pymysql

class InsertPatentsData():

    def connect(self,):

        host="localhost"
        user="root"
        passwd=""
        port=3306
        db="patentsviewdata"
        try:
            conn=pymysql.Connect(host=host,user=user,passwd=passwd,port=port,db=db)

            cur=None
            if conn:
                cur=conn.cursor()
            # print "connection database success"
            #
            # cur.execute("select * from application limit 5;")
            # result=cur.fetchone()
            # while result:
            #     print result
            #     print type(result)
            #     result=cur.fetchone()
        except Exception,e:
            print ("Connection mysql database error! The error is %s",e)

        return conn

    def  insert_file_into_db(self,file_name=""):
        assert file_name!="","file_name should be a file name including path,and can not be None"
        table_name=file_name.split("/")[-1].split(".")[0]

        file=open(file_name,"r")

        conn=self.connect()
        cur=conn.cursor()
        batch_num=100000
        i=0
        line_data=[]
        title=file.next()
        tp=tuple(title.split("\t"))
        table_param="("+("%s,"*len(tp))[0:-1]+")"  # generate a string like (%s,%s,%s) the number of %s is unknown

        sql_str="insert into "+table_name+" values "+table_param

        print sql_str
        flag=True
        for line in file:
            item=tuple(str(line).rstrip("\n").split("\t"))

            if flag:
                print item
                flag=False
            #
            i+=1
            line_data.append(item)
            if(i==batch_num):
                try:
                    conn.begin()
                    cur.executemany(sql_str,line_data)
                    conn.commit()

                except Exception,e:
                    conn.rollback()
                    print e
                line_data = []
                i = 0
        try:
            conn.begin()
            cur.executemany(sql_str, line_data)
            conn.commit()

        except e:
            conn.rollback()
            print e

        cur.close()
        conn.close()
if __name__=="__main__":
    insert_tool=InsertPatentsData()

    file_name="D:/patentsviewdata/tsvfile/cpc_current.tsv"  # give a file name
    insert_tool.insert_file_into_db(file_name=file_name)
