print('----------------------')
t1=('Iran','Canada','Japan','Turkey','Korea')
print(t1)
print('Pleas enter one of the countries that shown:')
c=input()
print(t1.index(c))

#70*******************
print('Pleas enter a number :(0 to 4)')
num=int(input())
print(t1[num])
#71*****************
print('----------------------')
list_sport=['badminton','handball']
print(list_sport)
print('What your favorite sport?')
fav_sport=input()
list_sport.append(fav_sport)
print(list_sport)
#72****************
print('----------------------')
list_color=['red','blue','pink','yellow','white','green','purpul','black','brown','dark blue']
print("Enter a number between 0-4 for start:")
start=int(input())
print("Enter a number between 5-9 for end:")
end=int(input())
print(list_color[start:end])
#73**************************
print('----------------------')
food={}
print('Enter four of your favorit food?')
for i in range(1,5):
    food[i]=input()

for a,b in food.items():
    print(a,b)

print('Which you want get rid of?')
select=input()

for x in range(1,5):
    if food[x]==select :
       food.pop(x)

for f,g in food.items():
    print(f,g)

#74***************************
print('----------------------')
tag=True
list1=[100,200,300,400]
for i in range(4):
	print (list1[i],'\n')
	
print('Enter a 3digit number:')
num=int(input())

for j in range(4):
    if list1[j]==num:
        print('number placed in:',j)
        tag=False
    if tag==True and j==4 :
         print('That is not the list')
#75**************************
print('----------------------')
print('please enter three people name that invite to a party')
print('Enter name first:')
p1=input()
print('Enter name second:')
p2=input()
print('Enter name third:')
p3=input()
list_guest=[p1,p2,p3]
counter=3
ans=''
print('Do you want to add another person(y/n):')
ans=input()
while  ans=='y':
       print('enter new guest name:')
       name=input()
       list_guest.append(name)
       print('Do you want to add another person(y/n):')
       ans=input()
       counter=+1
for i in list_guest[-1]:
    print(i,'         ',list_guest[i],'\n')
#77******************************
print('Do you want to remove any people(y/n):')
ans1=input()
while ans1=='y':
      if ans1=='y' :
         print ('which one :')
         rm=input()
         list_guest.remove(rm)
         print('Do you want to remove any people(y/n):')
         ans1=input()
for j in list_guest[-1]:
    print(j,'           ',list_guest[j])

    
    
             

    






        










