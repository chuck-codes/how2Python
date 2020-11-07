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
    myName= input('What is your name? ')
    myAge= input('What is your age? ')
    while True:
        try:
            myAge= int(myAge)
            if myAge >0:
                break
            else:
                myAge= input('Please enter a postive number for your age: ')
        except:
            myAge= input('Please enter a number for your age: ')
    myEmail= input('What is your email? ')
    #print(f'My test name is {testName} My test Age is {testAge} and my test email is {testEmail}')
    return myName, myAge, myEmail


def add2DB(age, name, email):
    f = open("userDB.txt", "a+")
    f.write(f"{age} | {name} | {email}\n")
    f.close()
    print('All done')



def main():
    flag= True
    while flag== True:
        isDone= input('Do you want to stop? (Type "yes" to stop) ')
        if isDone.lower()== "yes":
            flag= False
            print('Thanks for playing')
            
        else:
            testName, testAge, testEmail= gatherDetails()
            add2DB(testName,testAge,testEmail)
            


main()
'''
How to determine a single value for a user in organized data
f = open("userDB.txt", "r")
lines= f.readlines()
f.close()
person1= lines[0]
#print(person1)
p1= person1.split('|')
#print(p1)
print(p1[1])
'''
