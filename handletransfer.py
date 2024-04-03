import handleLogin as lg
import handleDataBase as db
import handleSignedInUserFunction as hf
userIndex = db.allUsersData[lg.userIndex]
def act():
    index = 0
    number = input('Enter the person number you want to transfer to >>>. ')
    if number in db.allUserPhoneNumber:
        for i in db.allUsersData:
            if i[4] == number:
                break
            index += 1

        amt = input('How much will you like to transfer >>> ')
        try:
            if int(amt) <= int(userIndex[6]):
                print(f'\n>>>>>>>>>>>>>>>>>  You are about to transfer {amt} to {db.allUsersData[index][1].title()} {db.allUsersData[index][2].title()} <<<<<<<<<<<<<<<<<<<\n')
                pin = input('Enter your pin to complete transaction >>> ')
                if pin == userIndex[5]:
                    updateSenderBalance = f'UPDATE allusers SET balance="{int(userIndex[6]) - int(amt)}" WHERE phoneNumber="{userIndex[4]}"'
                    updateReceiverBalance = f'UPDATE allusers SET balance = "{int(db.allUsersData[index][6]) + int(amt)}" WHERE phoneNumber = "{number}"'
                    db.connector.execute(updateSenderBalance)
                    db.connector.execute(updateReceiverBalance)
                    db.data.commit()
                    print(f'Transaction successful, you have successfully sent  {amt} to {db.allUsersData[index][1].title()} {db.allUsersData[index][2].title()}')
                    hf.userFunction()
                else:
                    print('Wrong Pin, try again')
                    hf.userFunction()
            else:
                print(f'You do not have up to {amt} in your account.')
                hf.userFunction()
        except:
            print('Amount should be numbers only, it should not contain letters or sybols.')
            hf.userFunction()
    else:
        print('The person you are trying to send money to is not registered to soft credit')
        hf.userFunction()