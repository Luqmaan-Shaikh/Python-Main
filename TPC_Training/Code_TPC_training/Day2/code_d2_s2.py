# 29 

# input = [3,-2,7,-1,0,5,4]

# pos = 0

# neg = 0

# for i in range(len(input)) :
#     if input[i] <= 0 :
#         neg += 1
#     elif input[i] > 0 :
#         pos += 1
# print(pos)
# print(neg)

# OR

# input = [3,-2,7,-1,0,5,4]

# pos = 0
# neg = 0

# for i in input :
#     if i > 0 :
#         pos += 1
#     else :
#         neg += 1
# print(pos)
# print(neg)

# 30 (Nested loop)

# for i in range(1,4) : #outer loop -> row
#     for j in range(1,4) : #inner loop -> col
#         print(i , end = " ")
#     print()
    
# 31

#try

# data = int(input("Enter: "))
# data = 1222


# 32

# n = int(input("enter: "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end=" ")
#     print()

# 33 

# n = int(input("enter: "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end=" ")
#     print()

# 34 

# n = int(input("enter: "))

# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+j),end=" ")
#     print()

# 35 (palindrome)

# N = input("enter : ")

# if N == N[::-1]:
#     print("palindrome")
# else :
#     print("not palindrome")

# 36 (Anagram)

# n = input("enter 1 : ")
# m = input("enter 2 : ")

# list1 = list(n)
# list2 = list(m)

# print(list1)
# print(list2)

# list1.sort()
# list2.sort()

# if list1 == list2 :
#     print("Anagram")
# else :
#     print("not a anagram")

# 37 (panagram)

# s = "The quick brown fox jumps over the lazy dog"
# flag=True

# for i in range(1,27) :
#     if chr(64+i) not in s and chr(96+i) not in s :
#         print("not in panagram")
#         flag = False 
#         break

# if flag == True :
#     print("panagram")

# 38 

# s = "programming"
# new_s = ''
# for i in s:
#     if i not in new_s :
#         new_s+=i
# print(new_s)       

# OR 

# a = "abababab"

# print(a.count("ab"))

# 39 

