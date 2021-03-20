a=int(input('enter a number'))

if a%3==0 and a%5==0:
    print('consultadd-python training')
elif a%3==0:
    print('consultadd')
elif a%5==0:
    print('python training')


#ans2
print("1. Addition") 
print("2. Subtraction") 
print("3. Division") 
print("4. Multiplication") 
print("5. Average") 
num = int(input("Enter your choice: ")) 
while num<1 or num>5: 
 num=int(input("Invalid choice. Try again: ")) 
first = int(input("Enter first number: ")) 
second = int(input("Enter second number: ")) 
result = 0 
if num==1: 
 result = first+second 
 print(result)
elif num==2: 
 result = first-second 
 print(result)
elif num==3: 
 result = first/second 
 print(result)
elif num==4: 
 result = first*second 
 print(result)
else: 
 first1 = int(input("Enter third number: ")) 
 second1 = int(input("Enter fourth number: ")) 
 result = (first+first1+second+second1)/4 
 print(result)
 if result<0: 
    print("negative") 
 
#ans3
a=10
b=20
c = 30  
avg = (a+b+c)/3 
print("avg = ", avg) 
if avg>a and avg>b and avg>c: 
 print("avg is higher than a, b, c") 
elif avg>a and avg>b: 
 print("avg is higher than a, b") 
elif avg>b and avg>c: 
 print("avg is higher than b, c") 
elif avg>a and avg>c: 
 print("avg is higher than a, c") 
elif avg>a: 
 print("avg is just higher than a") 
elif avg>b: 
 print("avg is just higher than b") 
elif avg>c: 
 print("avg is just higher than c")


 #ans4
while True:
    try:
        user_input = int(input("Enter an integer number:"))
        if user_input < 0:
            print("It's over")
            break
        else:
            print("Good Going! Enter negative number to exit else continue.")
    except ValueError:
        pass

  
 
 #ans5
nl=[]
for x in range(2000, 3200):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))

# ans6
# a = 123
# for i in a:
#     print(i)


i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
    else:
        print("error")
        count = 0



while True:
    print(count)
    count += 1
    if count >= 5:
        break


# ans7
for x in range(6):
    if (x == 3 or x==6):
        continue
print(x,end=' ')


# ans8
s = input("Input a string")
d=l=0
for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("Letters", l)
print("Digits", d)

# ans9
import random
target_num, guess_num = random.randint(1, 10), 0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 and 10 until you get it right : '))
print('Well guessed!')


# ans10
import random
guess = 57
counter = 0
while counter < 5:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        print("Good guess!")
        guess = random.randint(1, 100)
    else:
        print("Try again!")
    counter += 1
print("Game over!")


# ans11
import random
guess = 57
counter = 0
while counter < 5:
    user_input = int(input("Guess the lucky number: "))
    if user_input == guess:
        print("Good guess!")
        break
    else:
        print("Try again!")
    counter += 1
print("Sorry but that was not very successful!")