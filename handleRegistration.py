import handleDataBase as db
import pythonProject
import time

adminBalance = int(db.allUsersData[0][6]) 
databaseValue = []
age = '0'
firstName = ''
LastName = ''
email = ''
def register():
    global age
    firstName = input('What is your First Name >>>. ')
    LastName = input('What is your Last Name >>>. ')
    age = input('What is your age >>>  ')
    if len(firstName) >= 2 and len(LastName) >= 2:
        databaseValue.append((firstName))
        databaseValue.append((LastName))
        emails()
    else:
        print('Username should be more than two values, Please try again. =( ')
        register()
        
def emails():
    email = input('What is your email >>>. ')
    if '@' in email and '.' in email and not email.endswith('.') and not  email.endswith('@') and not email.startswith('.') and not  email.startswith('@') and email.index('@') - email.index('.') != 1:
        # Authentication
        if not email in db.allUserEmail:
            databaseValue.append((email))
            phoneNumbers()
        else:
            print('Email already in use, please use another email.')
            emails()
    else:
        print('Our system noticed an incorrect  email addresss, please try again, sorry for any inconvinence...')
        emails()

def phoneNumbers():
    phoneNumber = input('What is your phone Number >>>. ')
    if not phoneNumber in db.allUserPhoneNumber:
        if len(phoneNumber) == 11:
            try:
                phoneNumber = int(phoneNumber)
                phoneNumber = '0' + str(phoneNumber)
                databaseValue.append((phoneNumber))
                passwordFunc()
            except:
                print('Phone Number should be numbers only. It should not contain letters or symbols')
                phoneNumbers()
        else:
            print('Phone Number should be 11 digits')
            phoneNumbers()
    else:
        print('Phone Number is been used by someone else, please try another number.')
        phoneNumbers()

def passwordFunc():
    global age
    password = input('Add a 4 digit pin >>>. ')
    if len(password) == 4:
        try:
            if int(age) >= 18:
                if not password.startswith('0'):
                    password = int(password)
                    password = str(password)
                else:
                    password = int(password)
                    password = '0' + str(password)
                databaseValue.append((password))
                databaseValue.append((100))
                updateAdmin = f'UPDATE allusers SET balance="{adminBalance - 100}" WHERE phoneNumber="09019525536"'
                sendToDb = 'INSERT INTO allusers (firstname, lastname, email, phoneNumber, password, balance) VALUES(%s, %s, %s, %s, %s, %s)'
                db.connector.execute(sendToDb, databaseValue)
                db.connector.execute(updateAdmin)
                db.data.commit()
                db.fetch()
                print('Account Created Successfully \n\n')
                time.sleep(1.5)
                pythonProject.userAction()
            else:
                print('Account Cannot Be created.')
                passwordFunc()
        except TypeError:
            print('Pin should be numbers only. It should not contain letters or symbols')
            passwordFunc()
    else:
        print('User pin should be a length of four')
        passwordFunc()