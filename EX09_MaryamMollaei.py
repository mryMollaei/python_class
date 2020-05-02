#45********************************
print('#################################################################')
total=0
while total<=50:
    print('Enter a number:')
    num=int(input())
    total=total+num
print ('Total is:',total)    
print('#################################################################')
#46*************************************************
n1=0
while n1<5:
    print('Enter a number:')
    n1=int(input())

print('The last number you entered was a ',n1)
print('#################################################################')
#47***********************************************
print('Enter a number:')
num1=int(input())
print('Enter another number:')
num2=int(input())
sum=num1+num2
print('Do you want to add another number(y/n):')
ans=input()
while ans=='y':
    print('Enter another number:')
    num2=int(input())
    sum=sum+num2
    print('Do you want to add another number(y/n):')
    ans=input()

print('summary is:',sum)

#48*****************************************
print('#################################################################')
print('Enter your guest name:')
name_guest=input()
number_Gu=1
print(name_guest,'is invited to the party')
print('Do you want to invite some body else:(y/n)')
q=input()
while q=='y':
    number_Gu=number_Gu+1
    print('Enter your guest name:')
    name_guest=input()
    print(name_guest,'is invited to the party')
    print('Do you want to invite some body else:(y/n)')
    q=input()

print('number of guests:',number_Gu)

#49****************************************                
print('#################################################################')
compnum=50
score=0
n_guess=0
while compnum!=n_guess:
    print('Enter a number:')
    n_guess=int(input())
    if n_guess>compnum:
        print('Too high')
    elif n_guess<compnum:
        print('Too low')
    score=score+10
print('welldone your score is',score)    

print('#################################################################')
