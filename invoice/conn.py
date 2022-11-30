import mysql.connector as db
import tbl
import json
con = db.connect(host='localhost',user='root',password='', database='shop')
cur = con.cursor()

def NewId(tb):
    sql = "Select max(id) from {}".format(tb)
    cur.execute(sql)
    res = cur.fetchone()
    if(res[0] == None):
        return 1
    else:
        return int(res[0]) + 1



def newUser(ud):
    uId = NewId('users')
    sql = "Insert into users(id, name, email, pass, bal) values({}, '{}', '{}', '{}', 25)".format(uId, ud[0], ud[1], ud[2])
    cur.execute(sql)
    con.commit()
    return True

def checkLogin(data):
    sql = "Select * from users where email='{}' and pass='{}'".format(data[0], data[1])
    cur.execute(sql)
    res = cur.fetchone()
    if(cur.rowcount == 1):
        return res
    else:
        return False

def checkAdminLogin(data):
    sql = "Select * from admin where name='{}' and pass='{}'".format(data[0], data[1])
    cur.execute(sql)
    res = cur.fetchone()
    if(cur.rowcount == 1):
        return res
    else:
        return False

def fetchAllUsers():
    sql = "select id,name,email,bal from users"
    cur.execute(sql)
    res = cur.fetchall()
    if(cur.rowcount == 0):
        return False
    else:
        return res

def fetchUserProfile(ids):
    sql = "select id,name,email,bal from users where id = {}".format(ids)
    cur.execute(sql)
    res = cur.fetchone()
    if(cur.rowcount == 0):
        return False
    else:
        return res

def newPrduct(data):
    sql = "insert into products values({}, '{}', {}, {}, {})".format(NewId('products'), data[0], data[1], data[2], data[3])
    cur.execute(sql)
    con.commit()
    return True

def fetchAllProducts(user = False):
    if(user):
        sql = "select id,name,mrp,s_price from products"
    else:
        sql = "select * from products"
    cur.execute(sql)
    res = cur.fetchall()
    if(cur.rowcount == 0):
        return False
    else:
        return res

def checkIfProductExists(ids, allFields = False):
    if(allFields):
        sql = "select * from products where id = {}".format(ids)
        cur.execute(sql)
        res = cur.fetchmany()

    else:
        sql = "select name from products where id = {}".format(ids)
        cur.execute(sql)
        res = cur.fetchone()
    if(cur.rowcount != 1):
        return False
    else:
        return res

def checkIfUserExist(ids, allFields = False):
    if(allFields):
        sql = "select * from users where id = {}".format(ids)
        cur.execute(sql)
        res = cur.fetchmany()

    else:
        sql = "select name from users where id = {}".format(ids)
        cur.execute(sql)
        res = cur.fetchone()
    if(cur.rowcount != 1):
        return False
    else:
        return res

def updateStock(ids, stock):
    sql = "Update products set stock = stock + {} where id = {}".format(stock, ids)
    cur.execute(sql)
    con.commit()
    return True

def updateProduct(ids, data):
    sql = "Update products set name = '{}', mrp = {}, s_price = {}, stock = {} where id = {}".format(data[0], data[1], data[2], data[3], ids)
    cur.execute(sql)
    con.commit()
    return True

def removeProduct(ids):
    sql = "Delete from products where id = {}".format(ids)
    cur.execute(sql)
    con.commit()
    return True

def removeUser(ids):
    sql = "Delete from users where id = {}".format(ids)
    cur.execute(sql)
    con.commit()
    return True

def qtyManager(ids, qty):
    sql = "select * from products where id = {}".format(ids)
    cur.execute(sql)
    res = cur.fetchone()
    if(int(res[4]) > qty or int(res[4]) == qty):
        return True
    else:
        return int(res[4])

def getProductPrice(ids):
    sql = "select s_price from products where id = {}".format(ids)
    cur.execute(sql)
    res = cur.fetchone()
    return res[0]

def payBill(ids, bill, dat):
    sql = "select * from users where id = {}".format(ids)
    cur.execute(sql)
    user = cur.fetchone()
    if(user[4] > bill or user[4] == bill):
        sql = "Update users set bal = bal - {} where id = {}".format(bill, ids)
        cur.execute(sql)
        con.commit()
        sql = '''Insert into orders values({}, {}, "{}", {})'''.format(NewId('orders'), ids, json.dumps(dat), bill)
        cur.execute(sql)
        con.commit()
        for i in dat:
            sql = "Update products set stock = stock - {} where id = {}".format(i[3], ids)
            cur.execute(sql)
            con.commit()
        return True
    else:
        return False

def addBalance(ids, amt):
    sql = "update users set bal = bal + {} where id = {}".format(amt, ids)
    cur.execute(sql)
    con.commit()
    return True

def updatePassword(ids, newPas):
    sql = "update users set pass = '{}' where id = {}".format(newPas, ids)
    cur.execute(sql)
    con.commit()
    return True

def fetchOrderData(ids):
    sql = "select id,order_summary,total from orders where userId = {}".format(ids)
    cur.execute(sql)
    res = cur.fetchall()
    if(cur.rowcount == 0):
        return False
    else:
        return res
