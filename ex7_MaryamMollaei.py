#012*******************
print('Enter first number:')
num1=int(input())
print('Enter second number:')
num2=int(input())
if num1>num2:
    print(num2,num1)
else:
    print (num1,num2)    
#013**********************
print('Enter a number under 20:')
num3=int(input())
if num3>=20 :
    print('Too high')
else:
    print('Thank You!!!')
#14************************
print('Enter a number between 10 and 20:')
num4=int(input())
if num4>=10 and num4<=20 :
    print('Thank You!!!')
else:
    print('Incorrect Answer')
#15***************************
print('Please enter your favorite colour:')    
color=input()
if color=='RED' or color=='Red':
     print('My favorite color is red too')
else:
     print('I dont like',color,'I prefer Red')
#16**************************************

print('Is it rainy:')
ans1=input()
if ans1=='yes' :
    print('Is it windy?')
    ans2=input()
    if ans2=='yes':
        print('It is too windy for an umbrella...')
    else:
        print('Take an umbrella')
else:
    print('Enjoy your day!')

#17**********************************
print('How old are you?')
age=int(input())
if age>=18:
    print('You can vote')
elif age==17:
    print('You can drive')
elif age==16:
    print('You can buy a lottery ticket')
elif age<16:
    print('You can go trick or treating')

#18******************************
print('Enter a number:')
number=int(input())
if number<10:
    print('Too low!')
elif number>10 and number<20 :
    print('Correct')
else:
    print('Too high')
#19***********************
print('Enter 1 or 2 or 3 ') 
digit=input()
if digit==1:
    print('Thank you')
elif digit==2:
    print('Well done')
elif digit==3:
    print('correct')
else:
    print ('Error message')







    
     
    
