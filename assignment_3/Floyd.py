import numpy as np
from sys import maxsize
#defination of inf number 
inf=  maxsize
#algo 3.4
def floyd (n, weight_matrix,distance_matrix, p_matrix):
    for i in range (n):
        for j in range (n):       
            p_matrix[i][j]=[]     # Initialize the element as an empty list
    distance_matrix[:] = weight_matrix
    for k in range (n):
        for i in range (n):
            for j in range (n):
                if distance_matrix[i][k]+ distance_matrix[k][j]<distance_matrix[i][j]:
                    p_matrix[i][j].append(k)
                    distance_matrix[i][j]= distance_matrix[i][k]+ distance_matrix[k][j]

def make_p_matrix (n):
    p_matrix = np.empty((n,n),dtype=object)  # Create a NumPy array to store lists as elements
    return p_matrix

#algo 3.5
def print_via_point (x,y,p_matrix):
    print ('From point '+ str(x) + ' to point '+ str(y) + ', you need to go through the following point(s):' )
    for item in p_matrix[x][y]:
        print (item)


if __name__ == '__main__':
#Define the empty matrix for distance
    d_matrix = np.empty((7, 7))
    w_matrix = [
    [0, 4, inf,inf, inf,10,inf],
    [3, 0, inf,18,inf,inf,inf],
    [inf, 6, 0, inf,inf,inf,inf],
    [inf, 5,15,0,2,19,5],
    [inf,inf,12,1,0,inf,inf],
    [inf,inf,inf,inf,inf,0,10],
    [inf,inf,inf,8,inf,inf,0]
    ]
    p= make_p_matrix(7)
    floyd(7,w_matrix,d_matrix,p)
    print(d_matrix[6][2])
    print_via_point(6,2,p)