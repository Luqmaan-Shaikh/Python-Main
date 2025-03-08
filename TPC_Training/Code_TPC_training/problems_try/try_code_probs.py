# 1. REVERSING A STRING

# str = input()

# str = str[::-1]

# print(str)

# 2. Sum of Digits

# a = int(input())

# sum = 0 

# for i in str(a) :
#     sum += int(i)

# print(sum)

#OR

# a = input()

# sum = 0 

# for i in a :
#     sum += int(i)

# print(sum)

#OR

# a = int(input())

# sum = 0

# while a > 0 :
#     sum = sum + (a % 10)
#     a = a//10

# print(sum)

# 3. Smallest Integer

# arr = eval(input())

# arr.sort()

# if len(arr) == 0 :
#     print("-1")
# else :
#     print(arr[0])

# OR 

# arr = eval(input())   # as we used eval  : input method is -> [3,2,-1,5]

# smallest = arr[0]

# for num in arr :
#     if num < smallest :
#         smallest = num
# print(smallest)

#OR

# arr = input().split()  # as we did not use eval  : input method is -> 3 2 -1 5

# arr = [int(i) for i in arr]   # list comprehension , to convert each element of the list into an integer.

# smallest = arr[0]

# for num in arr :
#     if num < smallest :
#         smallest = num
# print(smallest)

# 4.Largest Integer

# arr = eval(input())

# arr.sort()

# if len(arr) == 0 :
#     print("-1")
# else :
#     print(arr[-1])

#OR

# arr = input().split()

# arr = [int(i) for i in arr]

# largest = arr[0]

# for num in arr :
#     if num > largest :
#         largest = num

# print(largest)

# 5. Count Vowels

# s2 = input()

# vowels = 0

# s2 = s2.lower()

# for i in s2 :
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
#         vowels += 1

# print(vowels)

# OR (No Need to do this)

# s2 = input()

# vowels = 0

# s2 = s2.lower()

# s2.split()

# for i in s2 :
#     if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
#         vowels += 1

# print(vowels)

# 6. Prime No

# n = int(input())

# if a <=1 :
#     print("not a prime no")
# else :
#     for i in range(2,n) :
#         if n % i == 0 :
#             print ("not a prime no")
#             break
#     else :
#         print("prime no")

# 7. Palimdrome or not ?

# s3 = input()

# if s3[:] == s3[::-1]:
#     print("palindrome")
# else :
#     print("not a palindrome")

# 8. Word in String 

# s4 = input()

# s4 = s4.split()

# print(len(s4))

# 9. Sum, Avg, Prod of list of nos

# l1 = eval(input())

# l1 = [int(i) for i in l1]

# sum = 0
# prod = 1

# for i in range(0, len(l1)) :
#     sum = sum + l1[i]
#     prod = prod * l1[i]

# print(sum)

# avg = sum/(len(l1))

# print(avg)

# print(prod)

# 10. Anagram

# s1 = input()
# s2 = input()

# l1 = list(s1)
# l2 = list(s2)

# l1.sort()
# l2.sort()

# print(l1,l2)

#OR

# s = eval(input())

# s1 , s2 = s

# freq1 = {}
# freq2 = {}

# for char in s1 :
#     freq1[char] = freq1.get(char, 0) + 1

# for char in s2 :
#     freq2[char] = freq2.get(char, 0) + 1

# if freq1 == freq2 :
#     print("anagram")
# else :
#     print("not anagtram")

'''11. U have a sequence of number
U have to calculate difference between the number on batch wise fashion
And sum it
Q: 1,3,5,2,4,1,3,9
A: 14

Diff between 1 and 3 is 2
5 and 2 is 3
4 and 1 is 3
3 and 9 is 6
Summing 2+3+3+6 gives us 14'''

# l = eval(input())

# diff = 0

# sum = 0 

# for i in range(0, len(l), 2) :
#     diff = abs(l[i] - l[i+1])
#     sum = sum + diff
# print(sum)

# 12. Remove Spaces from String

# s = input()

# replaced = "".join(map(lambda x : "" if x == " " else x,s))

# print(replaced)

# 13. Multiply all no in a list

# l = eval(input())

# prod = 1

# for i in l :
#     prod = prod * i

# print(prod)

# 