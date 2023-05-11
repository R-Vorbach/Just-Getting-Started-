# -*- coding: utf-8 -*-
"""
Created on Thu May 11 19:12:54 2023

@author: swimm
"""
import codecademylib3_seaborn
import pandas as pd
import numpy as np
from weather_data import london_data

#1 first lines of our london weather data
print(london_data.head())

#2 length of data_set
#print(len(london_data))

#Temperature variable 
#3
temp = london_data["TemperatureC"]
#print(temp[0:2])

#4
average_temp = np.average(temp)
#print(average_temp)

#5
temperature_var = np.var(temp)
#print(temperature_var)

#6
temperature_standard_deviation = np.std(temp)
#print(temperature_standard_deviation)

#Month Filtering
#7
#month column would be ideal to pivot our temperature readings about

#8
#extract temperatures for only June readings
june = london_data.loc[london_data["month"]==6]["TemperatureC"]
#print(june)

#9
#extract temperatures for only July readings
july = london_data.loc[london_data["month"]==7]["TemperatureC"]
#print(july)

#10, 11 statistics for both june & july temp data

june_mean = np.mean(june)
june_var = np.var(june)
june_std = np.std(june)

july_mean = np.mean(july)
july_var = np.var(july)
july_std = np.std(july)

print(june_mean, june_var, june_std)
print(july_mean, july_var, july_std)

#12 
#mean & std for every month
for i in range(1,13):
  month_temperatures = london_data.loc[london_data["month"]==i]["TemperatureC"]
  print("The mean temperature in month "+str(i)+" is "+str(np.mean(month_temperatures)))
  print("The standard deviation in month "+str(i)+" is "+str(np.std(month_temperatures))+"\n")

#13
#A
March_Humidity = london_data.loc[london_data["month"]==3]["Humidity"]
print("Humidity report (in units g/(m^3)) for March we have a mean: "+str(np.mean(March_Humidity))+ " with a standard deviation: "+str(np.std(March_Humidity))+"\n")

#B
noon_temps = []
noon_temps_lst = []
for i in london_data["Time"]:
  if i[11:13] == "12":
    noon_temps.append(london_data.loc[london_data["Time"]==i]["TemperatureC"])

#translates array object to list
for i in range(len(noon_temps)):
    noon_temps_lst.append(list(noon_temps[i])[0])
#print(noon_temps_lst[0])

#prints noon london temp statistics
print("At hour 12 we have a mean temperature (in celsius) of: "+str(np.mean(noon_temps_lst))+" with a standard deviation: "+str(np.std(noon_temps_lst)))