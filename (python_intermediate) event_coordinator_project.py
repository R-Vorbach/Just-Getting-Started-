# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 18:23:12 2022

@author: swimm
"""
import random

guests = {}
def read_guestlist(text):
  text_file = open(text,'r')
  while True:
    line = text_file.readline().strip().split(",")
    y = yield 
    
    #store the line of text into variable 'line' first!
    #setting it equal to the 'yield' expression creates conflicts with the below conditional as well as with first yielding an desired text before reaching the conditional 
    #e.g. yields undesired ","-line first then inputs it into following conditional statement
    
    #updating the generator with send-method is possible with variable 'y'

    if len(line) < 2:
    # If no more lines, close file
      text_file.close()
      break

    if y != None:
      name = y[0]
      age = y[1]
      guests[name] = int(age)
    name = line[0]
    age = line[1]
    guests[name] = int(age)
    
#accesses full txt file, helps check the program
alltext = open('guest_list.txt','r').read()
#print(alltext)

generator = read_guestlist('guest_list.txt')


#1
for i in range(11):
  next(generator)
#print(guests)


#2
generator.send('Jane,35'.strip().split(","))
#sends non-None value to generator that's sent to second conditional. A name is not skipped since the line is always added into the dictionaryy regardless 


#3
next(generator)
next(generator)
next(generator) #final iteration ('Rose')

#print(guests)



#4
gen_expression = (i for i in guests if guests[i] >= 21)
#for i in gen_expression:
  #print(i)



#5
foods = ['Chicken', 'Beef', 'Fish']
def table1_gen():
  for i in range(1,6):
    random.shuffle(foods)
    for j in foods:
      yield (j, 'Table 1', 'Seat '+str(i))
      break
#assigns seating for table 1
#NOTE the 'food' at every seat is completely random at every time when we run our code

def table2_gen():
  for i in range(1,6):
    random.shuffle(foods)
    for j in foods:
      yield (j, 'Table 2', 'Seat '+str(i))
      break

def table3_gen():
  for i in range(1,6):
    random.shuffle(foods)
    for j in foods:
      yield (j, 'Table 3', 'Seat '+str(i))
      break

def tables_gen():
  yield from table1_gen()
  yield from table2_gen()
  yield from table3_gen()

tables = tables_gen()
#table generator for all 3 tables

#for i in tables:
#  print(i)


#6

def assign_gen(dictionary, table_generator):
  for i in dictionary:
    for j in table_generator:
      yield (i, j)
      break 
#assigns every name (key in the guest dictionary) to a seating in the table-generator

assignments = assign_gen(guests, tables)
for i in assignments:
  print(i)



















