from sys import maxsize
inf = maxsize
undef = None

def upper_matrix(input_matrix):
    n= len(input_matrix)
    list_edge=[]
    for i in range (1,n):
        for j in range (1,n):
            if j>i:
              value =input_matrix[i][j]
              item=(i,j,value)
              list_edge.append(item)
    return list_edge

def sort_list (list):
    #sort the list based on the 3nd elem of each sublist
    sorted_list_3elem = sorted(list, key=lambda x: x[2])
    return sorted_list_3elem



def kruskal(input_marix):
    listof_i_j_weight = upper_matrix(input_marix)
    listof_i_j_weight_sort = sort_list(listof_i_j_weight)
    n= len(input_marix)-1
    parent = list(range(n + 1))  # Initialize each vertex as its own parent
    def find(v):
        if parent[v] == v:
            return v
        parent[v] = find(parent[v])
        return parent[v]

    def union(v1, v2):
        root1 = find(v1)
        root2 = find(v2)
        if root1 != root2:
            parent[root1] = root2

    mst_edges = []
    mst_weight = 0

    for edge in listof_i_j_weight_sort:
        u, v, weight = edge
        if find(u) != find(v):  # Check for a cycle
            mst_edges.append(edge)
            mst_weight += weight
            union(u, v)
            print('Edge ('+str(u)+','+str(v)+') with weight '+str(weight)+' is accepted, so add it to F :)')
        else:
            if weight==maxsize:
                weight='infinity'
            
            print('Edge ('+str(u)+','+str(v)+') with weight '+str(weight)+' is rejected :(')

    return mst_edges, mst_weight




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

    a,b=kruskal (input_matrix1)
    print('F={')
    for elem in a:
        print((elem[0],elem[1]))
    print('}')

    print('Calculation and Result for 2nd MST:')
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
    c,d=kruskal (input_matrix2)
    print('F={')
    for elem in c:
        print((elem[0],elem[1]))
    print('}')
