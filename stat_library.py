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
It asks for the amount of data which the user wants to calculate then,
when the user enters manually the data for the calculation,  it calculates and prints answers;
Mean, median, mode, standard deviation and variance are printed.
This simple calculator also calculates for random uniform distribution for a given polpulation.
you will however neeed to provide the desired mean and standard deviation and also the amount of
random values to be generated as desired.
This enables the cal. to calculate and plot for x and y axis of the histogram,scatter.
Plenty of room for improvement
 
""")

data = []

def start():
    while pop():
        pass 
    Random()

        
def pop():
    feed = int(input("How many items are you calculating for? > "))
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
    yes_answers = ("Yes", "YES" "yes", "Y", "y")
    no_answer = ("No", "no","N", "NO", "n")
    while True:
        print("Do you want to calculate for random normal distribution? Y or yes or hit enter to exit")
        user =input()
        if user == '':
            break
        if user in no_answer:
            break
        
        if user in yes_answers:
            rand_stdX = input("what is the standard devistion range for random x axis generation ? >")  
            rand_meanX = input("what is the mean range for random x axis generation ? >")
            rand_stdX = float(rand_stdX)
            rand_meanX = float(rand_meanX)
            rand_stdY = input("what is the standard deviation range for random y axis generation ? >")
            rand_meanY = input("what is the mean range for random y axis generation ? >")
            rand_stdY = float(rand_stdY)
            rand_meanY = float(rand_meanY)
            size = input("Enter the size of the random populationn to be generated")
            size = int(size)
            new_X = numpy.random.uniform(rand_meanX, rand_stdX,size )
            new_Y = numpy.random.uniform(rand_meanY, rand_stdY, size)
            print("Generated value for x", new_X)
            print("Generated value for y", new_Y)
            plt.hist(new_X, 10)
            plt.show()
            plt.hist(new_Y, 10)
            plt.show()
            plt.scatter(new_X, new_Y)
            plt.show()
            print("Graph is plotted... thanks ")
            break
    else:
        print("Thanks for calculating")
    
Random()


  


        


    
 
    
        
    
    

 

    