#Doing stuff with input output

numberOfTimes= 5
anyName= 'Chuck'
'''
#Test 1
if True== True:
    print('True is True')
else:
    print('This is not true')
#Test 2
if True== 'True':
    print('True is True')
else:
    print('This is not true')
#Test 3
if 1== 1:
    print('True is True')
else:
    print('This is not true')
#Test 4
if 1+1 == 2:
    print('True is True')
else:
    print('This is not true')
'''
flag= True
'''
while flag== True:
    anyName= input('What is your name? (Type "stop" to stop) ')
    if anyName.lower()!= "stop":
        print(f'hooray {anyName}')
    else:
        flag= False
        print('Have a nice day.')
'''   
    
#Doing stuff with input and output; but make it fancy
'''Takes a users name, age, email address'''
'''Name[string]     Age[int]   Email Address[string]'''
''' no numbers        >9        text@text.domain'''
def gatherDetails():
    while True:
        #Get Name
        try:
            myName= str(input('What is your name? '))
        except:
            print(f'{myName} is not the kind of name I recognize. Please try again')
        #Get Age
        try:
            myAge= int(input('What is your age? '))
        except:
            myAge= int(input('Please try a number '))
        #Get Email
        try:
            myEmail= str(input('Please enter your email '))
        except:
            print(f'{myEmail} is not the kind of name I recognize. Please try again')
        
        return myName, myAge, myEmail




testName, testAge, testEmail= gatherDetails()
print(f'My test name is {testName} My test Age is {testAge} and my test email is {testEmail}')



























'''
def gatherDetails():
    myName= input('What is your name? ')
    myAge= input('What is your age? ')
    myEmail= input('What is your email? ')








try:
    myName= str(myName)
except:
    print(f'{myName} is not the kind of name I recognize. Please try again')

'''