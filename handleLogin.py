import handleDataBase as db
import time
import pythonProject
db.fetch()
userIndex = 0
def login():
    db.fetch()
    receivedData = input('Enter your Email Or Phone Number >>>... ')
    if receivedData in db.allUserPhoneNumber or receivedData in db.allUserEmail:
        receivedPassword = input('Enter your Password >>>... ')
        for items in db.allUsersData:
            global userIndex
            if receivedData in items:
                break
            userIndex = int(userIndex + 1)
        if receivedPassword == db.alluserpassword[userIndex]:
            print('\nlogin successful \n')
            time.sleep(1.5)
            import handleSignedInUserFunction as action
            db.fetch()
            action.userFunction()

        else:
            print('Wrong Pin.')
            pythonProject.userAction()

    else:
        print('The email or phone number you enter is not registered. Try registering.')
        pythonProject.userAction()