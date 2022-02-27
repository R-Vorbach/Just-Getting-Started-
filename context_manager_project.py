# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 15:24:32 2022

@author: swimm
"""
# Write your code below: 
#import the contextmanager decorator
from contextlib import contextmanager

#define our generic context manager
#steps 2-4
@contextmanager
def generic(card, sender_name, recipient):
  opened_card = open(card, 'r')
  new_opened_card = open(f"{sender_name}_generic.txt", 'w')
  try:
    yield new_opened_card.write(f"Dear {recipient}\n" + opened_card.read()+"\n" + f"Sincerely, {sender_name}")
  finally:
    new_opened_card.close()
    opened_card.close()

#5
#with generic('thankyou_card.txt', 'Mwenda', 'Amanda') as card:
 # print('Card Generated!')
  #prints string confirming we successfully created our unique card

#6
#with open("Mwenda_generic.txt", 'r') as card:
 # print(card.read())
#prints our newly written thankyou card to Amanda, that we just wrote in the context manager (up above) 

#7
#class based context manager for 'personalized cards'
class Personalized:
  def __init__(self, sender, receiver):
    self.sender = sender
    self.receiver = receiver
    self.opened_personal_card = open(f"{self.sender}_personalized.txt", "w")
    #saves the sender and recipient names as attributes
    #saves an opened empty file as an attribute as well
  
  def __enter__(self):
    (self.opened_personal_card).write(f'Dear {self.receiver}\n')
    return self.opened_personal_card
    #writes the first line of our personal card
  
  def __exit__(self, *exc):
    (self.opened_personal_card).write(f'Sincerely {self.sender}\n')
    #return self.opened_personal_card
    (self.opened_personal_card).close()
    #writes the final line on our card


#10
with Personalized("John", "Michael") as card:
  card.write("I am so proud of you! Being your friend for all these years has been nothing but a blessing. I don’t say it often but I just wanted to let you know that you inspire me and I love you! All the best. Always.\n")
#adds personal contents to our "John_personalized.txt" personal card file

#11
#with open("John_personalized.txt", "r") as card:
 # print(card.read())
  #prints our read out personal card


#12
#nested with statements 
#writes the generic b-day card for 'Remy' from Josiah as well as the personal card to Esther from Josiah
with generic('happy_bday.txt', 'Josiah', 'Remy') as bday_card:
  with Personalized("Josiah", "Ester") as personal:
    personal.write("Happy Birthday!! I love you to the moon and back. Even though you’re a pain sometimes, you’re a pain I can't live without. I am incredibly proud of you and grateful to have you as a sister. Cheers to 25!! You’re getting old!\n")

#13
#reads out our bdday and personal cards
with open("Josiah_personalized.txt", "r") as personal:
  with open("Josiah_generic.txt", "r") as generic:
    print(personal.read())
    print(generic.read())







