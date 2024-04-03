import handleLogin as login
import handleDataBase as db
import handleSignedInUserFunction as hf
import datetime as dt
saveUserToInvestedUser = []
def function():
    userIndex = db.allUsersData[login.userIndex]
    index = 0
    if userIndex[4] in db.LoanedUserNumber:
        for i in db.loanedUser:
            if i[1] == userIndex[4]:
                break
            index += 1

    if not userIndex[4] in db.LoanedUserNumber:
        amount = input('How much will you like to invest RANGE(__#100____#1,000,000) >>>  ')
        try:
            amount = int(amount)
            amount = str(amount)
            saveUserToInvestedUser.append(userIndex[4])
            saveUserToInvestedUser.append(amount)
            if amount <= userIndex[6]:
                if int(amount) <= 1000000 and int(amount) >= 100:
                    confirm = input('Enter your pin to confirm investment >>> ')
                    if confirm == userIndex[5]:
                        saveUserToInvestedUser.append(userIndex[6])
                        updateUserBalance = f'UPDATE allusers SET balance = "{int(userIndex[6]) - int(amount)}" WHERE phoneNumber = "{userIndex[4]}" '
                        updateAdminBalance = f'UPDATE allusers SET balance = "{int(db.allUsersData[0][6]) + int(amount)}" WHERE phoneNumber = "09019525536"'
                        db.connector.execute('INSERT INTO investedusers (phoneNumber, investAMT, acctBalance) VALUES(%s, %s, %s)', saveUserToInvestedUser)
                        db.connector.execute(updateUserBalance)
                        db.connector.execute(updateAdminBalance)
                        db.data.commit()
                        print('Invest Successful')
                        print('THANKS FOR INVESTING INTO SOFT CREDIT.')
                        hf.userFunction()
                    else:
                        print('Wrong Pin, please try again')
                        hf.userFunction()
                else:
                    print('Amount should be in range 100 to 1,000,000')
                    hf.userFunction()
            else:
                print(f'You do not have up to {amount} in your account, please fund your account')
                hf.userFunction()
        except:
            print('Could not process investment please try again later.')
            hf.userFunction
    else:
        print(f'Kindly pay your existing loan of {db.loanedUser[index][1]} to be able to invest into softCredit.')
        hf.userFunction()