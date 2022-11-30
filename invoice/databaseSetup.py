import mysql.connector as db
import tbl
f = open('config.txt', 'r')
setup = f.read().split(',')
userName = setup[0]
pas = setup[1]
db_name = setup[2]

def checkTables():
    con = db.connect(host='localhost',user=userName,password=pas, database=db_name)
    cur = con.cursor()
    sql = "show tables"
    cur.execute(sql)
    res = cur.fetchall()
    li = ['admin', 'users', 'products', 'orders']
    lis = [False, False, False, False]
    for i in res:
        for j in i:
            ind = 0
            for k in li:
                if(j == k):
                    lis[ind] = True
                    break
                ind = ind + 1
    for i in range(len(lis)):
        if(lis[i] == False):
            if(li[i] == 'admin'):
                tbl.createAdminTbl(cur)
                sql = "Insert into admin(id, name, pass) values(1, 'admin', 'pas')"
                cur.execute(sql)
                con.commit()
            elif(li[i] == 'users'):
                tbl.createUserTbl(cur)
            elif(li[i] == 'products'):
                tbl.createProductTable(cur)
            elif(li[i] == 'orders'):
                tbl.createOrder(cur)

def checkDatabase():
    con = db.connect(host='localhost',user=userName,password=pas)
    cur = con.cursor()
    sql = "show databases"
    cur.execute(sql)
    res = cur.fetchall()
    doexist = False
    for i in res:
        if(doexist == False):
            for j in i:
                if j == db_name:
                    doexist = True
                    break
        else:
            break
    if(doexist == False):
        sql = 'create database {}'.format(db_name)
        cur.execute(sql)
    checkTables()

checkDatabase()
