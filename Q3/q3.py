import numpy as np
import matplotlib.pyplot as plt
poisson = np.random.poisson(5, 1000)
normal = np.random.normal(0, 5, 1000)
data = []
for m in range(100):
    np.random.shuffle(poisson)
    np.random.shuffle(normal)
    d1 = poisson[:100]
    d2 = normal[:100]
    for i in range(100):
        data.append((d1[i] + d2[i])/2)

np.savetxt("Dataset", data)
plt.hist(data, normed=True)
plt.savefig("Q3.png")
plt.show()