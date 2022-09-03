my_first_list = [47, "trol", 19, 21, 97, 777]
my_second_list = [17, "love", 19, 21, 97, 771]

list_difference = [element for element in my_first_list if element not in my_second_list]

print(list_difference)



difference_1 = set(my_first_list).difference(set(my_second_list))
difference_2 = set(my_second_list).difference(set(my_first_list))

list_difference_1 = list(difference_1.union(difference_2))

print(list_difference_1)