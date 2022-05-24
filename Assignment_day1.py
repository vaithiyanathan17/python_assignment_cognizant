#1.multi line string
Rhymes = '''Twinkle, twinkle, little star,
	How I wonder what you are! 
		Up above the world so high,   		
		Like a diamond in the sky. 
Twinkle, twinkle, little star, 
	How I wonder what you are'''


print(Rhymes)

#2.simple print

statement = "My Name Is James"
changed=statement.replace(" ","**")
print(changed)

print("python's course for beginner")
print("python's course for \"beginner\"")

#3.string input and assignment

print("Enter a string: ")
string = input()
splitter=string.split(" ")
print(splitter)
for i in range(len(splitter)):
    print(f"str{i+1}={splitter[i]}")

#4. compute the area of the circle with the given radius
pi = 3.14
print("Enter the radius value: ")
r = float(input())
print(pi*r*r)

#5. get the first and lastname print them in reverse

print("Enter your First Name : ")
first_name = input()
print("Enter your Last Name : ")
last_name = input()
print(f"Hello {last_name} {first_name}")

#6. comma seperated numbers from users and generate a list and tuple
print("enter the comma seperated elements")
data = list(map(int,input().split(",")))
print(data)
print(tuple(data))

#7. enter the filename with extension and print the extension
print("Enter the filename")
filename = input()
index=filename.index(".")
print(filename[index+1:])

#8. first and last element from the list

color_list = ["Red","Green","White" ,"Black"]

print(f"first element = {color_list[0]}")
print(f"last element = {color_list[-1]}")

#9. date format printing - tuple
exam_st_date = (11, 12, 2014)
print(f"The examination will start from : {exam_st_date[0]} / {exam_st_date[1]} / {exam_st_date[2]}")


#10. compute n+nn+nnn
print("Enter the value to calc n+nn+nnn")
n = int(input())
print(n+(n*n)+(n*n*n))

#11. sort without loop and conditionals

arr = [5,18,1]
arr.sort()
print(arr)

#12. future value given principal,interest,year
principal=10000
interest = 3.5
years = 7

future_value = principal*(1+(interest/100))**years
print(f"{future_value:.2f}")

#13.height in ft and inches to centimeters

print("choose feet or inches")
measure = input()
cm=0
if(measure == "feet"):
    print("input feet value")
    feet = float(input())
    print(feet*30.48)
else:
    print("Enter the inch value")
    inch = float(input())
    print(inch*2.54)