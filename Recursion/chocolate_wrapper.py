"""
    Given the following three values, the task is to find the total number of maximum chocolates 
    you can eat. 
    -> money: Money you have to buy chocolates
    -> price: Price of a chocolate
    -> wrap: Number of wrappers to be returned for getting one extra chocolate.
"""
m, p, w = map(int, input().split())


def chocolates(m, p, w):
    count = 0
    
