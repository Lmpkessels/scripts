"""
The goal was to:

Write a Python program that accepts a list of integers and calculates the 
length and the fifth element. 

Return true if the length of the list is 8 and the fifth element occurs thrice 
in the said list.

Resource: https://www.w3resource.com/python-exercises/puzzles/index.php
"""
def check_length_and_5th_element(list):
    repeated_index_5 = 0
    index_5_is_3_x_in_the_list = False
    
    for i in range(len(list)):
        if list[4] == list[i]:
            repeated_index_5 += 1

        if len(list) == 8 and repeated_index_5 == 3:
            index_5_is_3_x_in_the_list = True

    print(index_5_is_3_x_in_the_list)

check_length_and_5th_element([19, 19, 15, 5, 5, 5, 1, 2])