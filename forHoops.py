# for i in range(4):
#     print("lol")

list = ['Mariam','24','0.0002','4','18','F','']
list1 = ['a','b','c','d','e','f','g','h','i','j','k']

#Print the first three items of list1 in three different ways using a for loop

# for i in range(3):
#     print(list1[i])

# for i in range(len(list1)):
#     if (i < 3):
#         print(list1[i])
#     else:
#         break

# boneless = 0
# for i in list1:
#     if (boneless < 3):
#         print(list1[boneless])
#         boneless += 1
#     else:
#         break

#Print the last three items of list1 in three different ways using a for loop

# boneless = len(list1) - 3
# for i in list1:
#     if (boneless < len(list1)):
#         print(list1[boneless])
#         boneless += 1
#     else:
#         break

# for i in range(len(list1)):
#     if (i < len(list1) - 3):
#         pass   #The pass statement is a null operation; nothing happens when it executes.
#     elif (i >= len(list1) - 3):
#         print(list1[i])
#     else:
#         break

# boneless = -1   #starts from bakc to fron 'print(list1[-1])'
# for i in list1:
#     if (boneless > -4):
#         print(list1[boneless])
#         boneless += -1
#     else:
#         break


#Print the middle three items of list1 in three different ways using a for loop

boneless = 0
for i in list1:

    if (boneless != (len(list1)//2)):
        boneless +=1
    elif (boneless == (len(list1)//2)):
        print(list1[boneless])
        print(list1[boneless-1])
        print(list1[boneless+1])
        break
    else:
        break

for i in range(len(list1)):
    if (i < len(list1)//2):
        pass   #The pass statement is a null operation; nothing happens when it executes.
    elif (i == len(list1)//2):
        print(list1[i])
        print(list1[i-1])
        print(list1[i+1])
        break
    else:
        break


