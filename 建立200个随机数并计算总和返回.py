import numpy as np

averange = 0
while averange != 160:
    rand_array = np.random.randint(100, 201, 200)
    averange = sum(rand_array)/len(rand_array)
    if averange == 160:
        print(rand_array)
