# Yusuf Baig, yb3dt

list = [1, 6, 34, 74, 3, 74, 21, 83, 291, 48389729, 84759857825895]

# list.sort(reverse=True)
# print(list)

# return last item in list
# def last_index(list_input):
#     return list_input[len(list_input)-1]
#
# print(last_index(list))

# return last item in list without using len()
#
# def last_thingy(list_input):
#     return list_input[-1]
#
# print(last_thingy(list))

# function that takes every four items in a list and calculates distant between them, then makes all those values into a new list, then return the last value

# def anythingyouwant(list):
#     new_list = []
#     for i in range(len(list)-3):
#         distance = ((list[i] - list[i+2])**2 + (list[i+1] - list[i+3])**2)**(1/2)
#         new_list.append(distance)
#     return new_list[-1]
#
# print(anythingyouwant(list))


# do that again, but this time return median distance

def anythingyouwant(list):
    new_list = []
    for i in range(len(list)-3):
        distance = ((list[i] - list[i+2])**2 + (list[i+1] - list[i+3])**2)**(1/2)
        new_list.append(distance)
        new_list = sorted(new_list)
    return new_list[len(new_list)//2]

print(anythingyouwant(list))



