# # Write a NumPy program to create an array of all even integers from 30 to 70
import numpy as np
# creating array of even numbers from 30 to 70
even_number=np.arange(30,70,2);
print(even_number)

# write a NumPy program to generate an array of 15 random numbers from a standard normal
# distribution.

random_Array=np.random.normal(0,1,15)
print(random_Array)

# # How to compute the cross-product of two matrices in NumPy?
metrixA=np.array([[1,2,3],
                  [4,5,6]
                  ])
metrixB=np.array([[11,12,13],
                  [14,15,16]
                  ])

cross_mul=np.cross(metrixA,metrixB)
print(cross_mul)

# How to compute the determinant of an array using NumPy?

matrix = np.array([[11, 12, 13],
                   [14, 15, 16],
                   [17, 18, 19]])

det = np.linalg.det(matrix)

# print(det)

# How to create a 3x3x3 array with random values using NumPy?
random_arr=np.random.random((3,3,3))
# print(random_arr)


# How to create a 5x5 array with random values and find the minimum and maximum values using
# NumPy?
fRandom=np.random.random((5,5))
print(fRandom)

# How to compute the mean, standard deviation, and variance of a given array along the second axis in
# NumPy?

# make an array
array = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])
# mean
print(np.mean(array,axis=1))
# # standard deviation
print(np.std(array,axis=1))
# # varience
print(np.var(array,axis=1))
