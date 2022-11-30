one = {
    '1.' : 'User',
    '2.' : 'Manager',
    '3.' : 'Close Application'
    }
two = {
    '1.' : 'Login',
    '2.' : 'Create New Account',
    '3.' : 'Back',
    '4.' : 'Close Application'
    }
three = {
    '1.' : 'View All Products',
    '2.' : 'Add Products To Cart',
    '3.' : 'View Cart',
    '4.' : 'Generate Invoice And Pay Bill',
    '5.' : 'Order History',
    '6.' : 'Add Balance',
    '7.' : 'Change Password',
    '8.' : 'View Profile',
    '9.' : 'Back',
#    '0.' : 'Close Application'
    }
four = {
    '1.' : 'Show All Users',
    '2.' : 'Show Users Order History',
    '3.' : 'Add Product',
    '4.' : 'Update Stock',
    '5.' : 'Update Product',
    '6.' : 'Remove Product',
    '7.' : 'Show All Products',
    '8.' : 'Remove User',
    '9.' : 'Back',
    '0.' : 'Close Application'
    }
five = {
    '1.' : 'Yes',
    '2.' : 'Cancel'
    }
six = {
    '1.' : 'Add More Products',
    '2.' : 'Back'
    }
seven = {
    '1.' : 'Pay Bill',
    '2.' : 'Back'
    }

def centerString(st, surround_by = ' ', strCover = 100):
    ml = len(st)
    left = strCover - ml
    halfLeft = left//2
    additional = 0
    if(left%2 != 0):
        additional = 1
    return (surround_by * (halfLeft + additional)) + st + (surround_by * halfLeft)

def welcome():
    newStr= centerString('Welcome', '-', 98)
    print('+'+ newStr +'+')
    print('')

def space(sp = 1):
    for i in range(sp):
        print()

def reboot():
        err('Invalid choice')
        err('Application Closed')
        err('Please Restart The Application')

def shutDown():
    err('Working..')
    err('Closing Application')
    err('Application Closed')

def err(err):
    newStr = centerString(err)
    #print()
    print(line())
    print(newStr)
    print(line())
    #print()

def inp(msg = 'Choice'):
    space()
    a = input('Enter your ' + msg + ' ')
    if(a.isdigit()):
        return int(a)
    else:
        err('Please enter only Intereger values'.capitalize())
        err('Application Closed')
        return False

def showopt(li):
    for i in li:
        print(i, li[i])

def again():
    li = {
        '1.' : 'To Try Again',
        '2.' : 'To Go Back'
        }
    showopt(li)
    return inp()


def takeUserDetails():
    name = str(input('Enter your name '))
    email = str(input('Enter your email '))
    pas = str(input('Enter your password '))
    return [name, email, pas]

def userLoginDetails():
    email = str(input('Enter your email '))
    pas = str(input('Enter your password '))
    return [email, pas]

def line():
    return ('+'+ '-' * 98 +'+')


def msg(msg = 'Tankyou'):
    newStr = centerString(msg)
    #print()
    print(line())
    print()
    print(newStr)
    print()
    print(line())
    #print()

def adminLoginInput():
    username = str(input('Enter your username '))
    pas = str(input('Enter your password '))
    return [username, pas]

def showTable(li, titles):
    head = []
    maxHeadSPace = []
    for i in titles:
        head.append(i)
        maxHeadSPace.append(len(i))
    for k in li:
        curInd = 0
        for j in k:
            if(len(str(j)) > maxHeadSPace[curInd]):
                maxHeadSPace[curInd] = len(str(j))
            curInd = curInd + 1

    bar = '+'
    for i in range(len(titles)):
        newLine = '-' * maxHeadSPace[i]
        bar = bar + '-' + newLine + '-+'
    print(bar)
    curIndx = 0
    for i in titles:
        a = (maxHeadSPace[curIndx])
        b = (len(str(i)))
        print('| ', end='')
        print(i, end='')
        print(' ' * (a-b), end=' ')
        curIndx = curIndx+1
    print('|')
    print(bar)
    for i in li:
        curInd = 0
        for j in i:
            a = (maxHeadSPace[curInd])
            b = (len(str(j)))
            print('| ', end='')
            print(j, end='')
            print(' ' * (a-b), end=' ')
            curInd = curInd+1
        print('|')
        print(bar)

def takeProductInput(update = True):
    name = str(input('Enter product name '))
    mrp = int(input('Enter mrp '))
    sp = int(input('Enter selling price '))
    stock = int(input('Enter available stock '))
    return [name, mrp, sp, stock]

def c_inp(m, a = True):
    if(a):
        return int(input(m))
    else:
        return str(input(m))
    
    
        
    

