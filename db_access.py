"""

Write functions in alphabetical order.

"""

import pymongo


def get_db():
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client['budget_analyzer']
    return (db)

def get_date():
    import datetime as dt
    day = dt.datetime.now().day
    month = dt.datetime.now().month
    year = dt.datetime.now().year
    return (day,month,year)

def get_balance(user_name):
    db = get_db()
    balance = db.balance.find({"user_name":user_name})[0]['balance']
    return (balance)
	
def get_password(user_name):
    db = get_db()
    #password = db.user_details.find({"user_name":"arun@gmail.com"})[0]['password']
    password = db.user_details.find({"user_name":user_name})[0]['password']
    return (password)

def set_balance(user_name):
    db = get_db()
    initial_balance = 0
    db.balance.insert({"user_name":user_name,"balance":initial_balance})
    
def update_balance(user_name,amount,income_expense):
    db = get_db()
    print ("In update balance")
	
    cursor = db.balance.find({"user_name" : user_name})
    old_balance = cursor[0]["balance"]
    new_balance = 0
    if income_expense == "income":
        new_balance = old_balance + int(amount)
    elif income_expense == "expense":
        new_balance = old_balance - int(amount)    
    
    db.balance.update_one({"user_name":user_name},{"$set": {"balance" :new_balance}})
    print ("Old balance: ",old_balance,"New balance ",new_balance)
    return 1

def check_user_name(user_name):
    db = get_db()
    cursor = db.user_details.find({"user_name": user_name})
    if cursor.count() == 0:  #user_name does not exist
        return True
    else:
        return False
    
def expense(user_name,expense,category,note):
    import dateutil.parser
    #print ('In mongo expense is ',expense,' category ',category)
    day,month,year = get_date()
    db = get_db()
    date = dateutil.parser.parse(str(year)+"-"+str(month)+"-"+str(day))  #Year month day order
    db.expense_tracker.insert( { "user_name":user_name,"date":date,"expense":int(expense),"category":category,"note":note})
    return 1

def income(user_name,amount,note):
    import dateutil.parser
    #print ('In mongo income is ',expense)
    day,month,year = get_date()
    db = get_db()
    date = dateutil.parser.parse(str(year)+"-"+str(month)+"-"+str(day))  #Year month day order
    db.expense_tracker.insert( { "user_name":user_name,"date":date,"income":float(amount),"note":note})
    return 1
    
def reset(user_name):
    #Delete this user_name's all recors in expense_tracker and balance
    db.expense_tracker.remove({"user_name":user_name})
    db.balance.remove({"user_name":user_name})
    return 1

def month_review(categories, user_name):
    #Modify code. Add plots and trend.
    start_date = datetime.datetime.now() + datetime.timedelta(-30)
    day = str(start_date.day)
    month = str(start_date.month)
    year = str(start_date.year)
    cursor = db.expense_tracker.find({"user_name": user_name ,"date": { "$gt": dateutil.parser.parse(year+"-"+month+"-"+day)}})
    expense = {}
    for i in cursor:
        if i['category'] in expense.keys():
            expense[i['category']] = expense[i['category']] + int(i['expense'])
        else:
            expense[i['category']] = int(i['expense'])
    return (expense)

def week_review(categories, user_name):
    #Add plots and trend.
    start_date = datetime.datetime.now() + datetime.timedelta(-30)
    day = str(start_date.day)
    month = str(start_date.month)
    year = str(start_date.year)
    cursor = db.expense_tracker.find({"user_name": user_name ,"date": { "$gt": dateutil.parser.parse(year+"-"+month+"-"+day)}})
    expense = {}
    for i in cursor:
        if i['category'] in expense.keys():
            expense[i['category']] = expense[i['category']] + int(i['expense'])
        else:
            expense[i['category']] = int(i['expense'])
    return (expense)	
    
def sign_up(user_name,password):
    db = get_db()  
    db.user_details.insert({"user_name":user_name,"password":password})
    print ("Sign Up Successful")
    return 1
     
