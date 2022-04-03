# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 18:32:48 2022

@author: swimm
"""
# Import module 
import sqlite3


# Task 1: Create connection object
con = sqlite3.connect('hotel_booking.db')

# Task 2: Create cursor object
cur = con.cursor()

# Task 3: View first row of booking_summary
first_row = cur.execute('''SELECT * FROM booking_summary''').fetchone()
#print(len(first_row))
#print((first_row))

# Task 4: View first ten rows of booking_summary 
first_ten = cur.execute('''SELECT * FROM booking_summary''').fetchmany(10)
#print(first_ten)

# Task 5: Create object bra and print first 5 rows to view data
bra = cur.execute('''SELECT * FROM booking_summary WHERE country = 'BRA';''').fetchall()
#for i in range(5):
 # print(bra[i])

# Task 6: Create new table called bra_customers
cur.execute('''CREATE TABLE IF NOT EXISTS bra_customers (
  num INTEGER,
  hotel TEXT,
  is_cancelled INTEGER,
  lead_time INTEGER,
  arrival_date_year INTEGER,
  arrival_date_month TEXT,
  arrival_date_day_of_month INTEGER, 
  adults INTEGER,
  children INTEGER,
  country TEXT,
  adr REAL,
  special_requests INTEGER
  )''')

# Task 7: Insert the object bra into the table bra_customers 
cur.executemany('''INSERT INTO bra_customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', bra)

# Task 8: View the first 10 rows of bra_customers
#for i in cur.execute('''SELECT * FROM bra_customers''').fetchmany(10):
 # print(i)

# Task 9: Retrieve lead_time rows where the bookings were canceled

#NOTE: error in step 9, is_cancelled = 1 is the conditional to use for grabbing only cancellations, NOT lead_time = 0
lead_time_can = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 1;''').fetchall()

# Task 10: Find average lead time for those who canceled and print results
sum_lead_time_can = 0
for i in lead_time_can:
  sum_lead_time_can += i[0]
average_lead_time_can = sum_lead_time_can / len(lead_time_can)

#print('Average lead time (cancelled): '+str(average_lead_time_can))

# Task 11: Retrieve lead_time rows where the bookings were not canceled
lead_time_notcan = cur.execute('''SELECT lead_time FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

# Task 12: Find average lead time for those who did not cancel and print results
sum_lead_time_notcan = 0
for i in lead_time_notcan:
  sum_lead_time_notcan += i[0]
average_lead_time_notcan = sum_lead_time_notcan / len(lead_time_notcan)

#print('Average lead time (Non-cancelled):' +str(average_lead_time_notcan)) 

if average_lead_time_notcan > average_lead_time_can:
  print('Those who did not cancelled, had a longer average lead_time of: '+str(average_lead_time_notcan))
else:
  print('Those who cancelled, had a longer average lead_time of: '+str(average_lead_time_can)+' days.')

# Task 13: Retrieve special_requests rows where the bookings were canceled
special_requests_can = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 1;''').fetchall()

# Task 14: Find total speacial requests for those who canceled and print results
sum_special_requests_can = 0
for i in special_requests_can:
  sum_special_requests_can += i[0]

# Task 15: Retrieve special_requests rows where the bookings were not canceled
special_requests_notcan = cur.execute('''SELECT special_requests FROM bra_customers WHERE is_cancelled = 0;''').fetchall()

# Task 16: Find total speacial requests for those who did not cancel and print results
sum_special_requests_notcan = 0
for i in special_requests_notcan:
  sum_special_requests_notcan += i[0]

if sum_special_requests_notcan > sum_special_requests_can:
  print('Those who did NOT cancel, had the largest number of special requests for a total of ' + str(sum_special_requests_notcan)+' requests.')
else:
  print('Those who cancelled, had the largest number of special requests for a total of ' + str(sum_special_requests_can)+' requests.')

# Task 17: Commit changes and close the connection
con.commit()

con.close()