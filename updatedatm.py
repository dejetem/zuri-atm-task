import datetime
username = None
password = None
db = {}


db_user = {
   'Simon':'Passwordsimon',
    'Seyi':'Passwordseyi',
    'Love':'PasswordLove'
}

def create_users():
    username = input("Enter Username:")
    password = input("Enter Password:")
    db[username] = (password)
    print(db)
    print("Welcome " + username)
    return db

def login(db):
    username = input("Username:")
    password = input("Password:")
    return db[username] == (password)

def go():
    db = create_users()
    if login(db):
        print("LoginSuccessful")
    else:
        print("Invalid Login")
        exit() 

def Sign():
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in db_user and password == db_user[name]):
        print("Welcome " + name)
        return True
    else:
        print("Password or Username Incorrect")
        return False


def Operations():
    date_time = datetime.datetime.now()
    print(date_time.strftime("%Y-%b-%d %H:%M"))
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))
            
    if(selectedOption == 1):
        print('you selected %s' % selectedOption)
        print('How much would you like to withdraw')
        amount = int(input('enter amount:'))
        print('take your cash %s' % amount)
        Operations()
                
    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
        print('How much would you like to deposit')
        amount = int(input('enter amount:'))
        print('current balance %s' % amount)
        Operations()
                
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)
        print('What issue will you like to report')
        amount = input('enter complaint:')
        print('Thank you for contacting us' )
        Operations()

    elif(selectedOption == 4):
        exit()   
    else:
        print('Invalid Option selected, please try again')




print("Welcome, what would you like to do?")
print("1. Register")
print("2. Login")



actionSelect = int(input("Select an option \n"))   

if(actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = go()
        Operations()

            
elif(actionSelect == 2):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = Sign()
        Operations()
    
else:
    print('Invalid, username or password incorrect')