# 1
# input = [5,5,3,1,2,2,1,3,5]
# list1 = {}

# for i in range(len(input)):
#     if input[i] not in list1 :
#         list1[input[i]] = 1
#     else :
#         list1[input[i]] += 1

# print(list1)

# list2 = list1.items()

# print(list2)

# freq = 0
# no = 0

# for i in list2 :
#     if i[1] > freq :
#         freq = i[1]
#         no = i[0]
#     print(i)
# print(no)

# 2 
# a1 = [2,3,5]
# a2 = [1,4,6]
# b = a1 + a2
# b.sort()
# print(b)

# 3
# a = [1,2,3,5,3,2,7,6]
# k = 3

# a.sort()

# print(a[-k])

# 4 (will only work for this test case (dont sort , intead use dict or something))
# a = [3,2,1,2,3,4,5,1]

# a.sort()
# i = 0

# while i < (len(a)-1) :
#     if a[i] != a[i+1] :
#         print(a[i])
#         i += 1
#     else :
#         i+=2

