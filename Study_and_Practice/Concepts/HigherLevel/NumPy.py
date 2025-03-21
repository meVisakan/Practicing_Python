import time
import numpy as np

start = time.time()
a = [i for i in range(1080000000)]
b = [i for i in range(1080000000, 2000000000)]
c = a + b

print(time.time() - start)      # Took about 157s

n_start = time.time()
na = np.arange(1000000000)
nb = np.arange(1000000000, 2000000000)
nc = na + nb

print(time.time() - n_start)     # Took about 9s
