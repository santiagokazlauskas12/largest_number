""" * [1] => 1
    * [1, 2] => 1
    * [1, 1, 3, 3, 3, 4, 4, 4, 4] => 3"""

import math


lista=[1, 1,1,1,1, 3, 2, 2, 2, 2, 2, 3, 3, 4, 4, 4,4, 4]

def max_repeat (list_numbers):

    dic={}
    max_list=[]

    for number in list_numbers:
        if number not in dic:
            dic[number]=1
        elif number in dic:
            dic[number]=dic[number]+1

    for k,v in dic.items():
        result=math.inf
        if v == max(dic.values()) and k < result:
                result=k
                return result,v




print(max_repeat(lista))
