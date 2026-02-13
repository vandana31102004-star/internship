import numpy as np 
a=np.array([[1,2,3,],
            [4,5,6]])
b=np.array([10,20,30])
result=a+b
print(result)
arr=np.random.rand(10000)
squared=arr**2

arr=np.arange(12)
reshaped=arr.reshape(3,4)
print(reshaped)
a=np.array([[1,2]])
b=np.array([[3,4]])
vstacked=np.vstack((a,b))
print(vstacked)

a=np.array([[1,2],
            [3,4]])
b=np.array([[5,6],
            [7,8]])
print("array A:")
print(a)
print("\nAraay B:")
print(b)

v_result=np.vstack((a,b))
print("\nAfter vstack (Vertical Stack):")
print(v_result)
h_result = np.hstack((a, b))
print("\nAfter hstack (Horizontal Stack):")
print(h_result)


data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=0))


data = np.array([[10, 20, 30],
                 [40, 50, 60]])

print(np.mean(data))
print(np.mean(data, axis=1))

