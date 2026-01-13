"""
The goal was to:

Write a Python program that accepts a list of integers and calculates the 
length and the fifth element. 

Return true if the length of the list is 8 and the fifth element occurs thrice 
in the said list.

Resource: https://www.w3resource.com/python-exercises/puzzles/index.php
"""
def check_len_and_indx_5(list):
    repeated_index_5 = 0
    len_8_and_reputition_3 = False
    
    for i in range(len(list)):
        if list[4] == list[i]:
            repeated_index_5 += 1

        if len(list) == 8 and repeated_index_5 == 3:
            len_8_and_repetition_3 = True

    print(len_8_and_repetition_3)

check_len_and_indx_5([19, 19, 15, 5, 5, 5, 1, 2])