import numpy as np
import matplotlib.pyplot as plt
import csv
from numpy import genfromtxt

a = 'output'
b = '.csv'

fig, graph = plt.subplots()

for var in range(5):
    tsper = []
    ssper = []
    vsper = []
    with open(a + str(var) + b, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for riga in csv_reader:
            tsper.append(riga["t"])
            ssper.append(riga["s"])

    tsper = np.array(tsper, dtype=np.float64)
    ssper = np.array(ssper, dtype=np.float64)

    #normalize time
    c = tsper[0]
    for i in range(11):
            tsper[i] = tsper[i] - c


    vsper.append(0)
    for i in range(11):
        if i != 0:
            vsper.append((ssper[i - 1] - ssper[i])/(tsper[i] - tsper[i - 1]) / 100)

    vsper = np.array(vsper, dtype=np.float64)

    #print(tsper)
    #print(ssper)
    #print(vsper)

    if(False): #set to false to get only the all_function graph
        plt.figure()
        plt.plot(tsper, vsper, label = 'sample_' + str(var + 1))
        plt.legend()
    graph.plot(tsper, vsper, 'ro',label = 'sample_' + str(var + 1))


graph.set_xlabel('t')
graph.set_ylabel('v(t)')
plt.show()
