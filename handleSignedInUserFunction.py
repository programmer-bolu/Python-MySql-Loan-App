import handleDataBase as db
import handleLogin as login
import handleLoanTaking as tl
import handleInvestment
import handletransfer as ht
db.fetch()
def userFunction():
    global login
    userIndex = login.userIndex
    db.fetch()
    print(
    f''' ▶▶▶▶▶▶▶   Welcome {(db.allUsersData[userIndex][1]).title()} {(db.allUsersData[userIndex][2]).title()}   ◀◀◀◀◀◀◀
    To take a loan, input 1
    To invest into SoftCredit input 2
    To check Balance input 3
    To pay loan, input 4 
    To logout, input 5'''
    )
    userFunc = input('⨠⨠⨠⨠⨠  ')
    index = 0

    if db.allUsersData[userIndex][4] in db.LoanedUserNumber:
        for i in db.loanedUser:
            if i[1] == db.allUsersData[userIndex][4]:
                break
            index += 1    

    if userFunc == '1':
        db.fetch()
        if not db.allUsersData[userIndex][4] in db.LoanedUserNumber:
            tl.tl()
        else:
            print(f'\nUnable to process loan, kindly pay your existing loan of #{db.loanedUser[index][2]}')
            userFunction()
    elif userFunc == '3':
        import handleDataBase as database
        database.fetch()
        global save
        if db.allUsersData[userIndex][4] in db.LoanedUserNumber:
            print(f'\nYour balance is {db.allUsersData[userIndex][6]}\nYou have a loan balance of {db.loanedUser[index][2]}')
            userFunction()
        else:
            db.fetch()
            print(f'\nYour balance is {db.allUsersData[userIndex][6]}\n')
            userFunction()
    elif userFunc == '2':
        db.fetch()
        handleInvestment.function()
    elif userFunc == '5':
        import handleLogin as login
        db.fetch()
        print('LOGOUT SUCCESSFUL. ↺↺')
        import pythonProject
        pythonProject.userAction()
    elif userFunc == '4':
        if db.allUsersData[userIndex][4] in db.LoanedUserNumber:
            import handlePayLoan
        else:
            print('You do not have any pending loan to pay')
            userFunction()
    # elif userFunc == '5':
    #     ht.act()
    else:
        print('Wrong Input')
        userFunction()
