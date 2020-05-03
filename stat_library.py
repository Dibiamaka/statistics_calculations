# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 06:07:12 2020

@author: DIBIAMAKA
"""
 
import matplotlib.pyplot as plt
import numpy
import statistics
from statistics import mode,  StatisticsError

print("""
      
This is a basic statistics calcultor.
It asks for the amoubt of data which the user wants to calculate then,
which the user enters manually for the calculator to calculates and prints answers.
Mean, median, mode, standard deviation and variance are printed.

iThis simple calculator also calculates for random uniform distribution for a given polpulation.
you will however neeed to provid the desired mean and standard deviation and also the amount of
random generated values as desired.
this enables the cal. to calculate and plot for x and y axis of the 
histogram
scatter
line regression
etc

 i mostly use this for my library
 
""")
feed = input("How many items are you calculating for >? ")
feed = int(feed)

data = []

def start():
    
    while pop():
        pass 
    Random()

        
        

    
    

def pop():
    population = 1
    while population <= feed:
        collect = input("Enter data> ")
        collect = float(collect)
        data.append(collect)
        population = population +1
        print(data)

pop()
     



Mean = statistics.mean(data)    
Midian = statistics.median(data)
Standard_deviation = statistics.stdev(data)    
Variance = statistics.variance(data)
try:
    Mode = statistics.mode(data)
except StatisticsError:
    print("There are no unique entry")
    



print("Mean = ", Mean)
print("Midian = ", Midian)
print("Standard deviation = ", Standard_deviation)
print("Vaiance = ", Variance)


def Random():
    while user_input == "Y":
        user_input = input("Do you want to calculate for random unifrom distrinution? y/N")
        rand_stdX = input("std range for random x axis generation ? >")  
        rand_meanX = input("mean range for random x axis generation ? >")
        rand_stdX = float(rand_stdX)
        rand_meanX = float(rand_meanX)
        rand_stdY = input("std range for random y axis generation ? >")
        rand_meanY = input("mean range for random y axis generation ? >")
        rand_stdY = float(rand_stdY)
        rand_meanY = float(rand_meanY)
        size = input("Enter the size of the random populationn to be generated")
        size = int(size)
        new_X = numpy.random.normal(rand_meanX, rand_stdX,size )
        new_Y = numpy.random.normal(rand_meanY, rand_stdY, size)
        plt.scatter(new_X, new_Y)
        plt.show()
    else:
        print("Thanks for calculating")
    
Random()





        


    
 
    
        
    
    

 

    