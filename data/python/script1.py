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
    graph.plot(tsper, vsper, 'ro', label = 'sample_' + str(var + 1))

#add my_function
h = 25 #cm
x = h
v = 0
dt = 0.001 #s
t = 0.0
tOsservazione = 25 #s
g = 9.81
vL = 0.833


R = 0.006 #m
rhoSfera = 7800
rhoFluido = 908
MassaSfera = 0.00702 #kg
VolumeSfera = (4/3)*np.pi*R**3
PesoNelFluido = VolumeSfera*g*(rhoSfera-rhoFluido)
a = PesoNelFluido / MassaSfera
b=PesoNelFluido/(vL)

posizione = []
velocita = []
tempo = []
while t<tOsservazione and x>0:
    posizione.append(x)
    velocita.append(v)
    x=x-v*dt
    v=v+a*dt
    a=(PesoNelFluido-b*v)/MassaSfera
    tempo.append(t)
    t=t+dt
posizione = np.array(posizione, dtype=np.float64)
velocita = np.array(velocita, dtype=np.float64)
tempo = np.array(tempo, dtype=np.float64)
graph.plot(tempo, velocita, 'r-')

graph.set_xlabel('t')
graph.set_ylabel('v(t)')
plt.show()
