import matplotlib.pyplot as plt
import numpy as np


#Load the data
C_av2,T2  = np.loadtxt("./C_avg_2.out",unpack=True) # C average values against temperature
C_av4,T4  = np.loadtxt("./C_avg_4.out",unpack=True) # C average values against temperature
C_av8,T8  = np.loadtxt("./C_avg_8.out",unpack=True) # C average values against temperature
C_av16,T16  = np.loadtxt("./C_avg_16.out",unpack=True) # C average values against temperature
#C_av25,T25  = np.loadtxt("./C_avg_25.out",unpack=True) # C average values against temperature
C_av32,T32  = np.loadtxt("./C_avg_32.out",unpack=True) # C average values against temperature
#C_iter,T1  = np.loadtxt("./C_iter.out",unpack=True) # C iterative values against temperature
#C_theo,T  = np.loadtxt("./C_theo.out",unpack=True) # C iterative values against temperature

max_C2 = max(C_av2)
max_T2 = T2[C_av2.argmax()]
print(max_C2, max_T2, 2)

max_C4 = max(C_av4)
max_T4 = T4[C_av4.argmax()]
print(max_C4, max_T4, 4)

max_C8 = max(C_av8)
max_T8 = T8[C_av8.argmax()]
print(max_C8, max_T8, 8)

max_C16 = max(C_av16)
max_T16 = T16[C_av16.argmax()]
print(max_C16, max_T16, 16)

##max_C25 = max(C_av25)
##max_T25 = T25[C_av25.argmax()]
##print(max_C25, max_T25, 25)

max_C32 = max(C_av32)
max_T32 = T32[C_av32.argmax()]
print(max_C32, max_T32, 32)

#plot magnetisation vs time
fig, ax1 = plt.subplots()
ax1.plot(T2,C_av2,lw=2,label=r" $C_v$  N2", color='blue')
ax1.plot(T4,C_av4,lw=2,label=r" $C_v$  N4", color='green')
ax1.plot(T8,C_av8,lw=2.5,label=r" $C_v$  N8",color='cyan')
ax1.plot(T16,C_av16,lw=2.5,label=r"$C_v$  N16",color='orange')
##ax1.plot(T25,C_av25,lw=2.5,label=r"$C_v$  N25",color='yellow')
ax1.plot(T32,C_av32,lw=2,label=r"$C_v$  N32",color='purple')
#ax1.plot(T1,C_iter,'.',markersize=4,color = "green", label =r'trial $C_v$')
#ax1.plot(T,C_theo,lw=2.5,label=r"theoretical $C_v$ ", color="magenta")
plt.plot( [2.26918, 2.26918], [0, 1.8] , linestyle="dashed", color="red", linewidth=2, label=r"$T_{critical}$ (theoretical)")
plt.legend(loc= 'upper right')
#plt.ylim(0, 0.014 )
for ymaj in ax1.yaxis.get_majorticklocs():
  ax1.axhline(y=ymaj,color= 'k',ls='-')

plt.xlabel(r'Temperature $/ J k_B^{-1}$', fontsize=16)
plt.ylabel(r'$ C_v /  J  k_B ^{-2}$ ', fontsize=16)
#ax1.set_title("Heat Capacity vs  Temperature for different Lattice Size", fontsize=16)
"""ax1.legend(loc='upper center', bbox_to_anchor=(0.66, 1.00),
          ncol=2, fancybox=True, shadow=True)"""



plt.show()  #uncomment if one want to show plot
#plt.savefig("T=0.05_v2.png") #saves plot as png
