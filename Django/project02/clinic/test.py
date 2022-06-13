array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10

# def sum (array, targetSum):
#     for num in array:
#         sumNumbers = 0

#         while sumNumbers != targetSum

from typing import List, Tuple, Union


# def sum(array: List[int], targetSun: int):
#     unique_numbers = set()
#     for num in array:
#         required_value = targetSun - num
#         print(required_value)
#         print(unique_numbers)
#         if required_value in unique_numbers:
#             return num, required_value
#         unique_numbers.add(num)
#     return []


# def sum(array: List[int], targetSun: int):
#     array_sum_numbers = []
#     for num in array:
#         array.remove(num)
#         second_number_sum = targetSun - num
#         if second_number_sum in array:
#             array_sum_numbers.append(num)
#             array_sum_numbers.append(second_number_sum)
#             return array_sum_numbers
#     return []


# print(sum(array, targetSum))

string = "BBBBBBBBBBBAACCDDD"


def countChar(string):
    charsList = set(string)
    stringsSum = ""
    for char in charsList:
        if string.count(char) > 9:
            numberChar = str(string.count(char) - 9)
            stringsSum = stringsSum + "9" + char + numberChar + char
        if string.count(char) < 9:
            stringsSum = stringsSum + str(string.count(char)) + char
    return stringsSum


print(countChar(string))
