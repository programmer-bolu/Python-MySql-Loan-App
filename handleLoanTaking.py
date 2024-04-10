import datetime as dt
import handleDataBase as db
import handleLogin as login
import time as tm
import handleSignedInUserFunction as hsif
SaveToLoanedUser = 'INSERT INTO loneduser (phoneNumber, loanedAmt, loanedDate, dateToPayLoan) VALUES(%s, %s, %s, %s)'
def tl():
    print('You will pay a interest of 20% of the money you loaned')
    userIndex = db.allUsersData[login.userIndex]
    currentDay = dt.datetime.now()
    loanAmount = input('\nHow much loan will you like to take Maximum("#1,000,000")>>>. ')
    loanedUserValue = [userIndex[4]]
    try:
        loanAmount = int(loanAmount)
        if loanAmount <= 1000000 and int(db.allUsersData[0][6]) - loanAmount >= 0:
            loanedUserValue.append(str(loanAmount + (0.2 * loanAmount)))
            time = f'\nWhen will you like to pay the loan ||| RANGE( {currentDay.strftime("%m")}/{currentDay.strftime("%Y")} to {int(currentDay.strftime("%m")) + 3}/{currentDay.strftime("%Y")}) |||'
            print(time)
            time = input('Enter in this format 01/2001 >>>>  ')
            if len(time) == 7:
                if int(time[0] + time[1]) <= int(currentDay.strftime("%m")) + 3 and int(time[3]+time[4]+time[5]+time[6]) == int(currentDay.strftime("%Y")):
                    loanedUserValue.append(f'{currentDay.strftime("%m")}/{currentDay.strftime("%Y")}')
                    loanedUserValue.append(time)
                    updateBalance = f'UPDATE allusers SET balance="{loanAmount + int(userIndex[6])}" WHERE phoneNumber="{userIndex[4]}"'
                    updateAdmin = f'UPDATE allusers SET balance="{int(db.allUsersData[0][6]) - loanAmount}" WHERE phoneNumber="09019525536"'
                    db.connector.execute(SaveToLoanedUser, loanedUserValue)
                    db.connector.execute(updateBalance)
                    db.connector.execute(updateAdmin)
                    db.data.commit()
                    db.fetch()
                    tm.sleep(1)
                    print(f'\nLoaned Successful Taken for {(userIndex[1]).title()} {(userIndex[2]).title()}. Check your Balance...\nFor any Enquiry contact +2349019525536\n')
                    db.fetch()
                    hsif.userFunction()
                else:
                    print(f'The loan Range Is ({currentDay.strftime("%m")}/{currentDay.strftime("%Y")} to {int(currentDay.strftime("%m")) + 3}/{currentDay.strftime("%Y")})')
                    hsif.userFunction()
            else:
                print('Error parsing information, make sure the date is in this format ___01/2001___')
                hsif.userFunction()
        else:
            print('Input out of range, try again')
            tl()
    except:
        print('Amount should be numbers only, there should not be letters or symbols')
        hsif.userFunction()
