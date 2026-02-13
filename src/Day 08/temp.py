import numpy as np
a0=np.array(10)
print(a0)
print("Dimensions:",a0.ndim)


a1=np.array([1,2,3,4])
print(a1)
print("Dimensions:",a1.ndim)

a2=np.array([[1,2,3],
             [4,5,6]])
print(a2)
print("Dimensions:",a2.ndim)


a3 = np.array([
    [[1, 2, 3],
     [4, 5, 6]],

    [[7, 8, 9],
     [10, 11, 12]]
])

print("3D Array:")
print(a3)


print("\nNumber of dimensions:", a3.ndim)
print("Shape of array:", a3.shape)

