import funct as fun
import conn as server
import databaseSetup as dbSet







def space(sp = 1):
    fun.space(sp)

def getList(cart, pri = False):
    dat = []
    price = 0
    for i in cart:
        newTup = []
        newTup.append(i)
        ind = 1
        for j in cart[i]:
            newTup.append(j)
            ind = ind + 1
        price = price + (cart[i][1] * cart[i][2])
        newTup.append(cart[i][1] * cart[i][2])
        dat.append(newTup)
    if(pri):
        return price
    else:
        return dat

#application
def main():
    dbSet.checkDatabase()
    fun.showopt(fun.one)
    a = fun.inp('Role')
    space()
    if(a == 1):
        # if user choosed user application
        cart = {}
        user = None
        def userRole():
            fun.msg('What would you like to do'.capitalize())
            space()
            fun.showopt(fun.two)
            b = fun.inp('Choice')
            space()
            if(b == 1):
                def userLogin():
                    ud = fun.userLoginDetails()
                    check = server.checkLogin(ud)
                    if(check != False):
                        user = check[0]
                        fun.msg('Welcome ' + check[1].capitalize())
                        def addItemToCart(ids, name, qty, price):
                            cart[ids] = [name, qty, server.getProductPrice(ids)]
                        def userFun():
                            b = fun.showopt(fun.three)
                            c = fun.inp()
                            if(c == 1):
                                ua = server.fetchAllProducts(True)
                                if(ua != False):
                                    fun.showTable(ua, ['Id', 'Product Name', 'Market Price', 'Our Price'])
                                    space()
                                else:
                                    fun.showTable([[]], ['Id', 'Product Name', 'Market Price', 'Our Price'])
                            elif(c == 2):
                                def addProductToCart():
                                    ub = fun.c_inp('Enter Product Id ')
                                    uc = server.checkIfProductExists(ub)
                                    if(uc != False):
                                        ud = fun.c_inp('Enter Qty ')
                                        checkQty = server.qtyManager(ub, ud)
                                        if(checkQty != True):
                                            fun.err('We Are Sorry To Inform You')
                                            fun.err('Only ' + str(checkQty) +' Qty Of ' + uc[0] +' Is Left')
                                            fun.err('Adding ' + str(checkQty) + ' ' + uc[0] +' To Your Cart')
                                            ud = checkQty
                                        else:
                                            fun.err('Adding ' + str(ud) + ' ' + uc[0] +' To Your Cart')
                                        addItemToCart(ub, uc[0], ud, 0)
                                        space()
                                        fun.showopt(fun.six)
                                        space()
                                        ue = fun.inp()
                                        if(ue == 1):
                                            addProductToCart()
                                        else:
                                            userFun()
                                    else:
                                        fun.err('No Product Exist With This Id ' + str(ub))
                                addProductToCart()
                            elif(c == 3):
                                dat = getList(cart)
                                space()
                                fun.showTable(dat, ['Id', 'Product Name', 'Cost', 'Qty', 'Total'])
                                space()
                                fun.c_inp('Press Any Key To Continue ')
                                space()
                            elif(c == 4):
                                dat = getList(cart)
                                space()
                                fun.err('Your Invoice')
                                fun.showTable(dat, ['Id', 'Product Name', 'Cost', 'Qty', 'Total'])
                                fun.err('Total Bill : ' + str(getList(cart, True)))
                                space()
                                fun.showopt(fun.seven)
                                space()
                                uf = fun.inp()
                                if(uf == 1):
                                    payed = server.payBill(user, getList(cart, True), dat)
                                    if(payed):
                                        fun.err('Bill Payed')
                                        fun.err('Tankyou for shopping with us')
                                        fun.err('Will be waiting for your next order')
                                    else:
                                        fun.err('Insufficient Balance')
                                        fun.err('Please Add Balance')
                                elif(uf == 2):
                                    userFun()
                            elif(c == 5):
                                uf = server.fetchOrderData(user)
                                if(uf != False):
                                    fun.showTable(uf, ['Order Id', 'Order Summary', 'Total Price'])
                                else:
                                    fun.err('No Order Placed Yet')
                            elif(c == 6):
                                ag = fun.c_inp('Enter Ammount Rs. ')
                                af = fun.c_inp('Enter UPI Id ', False)
                                server.addBalance(user, ag)
                                fun.err('Balance Udated Sucessfuly')
                                space()
                            elif(c == 7):
                                def changePas():
                                    ag = fun.c_inp('Enter New Password', False)
                                    server.updatePassword(user, ag)
                                    fun.err('Updating Password')
                                    fun.err('Password Updated Sucessfuly')
                                changePas()
                            elif(c == 8):
                                profileData = server.fetchUserProfile(user)
                                space()
                                fun.err('Your Profile Informations')
                                fun.showTable([profileData], ['Id', 'Name', 'Email', 'Balance'])
                                space()
                                fun.c_inp('Press Any Key To Continue', False)
                            elif(c == 9):
                                userRole()

                            userFun()
                        userFun()
                        
                    else:
                        fun.err('Invalid Login Details')
                        a = fun.again()
                        space()
                        if(a == 1):
                            userLogin()
                        else:
                            userRole()
                userLogin()
            elif(b == 2):
                def createUser():
                    ud = fun.takeUserDetails()
                    server.newUser(ud)
                    fun.msg('Your Accoun has been created sucessfuly')
                    userRole()
                createUser()
            elif(b == 3):
                main()
            elif(b == 4):
                fun.shutDown()
        userRole()
    # if user choosed admin application
    elif(a == 2):
        def admin():
            fun.msg('Admin Area')
            fun.err('Enter Your Login Creds')
            a = fun.adminLoginInput()
            b = server.checkAdminLogin(a)
            if(b != False):
                fun.msg('Welcome ' + b[1])
                def adminFun():
                    fun.showopt(fun.four)
                    c = fun.inp()
                    space()
                    if(c == 1):
                        users = server.fetchAllUsers()
                        if(users != False):
                            fun.showTable(users, ['Id', 'Name', 'Email', 'Balance'])
                        else:
                            fun.err('No users Found')
                    elif(c == 2):
                        aa = fun.c_inp('Enter user userId ')
                        uf = server.fetchOrderData(aa)
                        if(uf != False):
                            fun.showTable(uf, ['Order Id', 'Order Summary', 'Total Price'])
                        else:
                            fun.err('User Had Not Placed Any Order Yet')
                    elif(c == 3):
                        aa = fun.takeProductInput()
                        server.newPrduct(aa)
                        fun.err('New Product Added Sucessfuly')
                    elif(c == 4):
                        aa = fun.c_inp('Enter product id ')
                        ab = server.checkIfProductExists(aa)
                        if(ab != False):
                            ac = fun.c_inp('Enter addition stock')
                            server.updateStock(aa, ac)
                            fun.err('Stock Updated Sucessfuly')
                        else:
                            fun.err('No Product Exist with id ' + str(aa))
                    elif(c == 5):
                        aa = fun.c_inp('Enter product id ')
                        ab = server.checkIfProductExists(aa, True)
                        if(ab != False):
                            fun.msg('Currect Details Of Product With Id ' + str(aa))
                            fun.showTable(ab, ['Id', 'Product Name', 'Market Price', 'Selling Price', 'Stock'])
                            ac = fun.takeProductInput()
                            server.updateProduct(aa, ac)
                            fun.err('Product Updated sucessfuly')
                        else:
                            fun.err('No Product Exist with id ' + str(aa))
                    elif(c == 6):
                        aa = fun.c_inp('Enter product id ')
                        ab = server.checkIfProductExists(aa)
                        if(ab != False):
                            fun.err('Are You Sure You Want To Remove This Product')
                            fun.showopt(fun.five)
                            c = fun.inp()
                            if(c == 1):
                                server.removeProduct(aa)
                                fun.msg('Product Removed Sucessfuly')
                        else:
                            fun.err('No Product Exist with id ' + str(aa))
                    elif(c == 7):
                        products = server.fetchAllProducts()
                        if(products != False):
                            fun.showTable(products, ['Id', 'Product Name', 'Market Price', 'Selling Price', 'Stock'])
                        else:
                            fun.err('No Products Listed Yet')
                    elif(c == 8):
                        aa = fun.c_inp('Enter user id ')
                        ab = server.checkIfUserExist(aa)
                        if(ab != False):
                            fun.err('Are You Sure You Want To Remove This User')
                            fun.showopt(fun.five)
                            ac = fun.inp()
                            if(ac == 1):
                                server.removeUser(aa)
                                fun.msg('User Removed Sucessfuly')
                        else:
                            fun.err('No Product Exist with id ' + str(aa))
                    elif(c == 9):
                        main()
                    elif(c == 0):
                        fun.shutDown()
                    space()
                    fun.c_inp('Press any key to continue ', False)
                    space()
                    adminFun()
                adminFun()
                
            else:
                fun.err('Invlid Choice')
            admin()
        admin()
    # if user wants to close the application
    else:
        fun.shutDown()


fun.welcome()
main()



