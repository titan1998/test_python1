import matplotlib.pyplot as plt
import numpy as np


#Load the data
C_av,T  = np.loadtxt("./C_avg.out",unpack=True) # C average values against temperature
C_iter,T1  = np.loadtxt("./C_iter.out",unpack=True) # C iterative values against temperature
C_theo,T2  = np.loadtxt("./C_theo.out",unpack=True) # C iterative values against temperature



#plot magnetisation vs time
fig, ax1 = plt.subplots()
ax1.plot(T,C_av,lw=2.5,label=r"average $C_v$ ")
ax1.plot(T1,C_iter,'.',markersize=4,color = "green", label =r'trial $C_v$')
ax1.plot(T2,C_theo,lw=1.5,label=r"theoretical $C_v$ ", color="magenta")
plt.plot( [2.26918, 2.26918], [0, 2.5] , linestyle="dashed", color="red", linewidth=2, label=r"$T_{critical}$ (theoretical)")
plt.legend(loc= 'upper right')
#plt.ylim(0, 0.014 )
for ymaj in ax1.yaxis.get_majorticklocs():
  ax1.axhline(y=ymaj,color= 'k',ls='-')

plt.xlabel(r'Temperature $/ J k_B^{-1}$', fontsize=16)
plt.ylabel(r'$ C_v /  J  k_B ^{-2}$ ', fontsize=16)
ax1.set_title("Heat Capacity vs  Temperature", fontsize=16)
"""ax1.legend(loc='upper center', bbox_to_anchor=(0.66, 1.00),
          ncol=2, fancybox=True, shadow=True)"""



plt.show()  #uncomment if one want to show plot
#plt.savefig("T=0.05_v2.png") #saves plot as png
