import handleLogin as login
import handleDataBase as db
import handleSignedInUserFunction as hf
userIndex = db.allUsersData[login.userIndex]
index = 0
amt = input('How much will you like to pay >>>. ')
def confirm():
    global amt
    if userIndex[4] in db.LoanedUserNumber:
        for i in db.LoanedUserNumber:
            global index
            if i == userIndex[4]:
                break
            index += 1    
    try:
        amt = int(amt)
        payment()
    except:
        print('Amount should be Numbers only, it should not contan letters or symbols.')
        import handleSignedInUserFunction as ff
        ff.userFunction()

def payment():
    # print(userIndex)
    con = input('Enter your Pin >>> ')
    if con == userIndex[5]:
        if int(db.loanedUser[index][2]) - int(amt) == 0:
            action = f'DELETE FROM loneduser WHERE phoneNumber = "{db.loanedUser[index][1]}"'
            updateuserbalance = f'UPDATE allusers SET balance = "{int(userIndex[6]) - int(amt)}" WHERE phoneNumber = "{userIndex[4]}"'
            updateadminbalance = f'UPDATE allusers SET balance = "{int(db.allUsersData[0][6]) + int(amt)}" WHERE phoneNumber = "09019525536"'
            db.connector.execute(action)
            db.connector.execute(updateadminbalance)
            db.connector.execute(updateuserbalance)
            db.data.commit()
            print('Loan paied successfully, you have cleared your loan')
            hf.userFunction()
        elif int(db.loanedUser[index][2]) - int(amt) < 0:
            action = f'DELETE FROM loneduser WHERE phoneNumber = "{db.loanedUser[index][1]}"'
            updateuserbalance = f'UPDATE allusers SET balance = "{int(userIndex[6]) - int(db.loanedUser[index][2])}" WHERE phoneNumber = "{userIndex[4]}"'
            updateadminbalance = f'UPDATE allusers SET balance = "{int(db.allUsersData[0][6]) + int(db.loanedUser[index][2])}" WHERE phoneNumber = "09019525536"'
            db.connector.execute(action)
            db.connector.execute(updateadminbalance)
            db.connector.execute(updateuserbalance)
            print(f'Loan paid successful {db.loanedUser[index][2]} was deducted, you have cleared your loan')
            db.data.commit()
            hf.userFunction()
        else:
            action = f'UPDATE loneduser SET loanedAmt="{int(db.loanedUser[index][2]) - amt}" WHERE phoneNumber="{userIndex[4]}"'
            updateuserbalance = f'UPDATE allusers SET balance="{int(userIndex[6]) - amt}" WHERE phoneNumber="{userIndex[4]}"'
            updateadminbalance = f'UPDATE allusers SET balance="{int(db.allUsersData[0][6]) + amt}" WHERE phoneNumber="09019525536"'
            db.connector.execute(action)
            db.connector.execute(updateadminbalance)
            db.connector.execute(updateuserbalance)
            db.data.commit()
            db.fetch()
            print(f'Loan paid successful {amt} was deducted, check your balance to view your pending loan.')
            hf.userFunction()
    else:
        print('Wrong Pin, Try again')
        hf.userFunction()

def main():
    if int(amt) <= int(userIndex[6]):
        confirm()
    else:
        print(f'You did not have up to {amt} in your account')
        hf.userFunction()
