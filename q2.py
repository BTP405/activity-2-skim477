import matplotlib.pyplot as plt
import numpy as np

def graphSnowfall(t):

    with open(t, 'r') as file:
        snowfall_data = [float(line.strip()) for line in file]
        containers = {"0-10":0, "11-20":0, "21-30":0, "31-40":0, "41-50":0}           
    
        for amount in snowfall_data:
            if amount <= 10:
                containers["0-10"]+=1
            elif amount <= 20:
                containers["11-20"]+=1
            elif amount <= 30:
                containers["21-30"]+=1
            elif amount <= 40:
                containers["31-40"]+=1
            elif amount <= 50:
                containers["41-50"]+=1

    ranges = list(containers.keys())
    occurrences = list(containers.values())
    
    plt.figure(figsize=(10, 10))
    plt.bar(ranges, occurrences, color='blue')
    plt.xlabel('Range (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation')
    plt.show()
    

graphSnowfall("graph.txt")
