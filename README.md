# Gaussian-elemination.py
This file contains Gaussian elemination. A method to find the inverse of the matrix. It does two operations, forward substitution and backward substitution.
to find the inverse of the matrix:
change the A matrix with [a b 1 0;c d 0 1] . the [1 0; 0 1] is needed for finding the inverse of the matrix.the last two columns represent the inverse.

to find the solution to the matrix:
Ax=b 
[A b]. the last column represent the solution to the matrix.

note this implementation doesn't require the numpy or any dependencies and run in python2.7
