def createDatabase(cur):
    sql = "Create database shop"
    cur.execute(sql)

def createAdminTbl(cur):
    sql = "create table admin(\
    id int primary key,\
    name varchar(30),\
    pass varchar(30)\
    )"
    cur.execute(sql)

def createUserTbl(cur):
    sql = "create table users(\
    id int primary key,\
    name varchar(30),\
    email varchar(30),\
    pass varchar(30),\
    bal int\
    )"
    cur.execute(sql)

def createProductTable(cur):
    sql = "create table products(\
    id int primary key,\
    name varchar(30),\
    mrp int,\
    s_price int,\
    stock int\
    )"
    cur.execute(sql)

def createOrder(cur):
    sql = "create table orders(\
    id int primary key,\
    userId int,\
    order_summary varchar(250),\
    total int\
    )"
    cur.execute(sql)
    
