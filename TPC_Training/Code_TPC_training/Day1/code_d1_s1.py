# 1

# a=10
# pi=3.14
# name='prashant'
# result=True

# print(type(a))
# print(type(pi))
# print(type(name))
# print(type(result))

# 2

# print(id(a))
# print(id(pi))
# print(id(name))
# print(id(result))

# 3

# math = 50
# physics=50
# chemistry=50
# eng=40
# hindi=60

# print(id(math))
# print(id(physics))
# print(id(chemistry))
# print(id(eng))
# print(id(hindi))

# 4

# math=39
# math=49

# print(math)
# print(id(math))

# 5 

# val1 = input()
# val2 = input()

# temp = val1
# val1 = val2
# val2 = temp

# print('val1 = ' , val1)
# print('val2 = ' , val2)

# 6 

# a = int (input())
# b = int (input())

# a = a+b
# b = a-b
# a = a-b

# print('a = ' , a)
# print('b = ' , b)

# 7 

# p1 = float(input())
# p2 = float(input())
# p3 = float(input())

# sum = p1+p2+p3
# avg = (p1+p2+p3)/3.0

# print('sum = ' , sum)
# print('avg = ' , avg)

# 8 

# print(2+2)
# print('2' + '3')

# a = (input("Enter first value: "))
# b = (input("Enter second value: "))

# print(a+b)

# 9 

# a = int(input("Enter first value: "))
# b = int(input("Enter second value: "))

# print(a+b)

# 10 (INT -Type Cast)

# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int("4"))

# print(int("prashant")) - NO 
# print(int(10+5j)) - NO
# print(int("4.22")) - NO

# 11 (FLOAT - Type Cast)

# print(float(3))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("4"))

# print(float(10+5j)) - NO
# print(float("prashant")) -NO

# 12 (Complex - Type Cast)

# print(complex(3))
# print(complex(12.5))
# print(complex(True))
# print(complex(False))
# print(complex("5"))
# print(complex("5.6"))
# print(complex(5,-3))
# print(complex(True,False))

# print(complex("prashant")) - NO

# 13 (BOOLEAN - Type Cast)

# print(bool(0))
# print(bool(15))
# print(bool(3.14))
# print(bool(0.0))
# print(bool(1+2j))
# print(bool(0+0j))
# print(bool(-1))
# print(bool(False))
# print(bool(True))
# print(bool(""))
# print(bool("prashant"))

# 14 (identity op)

# x = 10
# y = 10

# print(x is y)
# print(x is not y)

# 15 (identity op)

# x = 15
# y = 10

# print(x is y)
# print(x is not y)

# 16 (membership op)

# a = "help4code"

# print('e' in a)
# print('f' not in a)

# print('e' not in a)
# print('f' in a)

# 17 (String Slicing)

# name = "prashantjha"

# print(name[0])
# print(name[1])
# print(name[-1])
# print(name[0:5])
# print(name[1:])
# print(name[:5])
# print(name[:])
# print(name[1:8:2])
# print(name[::-1])

# print(name[15]) - Error : IndexError: string index out of range

# 18 

# s = "python is object oriented programming language"

# print(s.find("python"))
# print(s.find("programming"))
# print(s.find("java"))

# 19 

# s = "prashant" , "ashish" , "sandip"
# m = ' '.join(s)
# print(m)

# 20 

# s = "Python are High level programming Language"

# print(s.lower())
# print(s.upper())
# print(s.swapcase())
# print(s.title())
# print(s.capitalize())

# 21 

# name = "prashant"
# sal = 5000
# age = 28

# print("{} sal is {} age is {}".format(name,sal,age))
# print("{0} sal is {1} age is {2}".format(name,sal,age))
# print("{x} sal is {y} age is {z}".format(x=name, y=sal, z=age))

# A=1
# print(f"{A} is a good boy")