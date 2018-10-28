import numpy as np
import matplotlib.pyplot as plt
for i in range(3):
    normal = np.random.normal(0, 5,1000)
    np.savetxt("Normal dataset" + str(i), normal)
    plt.hist(normal, normed=True)
    plt.savefig('Normal Histogram '+str(i+1)+'.png')
    plt.show()


# In this case also we can see that 
# the distribution is concetrated around 
# the mean of the normal distribution