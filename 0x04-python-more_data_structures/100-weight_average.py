#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    denominator = 0
    for tup in my_list:
        total += (tup[0] * tup[1])
        denominator += tup[1]
    average = total/denominator
    return average
