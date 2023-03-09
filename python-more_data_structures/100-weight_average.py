#!/usr/bin/python3
def weight_average(my_list=[]):
    # If the list is empty, return 0
    if not my_list:
        return 0
    # Compute the sum of products and the sum of weights
    sum_products = 0
    sum_weights = 0
    for score, weight in my_list:
        sum_products += score * weight
        sum_weights += weight
    # Compute and return the weighted average
    return sum_products / sum_weights
