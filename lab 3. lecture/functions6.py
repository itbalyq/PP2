def find_common_elements(list_x, list_y):
    common_list = []
    for element in list_x:
        if element in list_y:
            common_list.append(element)
    return common_list

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

result = find_common_elements(list1, list2)
print(result)

