import numpy as np

meu_array = np.array([[1,5,2,5,4], [10,8,11,0,10]], dtype='int')

maiores = meu_array[meu_array > 3]

print(maiores)
