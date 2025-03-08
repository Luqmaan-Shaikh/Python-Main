# 22 (IF)

# ch = int(input("Enter any No: "))

# if ch>0 :
#     print("positive")

# if ch<0 :
#     print("negative")

# if ch==0 :
#     print("zero")

# 23 

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
# d = int(input("Enter d: "))
# e = int(input("Enter e: "))

# if (a>b and a>c and a>d and a>e) :
#     print(a, "is Greatest")

# if (b>a and b>c and b>d and b>e) :
#     print(b, "is Greatest")

# if (c>a and c>b and c>d and c>e) :
#     print(c, "is Greatest")

# if (d>a and d>b and d>c and d>e) :
#     print(d, "is Greatest")

# if (e>a and e>b and e>c and e>d) :
#     print(e, "is Greatest")

#24 

# day = input("Enter Day: ")

# if day=='saturday' or day == 'SATURDAY' or day== 'sunday' or day== 'SUNDAY' :
#     print("Weekend")

# else :
#     print("Working Day")

# 25 

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))

# if b>a :
#     print("b is Greater than b")

# elif a==b :
#     print("a and b are Equal")

# else :
#     print("a is Greater than b")

# 26

# ch = ord(input("Enter any Character: "))
#ord function used to convert in ACII code

# print(ch)

# if (ch>=65 and ch<=91) :
#     print("Uppercase")

# elif (ch>=97 and ch<=122) :
#     print("Lowercase")

# elif (ch>=48 and ch<=57) :
#     print("Digit")

# else :
#     print("Special Symbol")

# 27 

# for i in range(10) :
#     print(i)

# for i in range(1,11) :
#     print(i)

# for i in range(1,11,2) :
#     print(i)

# for i in range(10,0,-1) :
#     print(i)

# for i in range(10,0,-3) :
#     print(i)

# for i in range(1,11) :
#     print(i*2)

# 28 

# for i in range(1,11) :
#     print(i, ' ', i*2, ' ', i*3, ' ', i*4, ' ', i*5, ' ', i*6, ' ', i*7, ' ', i*8, ' ', i*9, ' ', i*10)

# print()

# for i in range (1,11):
#     print(i*11, ' ', i*12, ' ', i*13, ' ', i*14, ' ', i*15, ' ', i*16, ' ', i*17, ' ', i*18, ' ', i*19, ' ', i*20)

# 29

# a = "shiwaleew"

# for i in a :
#     if i=='w':
#         print(i)

# for i in range (len(a)) :
#     if a[i]=='w':
#         print(i)

# 30 

# name = 'prashantjha'

# vow = 0
# cons = 0

# for i in name :
#     if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
#         vow+=1
#     else :
#         cons+=1

# print("vow = ", vow)
# print("cons = ", cons)

# 31 

# for i in range(1,6) :
#     if i == 4:
#         break
#     print(i)

# for i in range(1,6) :
#     if i == 4:
#         continue
#     print(i)

# 32 

# for i in range(1,6) :
#     if i == 3:
#         continue
#     print(i, " ", 6-i)

# for i , j in zip(range(1,6), range(5,0,-1)) :
#     if i==3 and j==3:
#         continue
#     print(i, " ", j)

# 33 

# p1 = int(input("Enter paper1 marks: "))
# p2 = int(input("Enter paper2 marks: "))
# p3 = int(input("Enter paper3 marks: "))
# p4 = int(input("Enter paper4 marks: "))
# p5 = int(input("Enter paper5 marks: "))

# if p1>40 and p2>40 and p3>40 and p4 >40 and p5 >40 :
#     print("Pass")
# else :
#     print("Fail")

# total = p1+p2+p3+p4+p5
# percentage = total/5.0

# print("Total= ", total)
# print("Percentage= ", percentage)

# gender = input("Enter Gender: ")

# if percentage >= 65 and gender == "male" :
#     print("can apply to MNC's")

# if percentage >= 70 and gender == "female" :
#     print("can apply to MNC's")

