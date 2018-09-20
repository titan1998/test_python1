#Ising model of Ferromagnetism

#importing libraries
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.constants as cnst
from matplotlib import colors
import sys

#intial parameters
N = 20# model ferromagnet as N by N lattice. Total lattices points is N^2
J =  1  #gives whether  exchange energy is positive or negative  (+1,-1
mu = 1  #magnetic moment in
H = 0   # applied field in
T = np.linspace(0.1,5.0,num= 50)  # temperature of heat bath in J/kb, initialising to 100 temps between the 2 values

#Tder= 1/3 # temperature
t = 0     #intialises time as zero
tstep = 200 #number of time steps used to reach near equilibrium
kb = 1 #cnst.k

 #making an N by N lattice
Initial_Lattice =np.random.choice([-1],[N,N]) # initialises spin lattice to be 'randomly' either up or down
Lattice= Initial_Lattice.copy()
np.savetxt("InitialLattice.txt",Initial_Lattice,fmt='%2d')

# Opening 2 files for the average C & another for all iterative values of C
##ef1=open('./E_avg.out', 'w+') #Open file to write values to use for plotting
##ef2=open('./E_iter.out', 'w+') #Open file to write values to use for plotting
cf1=open('./C_avg.out', 'w+') #Open file to write values to use for plotting
cf2=open('./C_iter.out', 'w+') #Open file to write values to use for plotting
cf3=open('./C_theo.out', 'w+') #Open file to write values to use for plotting 

#spin coupling
def spin_coupling(array,i,j):
        nearest_spins = array[i][j]*(array[i][(j+1) % (N)]+array[i][(j-1) % (N)]+array[(i+1)%N][j]+array[(i-1)%N][j]) #modular N ensures we have periodic boundary condtions
        return nearest_spins

#calculating total energy
def E_total(array):
    totalEnergy= array.copy()
    for i in range(0,N):    #goes through rows
        for j in range (0,N):  #goes through columns
            totalEnergy[i,j]= -J*(spin_coupling(array,i,j))-mu*H*(array[i,j]) #
    return  ( np.sum(totalEnergy) / (2)  )  # calculate total energy  and to take into account double counting 

#calculating total magnetisation
def magnetisation(array):
    return ( float(np.sum(array)) /  (N**2) )#from 1 to -1

E=np.zeros(tstep) #define total energy  array
E2=np.zeros(tstep) #define total energy square  array
C_v=np.zeros(10) #define the array to hold the heatcap values to get average value
E_av=np.zeros(10) #define the array to hold the Energy  values to get average value

k = magnetisation(Initial_Lattice)
#print("{:8.4g} {:8.4g} ".format(k,0))

#Metropolois algorithm

for x in range(len(T)):
        for iter in range(0,10):
            Lattice = Initial_Lattice.copy()
            for t in range (0,tstep):
                for i in range(0,N):    #goes through rows
                    for j in range (0,N):  #goes through columns
                        delta_energy = -J*(-2*spin_coupling(Lattice,i,j))-mu*H*(-2*Lattice[i,j]) #calculate change of energy when i,j element changes sign (-ve becuase using initial)
                        #print (delta_energy)
                        p = np.exp(-1*abs(delta_energy/(kb*T[x])))  #weighting of microstates, check T[X] non-zero
                        #print (p)
                        r = np.random.random()
                        if delta_energy < 0:
                            Lattice[i,j] = -1 * Lattice[i,j]
                        elif p > r:
                            Lattice[i,j] = -1*Lattice[i,j]
                        else :
                            Lattice[i,j] = 1*Lattice[i,j]
                E[t] = E_total(Lattice)
                E2[t] = E[t] ** 2
                #print("{:8.4g} {:8.4g} ".format(m,t+1))
                
            E_av[iter]= np.average(E[(tstep-101):(tstep-1)])  #gives average of total energy
            E2_av= np.average( E2[(tstep-101):(tstep-1)] ) #gives average energy^2
            C_v [iter] = abs( 1.0 / ( T[x]**2 * N**2) * (E2_av- (E_av[iter]**2 )))
            print("{:8.4g} {:8.4g} ".format(C_v[iter], T[x]), file = cf2, flush=True)
##            print("{:8.4g} {:8.4g} ".format(E_av[iter], T[x]), file = ef2, flush=True)
##        E_av_avg = np.average(E_av)
        C_v_avg = np.average(C_v)
        C_v_theo =  (8/ np.pi)* (T[x] **(-2)) * np.log(abs(1/ ( T[x]-2.26918) ))
        if C_v_theo <0:
                C_v_theo =0
        print("{:8.4g} {:8.4g} ".format(C_v_avg, T[x]), file = cf1, flush=True)
##        print("{:8.4g} {:8.4g} ".format(E_av_avg, T[x]), file = ef1, flush=True)
        print("{:8.4g} {:8.4g} ".format(C_v_theo, T[x]), file = cf3, flush=True)
        print('done for T =',T[x])
        sys.stdout.flush()
