import numpy as np
def minmult(n,d,p):
    return n

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")  # Print each element followed by a space
        print()  # Move to the next line for the next row

def set_matrix_to_value(matrix, value):
    # Iterate through the rows and columns of the matrix
    for i in range(matrix.shape[0]):  # Number of rows
        for j in range(matrix.shape[1]):  # Number of columns
            matrix[i][j] = value

if __name__ == '__main__':
    n= 5
    d = [10,4,5,5,20,20,2,2,50]
    p = np.empty((n, n), dtype=int)
    m = np.empty((n, n), dtype=int)
    set_matrix_to_value(p,-1)
    set_matrix_to_value(m,-1)
    for diagonal in range(0,n):
        for i in range (0,n-diagonal):
            j = i+diagonal
            list_mikj =[]
            for k in range(i,j):           
                mikj = m[i][k]+m[k+1][j] + d[i-1]*d[k]*d[j]
                list_mikj.append((mikj,k))


            if list_mikj:  # Check if list_mikj is not empty
                min_mikj = min(list_mikj, key=lambda x: x[0])
                m[i][j] = min_mikj[0]
                p[i][j] = min_mikj[1]
            else:
                # Handle the case where list_mikj is empty (you can set default values or raise an error)
                m[i][j] = 0  # Set a default value of 0
                p[i][j] = -1  # Set a default value of -1

print(m[0][n-1])
print(p[0][n-1])
print_matrix(p)

            
            