# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 20:02:26 2022

@author: -
"""
import csv
from functools import reduce

def count(predicate, iterable):
  count_filter = filter(predicate, iterable)
  count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
  return count_reduce    

#recursive helper function for our average
def avg_helper(curr_count, itr, curr_sum):
  next_num = next(itr, 'null')
  #base case
  if next_num == 'null':
    return (curr_sum / curr_count)
  #computation
  curr_count += 1
  curr_sum += next_num
  #recursive call
  return avg_helper(curr_count, itr, curr_sum)


def average(itr):
  # If itr is not iterable, this will generate an iterator.  
  iterable = iter(itr)
  return avg_helper(0, iterable, 0)

with open('1kSalesRec.csv', newline = '') as csvfile:
  reader = csv.reader(csvfile, delimiter=',', quotechar='|')
  fields = next(reader)

  #counts number of orders for Belgium
  count_belgium = count(lambda x: x[1] == 'Belgium', reader)
  print(count_belgium)

  #finds average total profit for Portugal's orders
  csvfile.seek(0)
  avg_portugal = average(map(lambda x: float(x[13]), filter(lambda x: x[1] == 'Portugal', reader)))
  print(avg_portugal)

