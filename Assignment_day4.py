#File Handling

# 1. read a file line by line and store it into a list

with open('sample_text.txt','r') as filename:
    read_list = filename.readlines()
    print(read_list)

#2. find the longest words
with open('sample_text.txt','r') as filename:
    read_list = filename.read().split(" ")
    max_len=len(max(read_list,key=len))
    for i in read_list:
        if(max_len==len(i)):
            print(i)

#3. number of lines in a text file

with open("sample_text.txt",'r') as f:
    for i, l in enumerate(f):
        pass
    print(i+1)

#4. copy file 
from shutil import copyfile
copyfile('sample_text.txt', 'sample_copy.txt')

#5. number of words in a text file
with open('sample_text.txt','r') as filename:
    read_list = filename.read()
    read_list.replace("."," ")
    print(read_list)
print(len(read_list.split(" ")))