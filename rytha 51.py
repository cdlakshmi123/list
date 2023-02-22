# geekCodes = [1, 2, 3, 4]
# geekCodes.append([5,6,7,8])
# print(geekCodes)

# qstn5 2

check1 = ['Learn', 'Quiz', 'Practice', 'Contribute']
check2 = check1
check3 = check1[:]
 
check2[0] = 'Code'
check3[1] = 'Mcq'
 
count = 0
for c in (check1, check2, check3):
    if c[0] == 'Code':
        count += 1
    if c[1] == 'Mcq':
        count += 10
 
print (count)

# qstn53
# list1 = range(100, 110)
# print (list1.index(105))

# qstn54
# list1 = [1, 2, 3, 4, 5]
# list2 = list1
 
# list2[0] = 0; 
# print( list1)

# qstn56
# List1 = [1998, 2002]
# List2 = [2014, 2016]
# print ((List1 + List2)*2)
 

# list = [1, 2, 3, None, (1, 2, 3, 4, 5), ['Geeks', 'for', 'Geeks']]
# print(len(list))
 
# print(list( range(4, 30, 2)))
 

# for i in range(4,31):
#     if i%2 == 0:
#         print(i, end=' ')
 
# a=[4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
 
# for i in a:
#     if i%2==0:
#         print(i, end=' ')
 
# Index=int(input("num"))
# n=0
# for x in range (0,Index+1):
#    n+=x
# print(n)

# list1 = [4, 6, 8, 24, 12,2]
# max= sorted(list1)
# print(max[-1])


# list = []
# list_1 =[]
# n = int(input("enter the total numbers inside list.:    "))
# i = 1
# while(i <= n):
#    num = int(input("enter the numbers you want to insert into list: "))
#    i +=1
#    list.append(num)
# print(list, " <--the given list by you is here.\n ")
  
# list.sort()
# print(list)
# print(max(list))

