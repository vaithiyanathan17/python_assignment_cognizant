# #1. max of three numbers
# def maximum(a,b,c):
#     return max(a,b,c) 
# print(maximum(3,90,25))

# #2. sum all the numbers in a list
# def list_sum(args):
#     sum=0
#     for i in args:
#         sum+=i
#     return sum
# print(list_sum([8, 2, 3, 0, 7]))

# #3. multipy all the numbers in al list
# def list_multiply(args):
#     mul=1
#     for i in args:
#         mul=mul*i
#     return mul

# print(list_multiply([8, 2, 3, -1, 7]))

# #4. program to reverse a string
# def reverse(str):
#     return str[::-1]
# print(reverse("1234abcd"))

# #5. function to calculate the factorial of a number
# def factorial(num):
#     fact=1
#     for i in range(num,0,-1):
#         fact*=i
#     return fact
# print(factorial(5))        

# #6. Number of upper and lower case letters
# def upper_and_lower(str):
#     upper = 0
#     lower = 0
#     str=str.replace(" ","")
#     for i in str:
#         if  i.isupper():
#             upper+=1
#         else:
#             lower+=1
#     return [upper,lower]
# print(upper_and_lower("The quick Brow Fox"))

# #7. prime number or not
# def prime(num):
#     str=""
#     if(num>1):
#         for i in range(2,num):
#             if(i*i<=num):
#                 if(num%i != 0):
#                     str="prime"
#                 else:
#                     str="not prime"
#     else:
#         str="enter value greater than 1"
#     return str

# print(prime(20))


# #8. sort hipen-seperated-string
# def hiphen_seperated(str):
#     splitted_str = str.split('-')
#     splitted_str.sort()
#     result_str='-'.join(splitted_str)
#     return result_str
# print(hiphen_seperated("green-red-yellow-black-white"))

# #9. lambda function adds 15 to given number
# #   lambda function that multiplies x and y
# add = lambda x:x+15
# multiply = lambda x,y:x*y
# print(add(10))
# print(multiply(6,8))

# #10. even and odd segregation using lambda and filter
# numbers=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = list(filter(lambda x: x%2==0,numbers))
# odd = list(filter(lambda x:x%2!=0,numbers))
# print(even)
# print(odd)

# #11. second lowest using lambda

# name_grade=[]
# n = int(input("Enter number of student"))
# for i in range(n):
#     name = input("name")
#     mark= int(input("mark"))
#     name_grade.append([name,mark])
# sorting = sorted(name_grade , key = lambda x:x[1])
# print(sorting[1])

# #12. add three list using map and lambda

# x=[9,10,99]
# y=[100,-12,3]
# z=[-69,32,-14]
# three_list = list(map(lambda x,y,z : x+y+z,x,y,z ))
# print(three_list)

# #13. conver all char to upper and lower using map and no duplicate char

# string = "hello"
# result_lower = list(map(lambda x : x.lower(),string))
# result_upper = list(map(lambda x : x.upper(),string))
# print(set(result_lower),set(result_upper))

# #File Handling

# # 1. read a file line by line and store it into a list

# with open('sample_text.txt','r') as filename:
#     read_list = filename.readlines()
#     print(read_list)

# #2. find the longest words
# with open('sample_text.txt','r') as filename:
#     read_list = filename.read().split(" ")
#     max_len=len(max(read_list,key=len))
#     for i in read_list:
#         if(max_len==len(i)):
#             print(i)

# #3. number of lines in a text file

# with open("sample_text.txt",'r') as f:
#     for i, l in enumerate(f):
#         pass
#     print(i+1)

# #4. copy file 
# from shutil import copyfile
# copyfile('sample_text.txt', 'sample_copy.txt')

# #5. number of words in a text file
# with open('sample_text.txt','r') as filename:
#     read_list = filename.read()
#     read_list.replace("."," ")
#     print(read_list)
# print(len(read_list.split(" ")))

