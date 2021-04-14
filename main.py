import datetime

name = input('What is your name? \n')

allowedUsers = ['Simon', 'Seyi', 'Love']
allowedPassword = ['Passwordsimon', 'Passwordseyi', 'PasswordLove']

if(name in allowedUsers ):
    password = input('Your password? \n')
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):
        print('Welcome %s' % name)
        date_time = datetime.datetime.now()
        print(date_time.strftime("%Y-%b-%d %H:%M"))
        print('these are the available options')
        print('1. Withdrawal')
        print('2. Cash deposit')
        print('3. Complaint')
        selectedOption = int(input('please select an option:'))
        if(selectedOption == 1):
            print('you selected  %s' % selectedOption)
            print('How much would you like to withdraw')
            amount = int(input('enter amount:'))
            print('take your cash %s' % amount)
        elif(selectedOption ==2):
            print('you selected  %s' % selectedOption)
            print('How much would you like to deposit')
            amount = int(input('enter amount:'))
            print('current balance %s' % amount)
        elif(selectedOption ==3):
            print('you selected  %s' % selectedOption)
            print('What issue will you like to report')
            amount = input('enter complaint:')
            print('Thank you for contacting us' )
        else:
            print('invalid option selected, please try again')
    else:
        print('password incorrect, please try again')
else:
    print('name not found, please try again')

