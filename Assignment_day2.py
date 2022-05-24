#1. pattern
n = int(input("number for pattern: "))
for i in range(1,n+1):
    print(f'{i}' *i)


#2. triangle
side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))
if(side1==side2==side3):
    print("Equiletral triangle")
elif(side1==side2 or side2==side3 or side1==side3):
    print("Isoceles triangle")
else:
    print("Scalene triangle")

#3. next day 17/feb/2001
calendar={'jan':31,'feb':28,'mar':31,'apr':30,'may':31,'june':30,'july':30,'aug':31,'sept':30,'oct':31,'nov':30,'dec':31}
date=list(map(str,input("Enter the date: ").split("/")))
calendar_list=list(calendar)
if(int(date[0])==calendar[date[1]]):
    list_index = calendar_list.index(date[1])
    if(list_index==len(calendar_list)-1):
        print(f"01/jan/{int(date[2])+1}")
    else:
        list_index+=1
        print(f"01/{calendar_list[list_index]}/{date[2]}")
elif(int(date[0])<calendar[date[1]]):
    print(f"{int(date[0])+1}/{date[1]}/{date[2]}")

#4. calculate number of digits and letters

string = "bjankpma-4i9qy79iankan9uaeh7"
alpha=0
number=0
other=0
for i in string:
    if i.isalpha():
        alpha+=1
    elif i.isnumeric():
        number+=1
    else:
        other+=1
print([alpha,number,other])

#5 alphabet or vowel

char = input("enter a char: ")
vowels=['a','e','i','o','u']
if char in vowels:
    print("vowel")
else:
    print("consonant")

#6 temperature to celsius farenheit

c_or_f = input("Choose celsius or farenheit: ")
temperature = int(input("Give temperature value: "))
if(c_or_f=="celsius"):
    c = (temperature-32)*(5/9)
    print(c)
else:
    f = (temperature*(9/5))+32
    print(f)

#7 pattern using nested for loop
'''
    *
    **
    ***
    ****
    *****
    ****
    ***
    **
    *
'''
n = int(input("Enter the pyramid size: "))

for i in range(n):
    for j in range(i):
        print("*" , end="")
    print("")
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

#8. half pyramid
n = int(input("Enter the pyramid size: "))
for i in range(n,0,-1):
    for j in range(i):
        print("*",end="")
    print("")

# 9. even and odd from the series of number

numbers = tuple(i for i in range(1,10))
even=0
odd=0
for i in numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even)
print(odd)

# #10. sum of three numbers
a,b,c=input("Enter the values").split(",")
result=0
if(a==b or b==c or a==c):
    print(result)
else:
    result=int(a)+int(b)+int(c)
    print(result) 


#11. income tax
income = int(input("Enter the amount"))
first_pay=income-10000
second_pay=first_pay-10000
tax=1000+(second_pay*0.2)
print(tax)  

#12. extract each digit

n= 7536
print(n%10)
reverse = 0
while(n != 0):
    remainder = n%10
    reverse = reverse*10+remainder
    n=n//10
print(reverse)

# 13. Fibonacci

n = int(input("Enter the fibonacci value"))
a=0
b=1
fib=[a,b]
for i in range(n-2):
    c=a+b
    a=b
    b=c
    fib.append(c)
print(fib)

#14. early multiplication

multiplier=int(input("multiplier: "))
multiplicand=int(input("multiplicand: "))
result=0
for i in range(multiplier):
    result+=multiplicand
print(result)

#15. multiplication table
n = int(input("input multiplier"))
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")

for i in range(1,11):
    print(f"{n} X {i} = {n*i}")

#16. palindrome or not
string = input("Enter the string: ")
if(string==string[::-1]):
    print("palindrome")
else:
    print("not palindrome")

#17. guess the number
import random
random_number= int(random.randint(1,10))
guess = int(input("Enter your guess: "))
guessed=True
while(guessed):
    if(guess==random_number):
        print("Nice! You got it")
        guessed=False
    elif(guess>random_number):
        print("please guess lower")
        guess = int(input("Enter your guess: "))
    else:
        print("please guess higher")
        guess = int(input("Enter your guess: "))

#18. odd from list1 and even from list2

list1 =  [10, 20, 23, 11, 17]
list2 = [13, 43, 24, 36, 12]
length=len(list1)-1
result=[]
print(length)
while(length >= 0):
    print(length)
    if( list1[length] % 2 != 0 and list2[length]%2==0):
        result.append(list1[length])
        result.append(list2[length])
    length-=1
print(result)

# 19. stop the sequence if 237 

numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345,399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217,815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717,958,743, 527]
#numbers=[224,127,237,198,998,192]
for i in range(len(numbers)):
    if numbers[i] != 237:
        if numbers[i]%2==0:
            print(numbers[i])
    else:
        quit()

#20. frequency of words

from enum import unique


string="Torvalds described himself as a nerd during his interview with Linux Journal. It is rare to hear of a child who loves going to school, but Torvalds belongs to that rare breed. As a child of divorced parents, maybe it was his way of coping with divorce that led him to be absorbed in the world of computers so he could spend time alone."
str_list=string.split()
unique=set(str_list)
for uniq in unique:
    print(uniq,': ',str_list.count(uniq))

#21. divisible by 5 & greater than 150

list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for i in range(len(list1)):
    if list1[i] <= 150:
        if list1[i]%5==0:
            print(list1[i])
    else:
        quit()

#22. no of digits in number
number = 75869
print(len(str(number)))

#23. Reverse the list using for loop
list1 = [10, 20, 30, 40, 50]
rev_lst=[]
for i in range(len(list1)-1,-1,-1):
    rev_lst.append(list1[i])
print(rev_lst)

#24. prime number within a range
start, end = 25, 50
primes = []

for i in range(start, end + 1):
    flag = 0

    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue

    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break

    if flag == 0:
        primes.append(i)
        
print(primes)

#25. factorial of a num

num = int(input("Enter the number: "))
result = 1
for i in range(num,0,-1):
    result*=i
print(result)
