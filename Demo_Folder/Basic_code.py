# print("\nPrint:-")

# print("Hello world")
# print("Hello world","Aniket")
# print(56)

# print("75")         # Numbers can be written in ("") or ( )
#                     # between ("") same to same print
#                     # between ( ) operation will performe

# print(67+7)
# print("67+5")

# print(4-9)
# print("4-9")

# print(4*9)
# print("4*9")
#                        # "" , it's denote string
# print(9/5)
# print("9/5")
#                       # Variable:- variable name can't write between "", in 'print' statement 
# name="Aniket"
# age="20"
# a=None
# value="23.5"
# print("My name is:",name)
# print("My name age is:",age)
# print(value)

# print(type(name))            # 'print(type(variable name))' define variable type
# print(type(a))

# print("\nArathmatic Operation:-")

# a=3
# b=5
# sum=a+b
# print(sum)
# print(a+b)

# print("\nAssigenment Operation:-")

# a=8
# a**=3
# print(a)

# print("\nLogical operation:-")

# a=True
# print(not a)
# b=False
# print(not b)
# print("Answer:",(a and b))
# print("Answer:",(a or b))

# print("\nInput:-")
# # val=input("Enter your age:")         # Input's data-type will generaly "String".
# # print("Your age is:",val)            # Otherwise maintaion the datatype.Like:- int(input())
# # print(type(val))             

# print("\nString & it's operations:-")

# str1="Brainware"
# str2="Aniket.Ghosh"
# str3="aniket\nGhosh"               # "\n" use for seperate a line
# str4="Aniket\tGhosh"               # "\t" use for tab(give space)\
# str5=" is my mother land"
# print(str1[::-1])                   # Add two string
# print(str2)
# print(str3)
# print(str4)
# print(len(str1+str5))             # Give the lenght of string
# print(str1[3])  
                             # Show the character on the given index (Which is start from '0')
# s=str(input("Enter your string:"))
# checked=''
# for ch in s:
#      if ch not in checked:         #Count number of charecter
#         t=s.count(ch)
#         print(f'Count of {ch} is:',t)
#         checked=checked+ch

# print(str4[2:8])                  # Slice(Give a specific part) of a string
# print(str4[:8])                   # If staring index blank,automatic set first index 
# print(str3[2:])                   # If last index is blank,automatic set last index.It also write "len(str)"
# print(str4[-5:-2])                # Using negative index,also show character on position(Start from'-1')

# print("\nFunction of string:-")

# print(str2.endswith('sh'))           # Cheack last part of a string end by given word.It give answers in (True/False)
# print(str1.capitalize())             # Capitalize the 1st element of the string
# print(str2.replace("h","ekp"))       # Replace old data to new data
# print(str2.find("h"))                # Cheack the'Word' is existes or not.If exists,show it's where it first start
# print(str2.count("h"))               # Cheack how much time 'Word' exists
