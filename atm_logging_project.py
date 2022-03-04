# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 11:45:56 2022

@author: swimm
"""
import random
import logging
import sys
from datetime import datetime

with open('stored_logs.log', 'w') as file:
    file.write('Begin logs\n')

logger = logging.getLogger(__name__)

format1 = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setFormatter(format1)

#file_handler = logging.FileHandler('formatted.log')
#file_handler.setFormatter(format1)

logger.addHandler(stream_handler)
#logger.addHandler(file_handler)

logger.setLevel(logging.DEBUG)
logging.basicConfig(filename='stored_logs.log', level=logging.DEBUG, format='[%(asctime)s] - %(lineno)d - %(levelname)s - %(message)s')
#configures the logs written to the file are formatted to include level names

#Note: outside of CodeCademy 'formatted.log' file does not exist; just create a new empty file in its place

class BankAccount:
  def __init__(self):
    self.balance=100
    print("Hello! Welcome to the ATM Depot!")
    logger.debug(self.balance)
    
  def authenticate(self):
    while True:
      pin = int(input("Enter account pin: "))
      logger.info(pin)
      if pin != 1234:
        logger.error('Invalid pin. Try again.')
      else:
        return None   
 
  def deposit(self):
    try:
      amount=float(input("Enter amount to be deposited: "))
      #if amount < 0:
       # logger.warning("You entered a negative number to deposit.")
        
      self.balance += amount
      logger.info("Amount Deposited: ${amount}\n Transaction Info:\n Status: Successful\n Transaction #{number}\n".format(amount=amount, number=random.randint(10000, 1000000)))

    except ValueError or amount < 0:
      logger.error("You entered an non-number or negative value to deposit.")

      logger.info("Transaction Info:\n Status: Failed\n Transaction #{number}".format(number=random.randint(10000, 1000000)))
 
  def withdraw(self):
    try:
      amount = float(input("Enter amount to be withdrawn: "))
      if self.balance >= amount:
        self.balance -= amount
        logger.info("You withdrew: ${amount}\n You withdrew: ${amount}\n Transaction Info:\n Status: Successful\n Transaction #{number}".format(amount=amount, number=random.randint(10000, 1000000)))
      else:
        logger.error("Insufficient balance to complete withdraw.")
        logger.info("Transaction Info:\n Status: Failed\n Transaction #{number}".format(number=random.randint(10000, 1000000)))
    except ValueError:
      logger.error("You entered a non-number value to withdraw.")
      logger.info("Transaction Info:\n Status: Failed\n Transaction #{number}".format(number=random.randint(10000, 1000000)))
 
  def display(self):
    print("Available Balance = ${balance}".format(balance=self.balance))
    logger.info(self.balance)
 
acct = BankAccount()
acct.authenticate()
acct.deposit()
acct.withdraw()
acct.display()

with open('stored_logs.log', 'r') as file:
    print(file.read())