import numpy as np
import matplotlib.pyplot as plt

def main():

    data = np.loadtxt("readableFit.txt", dtype = float)
    magnitude = data[:,1]
    magerr = data[:,2]
    phase = data[:,3]
    oc = np.median(data[:,5])
    model = data[:,4] + oc

    plt.errorbar(phase, magnitude, yerr = magerr, color= 'b', marker = 'o', ls = 'None', markersize = 2, elinewidth = 1)
    plt.plot(phase, model, 'r')
    plt.gca().invert_yaxis()
    plt.xlabel("Phase [days]")
    plt.ylabel("Magnitude")
    plt.show()




main()
