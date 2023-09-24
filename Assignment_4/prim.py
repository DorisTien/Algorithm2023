import numpy as np
from sys import maxsize
inf = maxsize
undef = None

def find_min(list1,list2,matrix):
    min = maxsize
    a= b = None
    for elem1 in list1:
        for elem2 in list2:
            if 0<matrix[elem1][elem2]<min:
                min= matrix[elem1][elem2]
                a= elem1
                b= elem2
    return a,b,min
def prim (n, weighted_matrix):
    #List for vertexes start with 1
    Y=[1]
    #list for edges
    F = []
    Z= list(range(2,n+1))

    print('Begin with Y = {'+str(Y[0])+'}, F = { }.')
    while len(Y)< n:
        a,b , min = find_min(Y,Z,weighted_matrix)         
        Z.remove(b)
        F.append((a,b))
        Y.append(b)
        print('Nearest vertex to Y is v'+str(b)+' (distance: '+
                str(weighted_matrix[a][b])+'), so add v'+str(b)+' to Y and'+str((a,b))
                +'to F.')
    return F,Y

if __name__ == '__main__':
    print('Calculation and Result for 1st MST:')

    input_matrix1 = [
    [undef, undef, undef, undef, undef, undef],
    [undef, 0, 1, 3, inf, inf],
    [undef, 1, 0, 3, 6, inf],
    [undef, 3, 3, 0, 4, 2], 
    [undef, inf, 6, 4, 0, 5], 
    [undef, inf, inf, 2, 5, 0]
]

    F_1, Y_1 = prim(5, input_matrix1)
    print("Edges in MST: ", F_1)
    print("Vertices in MST: ", Y_1)


    print('Calculation and Result for the 2nd MST:')
    input_matrix2 =[
    [undef,undef,undef,undef,undef,undef,undef,undef,undef,undef,undef],
    [undef,0,32,inf,17,inf,inf,inf,inf,inf,inf], #1
    [undef,32,0,inf,inf,45,inf,inf,inf,inf,inf], #2
    [undef,inf,inf,0,18,inf,inf,5,inf,inf,inf], #3
    [undef,17,inf,18,0,10,inf,inf,3,inf,inf], #4
    [undef,inf,45,inf,10,0,28,inf,inf,25,inf],   #5
    [undef,inf,inf,inf,inf,28,0,inf,inf,inf,6], #6
    [undef,inf,inf,5,inf,inf,inf,0,59,inf,inf], #7
    [undef,inf,inf,inf,3,inf,inf,59,0,4,inf], #8
    [undef,inf,inf,inf,inf,25,inf,inf,4,0,12], #9
    [undef,inf,inf,inf,inf,inf,6,inf,inf,12,0] #10
  ]
    F_2, Y_2=prim(10,input_matrix2)
    print("Edges in MST: ", F_2)
    print("Vertices in MST: ", Y_2)