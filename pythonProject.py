import handleRegistration as registration
import handleLogin as login
import handleDataBase as db

logo = '''
__| |______________________________| |__
__   ______________________________   __
  | |                              | |  
  | |╔═╗╔═╗╔═╗╔╦╗  ╔═╗╦═╗╔═╗╔╦╗╦╔╦╗| |  
  | |╚═╗║ ║╠╣  ║   ║  ╠╦╝║╣  ║║║ ║ | |  
  | |╚═╝╚═╝╚   ╩   ╚═╝╩╚═╚═╝═╩╝╩ ╩ | |  
__| |______________________________| |__
__   ______________________________   __
  | |                              | |  
'''

def WelcomeUser():
    print(logo)
    print('Welcome to softPay Co-Operative app, a subsidiary of softCredit ..... Your one and only loan app.\nFREE #100 after registration.. ')

def userAction():
    userFunction = input('      ▶▶ To Create a Softcredit account, input 1\n      ▶▶ To Login, input 2 \n      ▶▶ For terms and conditions, input 3\n      ▶▶ To quit, input 4\n⨠⨠⨠⨠⨠  ')
    if userFunction == '1':
        registration.register()
    elif userFunction == '2':
        import handleLogin as login
        login.login()
    elif userFunction == '4':
        import sys
        sys.exit()
    else:
        print('Input out of range, try again')
        userAction()