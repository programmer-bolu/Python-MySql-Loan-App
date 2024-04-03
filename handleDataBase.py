import mysql.connector
data = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Ilerioluwa1@',
    database="co__orperative",
    auth_plugin ='mysql_native_password'
)

# MY SQL CONNECTOR
connector = data.cursor()
allUsersData = [] # ALL USERS ARRAY
allUserEmail = []# ALL USERS EMAIL ARRAY
allUserPhoneNumber = []# ALL USERS PHONE NUMBER
alluserpassword = []
LoanedUserNumber = []
loanedUser = []

def fetch():
    connector.execute('SELECT * FROM allusers')
    result = connector.fetchall()
    for rows in result:
        allUsersData.append(rows)
        allUserEmail.append(rows[3])
        allUserPhoneNumber.append(rows[4])
        alluserpassword.append(rows[5])
    # GETITNG ALL USERS FROM DATABASE INTO AN ARRAY 
    # GETTING ALL LOANED USERS INFORMATION

    connector.execute('SELECT * FROM loneduser')
    loanedresult = connector.fetchall()
    for rows in loanedresult:
        LoanedUserNumber.append(rows[1])
        loanedUser.append(rows)
fetch()
