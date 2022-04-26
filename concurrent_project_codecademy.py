# -*- coding: utf-8 -*-
import time
import threading 
import asyncio
from multiprocessing import Process


def cal_average(num):  # Average function used for sequential programming, threading, and multiprocessing
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  time.sleep(1)
  return avg

def main_sequential(list1, list2, list3):  # Main wrapper for sequential example
  s = time.perf_counter()
  # your code goes here
  cal_average(list1)
  cal_average(list2)
  cal_average(list3)
  # roughly 3 secondds is the total time needed in order to execute these 3 function calls (each of which has a wait time of 1sec from the time.sleep(1) line)
  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

async def cal_average_async(num):  # Average function used for asynchronous programming only ( needs await asyncio.sleep() )
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  await asyncio.sleep(1)
  return avg

async def main_async(list1, list2, list3):  # Main wrapper for asynchronous example
  s = time.perf_counter()
  # your code goes here
  tasks = [cal_average_async(list1), cal_average_async(list2), cal_average_async(list3)]
  await asyncio.gather(*tasks)
  #since the tasks are run concurrently, each task can be run efficiently and each ignoring the one second wait time of each other. The total elasped time would be around 1.00033s roughly

  elapsed = time.perf_counter() - s
  print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")

def main_threading(list1, list2, list3):  # Main wrapper for threading example
  s = time.perf_counter()
  # your code goes here
  
  #7
  lists = [list1, list2, list3]
  threads = []
  
  #8
  for i in range(len(lists)):
    x = threading.Thread(target=cal_average, args=(lists[i],))
    threads.append(x)
    x.start()
  for j in threads:
    j.join()
  #similarly the threads are run concurrently and so the total time was roughly 1.002s
  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

def main_multiprocessing(list1, list2, list3):  # Main wrapper for multiprocessing example
  s = time.perf_counter()
  # your code goes here

  #10
  lists = [list1, list2, list3]
  #11
  processes = [Process(target=cal_average, args=(lists[i],)) for i in range(len(lists))]
  #12
  for p in processes:
    p.start()
  for p in processes:
    p.join()
  #total elapsed time was 1.005s

  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")

#asynchronous approach was a whole order of magnitude faster than the threading and multiprocessing ones. Thus for calculating an average, it seems using asynch would be our best bet for efficiency.

if __name__ == '__main__':  # Need to use this if-statement so multiprocessing doesn't cause an infinite loop
  l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Three lists we are trying to calculate average on
  l2 = [2, 4, 6, 8, 10]
  l3 = [1, 3, 5, 7, 9, 11]
  main_sequential(l1, l2, l3)
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main_async(l1, l2, l3))
  main_threading(l1, l2, l3)
  main_multiprocessing(l1, l2, l3)

