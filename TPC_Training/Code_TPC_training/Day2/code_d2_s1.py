# 1

# mylist = ["prashant", "Ashish", "komal", "ankush", "Ashish", 77, "sandip", 60.52, "prashant"]

# print(mylist)

# print(type(mylist))
# print(mylist[0])
# print(mylist[1])
# print(mylist[2])
# print(mylist[-1])
# print(mylist[2:5])
# print(mylist[:5])
# print(mylist[1:])
# print(mylist[1:8:2])

# 2

# mylist[0] = "Akshay"
# print(mylist)

# 3

# mylist.append('harsh')
# mylist.append(77)
# print(mylist)

# 4

# mylist.insert(2,'RAIT')
# print(mylist)

# 5 

# mylist.remove("sandip")
# print(mylist)

# 6

# newlist = mylist.copy() #cloning
# print(newlist)

# 7

# mylist = [["Luqmaan ", "Shaikh"], [77, 79], [2000 , "yyy"]]

# print("Ex of Multidimensional List")
# print(mylist)

# print(mylist[row][col])

# print(mylist[0][0])
# print(mylist[0][1])
# print(mylist[1][0])
# print(mylist[2][0])
# print(mylist[2][1])

# 8 

# list1 =["Luqmaan", "Shaikh"]
# print(list1*2)

# list2 = [50, 25.50]
# print(list1 + list2)

# 9

# list3 = [50,25.50,'Luqmaan']

# print(list3)
# del list3[2]
# print(list3)

# del list3
# print(list3)

# 10

# list4 = [50,25.50,'Luqmaan']

# list4.clear()
# print(list4)

# 11

# name = "Luqmaan"

# print(name)

# myname = list(name)

# print(myname)

# 12

# mylist = [10,20,30,40]

# mylist.reverse()

# print(mylist)

# 13 (Sorting)

''' default sorting order for number is ascending order
default sorting order for number is ascending order
list congtains homogenious data otherwise we get typeerror
pythin2 first sort no. then string follow '''

# mylist = [44,22,77,0,9,88]

# mylist.sort()
# print(mylist)

# mylist.sort(reverse=True)
# print(mylist)

# 14 (Alising)

''' means assigning one varibale reference to another '''

# mylist = [44,22,77,0,9,98]

# newlist = mylist
# print(id(mylist))
# print(id(newlist))

# print(mylist)
# print(newlist)

# mylist[0] = 89

# print(mylist)
# print(newlist)

# 15 

# mylist = [44,22,77,0,9,98]

# for i in mylist :
#     print(i)

# for i in mylist :
#     print(i, end=" ")

# 16 

# container = [2,1,4,5,5,4,4,1,1]

# count = 0
# even = 0
# odd = 0

# for i in container :
#     if i==4 :
#         count+=1

#     elif i==2 :
#         even+=1

#     elif i==5 :
#         odd+=1

# print(count-even)
# print(count-odd)

# 17 

# data = [2,1,4,5,5,4,4,1,1]

# max = min = data[0]

# data_len=9
# for i in range(len(data)) :
#     if data[i] > max :
#         max = data[i]

#     elif data[i] < min :
#         min = data[i] 

# print("max = ", max)
# print("min = ", min)

# 18 

# mylist = [0,1,0,3,12]
# N = len(mylist)
# for i in range(N) :
#     if mylist[i] == 0 :
#         mylist.remove(0)
#         mylist.append(0)

# print(mylist)

# OR

# mylist = [0,1,0,3,12]
# N = len(mylist)
# for i in range(N) :
#     if mylist[i] == 0 :
#         mylist.remove(mylist[i])
#         mylist.append(0)

# print(mylist)

# 19 

# try this

# data = [3,2,1,5,6,4]

# k = 0
# max = min = data[0]

# for i in range(len(data)) :
#     if data[i] > max :
#         max = data[i]

#     elif data[i] < min :
#         min = data[i] 

# print("max = ", max)
# print("min = ", min)

# OR 

# data = [3,2,1,5,6,4]

# k = int(input("Enter k: " ))

# data.sort(reverse=True)

# print(data[k-1])

# OR 

# data = [3,2,1,5,6,4]

# k = int(input("Enter k: " ))

# data.sort()

# print(data[-k])

# 20

# mycart = [10,20,200,300,800,60,700]

# for i in mycart :
#     if i > 400 :
#         print("This is my Purchased cart item: ")
#         continue
#     print(i)

# 21 (using else block)

# mycart = [10,20,200,300,800,60,700]

# for i in mycart :
#     if i > 400 :
#         print("This is my Purchased cart item: ")
#         continue
#     print(i)
# else :
#     print("You have purchased everything")

# 22 

# rollno = [3,5,7,1,11,4,5,2]

# for x in rollno :
#     if x==2 or x==4 or x==6 or x==8 or x==10 :
#         print("Even no found is: ", x)
#         break

# 23

# print("luqmaanshaikh23".isalnum())
# print("luqmaanshaikh".isalnum())
# print("luqmaanshaikh".isalpha())
# print("luqmaanshaikh23".isalpha())
# print("23".isalnum())
# print("23".isdigit())
# print("23f".isdigit())
# print("luqmaanshaikh".islower())
# print("".islower())
# print("LUQMAANSHAIKH".isupper())
# print("My Name I Luqmaan".istitle())
# print("".istitle())
# print("My Name Is Luqmaan".isspace())
# print("        ".isspace())

# 24 

# try it

# data = input("Enter something: ")

# print(data.isalnum())

# 25 

# n = [1,2,3,5,5,5,1,2,4,4,6,6,6]

# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
# print(n.count(5))
# print(n.count(6))
# print(n.count(7))

# 26 

# data = [1,1,0,1,1,1,0,1,1,1,1, 0, 1]

# consec_count = []
# count = 0

# for i in data :
#     if i==1 :
#         count+=1
#     else :
#         consec_count.append(count)
#         count = 0

# consec_count.append(count)

# print(max(consec_count))

# 27 

# a = [1,2,3,4]
# b = [3,4,5,6]

# for i in range(len(a)) :
#     if a[i] in b :
#         print(a[i])

# OR 

# a = [1,2,3,4]
# b = [3,4,5,6]

# c = []

# for i in range(len(a)) :
#     if a[i] in b :
#         c.append(a[i])

# print(c)
        
# 28 

# mylist = [1,2,3,2,1,4,5]

# for i in mylist : 
#     if mylist.count(3) == 1 :
#         print(i)
#         break