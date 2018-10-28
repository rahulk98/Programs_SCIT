import numpy as np
import matplotlib.pyplot as plt
for i in range(3):
    poisson = np.random.poisson(5,1000)
    np.savetxt("Poisson dataset-" + str(i), poisson)
    plt.hist(poisson, normed=True)
    plt.savefig('Poisson histogram '+str(i+1)+'.png')
    plt.show()

# from the three histograms we can infer that the data points are concentrated in the region of mean which is 5.