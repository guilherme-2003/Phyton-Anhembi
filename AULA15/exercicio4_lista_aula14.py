import numpy as np

iris1 = np.loadtxt('iris1.data', delimiter=',')
iris2 = np.loadtxt('iris2.data', delimiter=',')

print(iris1.shape)
print(iris2.shape)

iris = np.vstack( (iris1, iris2) )

np.savetxt('iris.data', iris, delimiter=',')
print('Arquivo salvo com sucesso!')