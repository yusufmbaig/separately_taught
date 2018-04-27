# Yusuf Baig, yb3dt

#the way theuy  waoiaokrks dont whrite waht i say verbationm
#fulfil function of for loops, bu lets code be more abiguous

# list = [1,2,3,4,5,5,67,7,8,9]
#
# boneless = True
# while boneless:
#     if len(list) == 0:
#         break
#     else:
#         del list[-1]
#         print(list)
# print(list)



# while loop that will print out the highest number in a given list

list2 = [2, 5, 1, 7, 30, 3, 4, 8, 60]

# boneful = True
# counter = 0
# while boneful:
#     print(list2)
#     if counter + 1 == len(list2):   # could also write counter < len(list2)
#         boneful = False
#     elif list2[counter] <= list2[counter + 1]:
#         del list2[counter]
#         if len(list2) == 1:
#             boneful = False
#         else:
#             counter += 1
#     elif list2[counter] > list2[counter + 1]:
#         del list2[counter + 1]
#         if len(list2) == 1:
#             boneful = False
#         else:
#             counter += 1
# print(list2)
# make counter that increases
# if counter is greater than counter+1, repeat loop with counter ++
# if counter is less that counter +1, delete counter
# else display list

# boneful = True
# counter = 0
# while boneful:
#     print(list2)
#     for i in range(len(list2)):
#         if list2[i] <= list2[i + 1]:
#             del list2[i]
#         elif list2[i] > list2[i + 1]:
#             del list2[i + 1]
#         else:
#             boneful = False

boneful = True
list3 = []

while boneful:
    max = 0
    print(list2)
    for i in list2:
        if max < i:
            max = i
    list3.append(max)
    del list2[list2.index(max)]
    if len(list2) == 0:
        boneful = False

print(list3)