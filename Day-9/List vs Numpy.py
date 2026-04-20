import numpy as np

import time
x = time.time()

list1 = [i for i in range(100000000)]
list2 = [i for i in range(100000000,200000000)]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
print(f"Time taken through List = ",time.time()-x)


# array1 = np.arange(100000000)
# array2 = np.arange(100000000,200000000)

# array3  = array1+array2
# print(f"Time taken through Numpy = ",time.time()-x)