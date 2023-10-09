import networkx as nx
'''
refernce: https://www.geeksforgeeks.org/networkx-python-software-package-study-complex-networks/
https://towardsdatascience.com/graph-coloring-with-networkx-88c45f09b8f4
'''
def is_promising(node, color, graph, colors_list):
    for neighbor in graph.neighbors(node):
        if colors_list[neighbor] == color:
            return False
    return True
def solution(graph, colors_list,node,color_num):
    if node==len(graph):
        return True
    for color in range(1,color_num+1):    
        if is_promising(node,color,graph,colors_list):
            colors_list[node]=color
            if solution(graph, colors_list,node+1,color_num):
                return True
    return False
def if_solution(colorlist):
    condition =True
    for i in range(1, len(colorlist)):
        if colorlist[i]==0:
            print(colorlist[i])
            condition= False
    return condition

if __name__ == '__main__':
    mygraph = nx.Graph()
    #The amount of different colors
    color_amount=3
    # Add nodes
    mygraph.add_nodes_from([0,1,2,3,4,5,6,7])

    # Add edges
    mygraph.add_edges_from([(1, 2), (1, 3), (1, 4), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3,6),(4,5),
                      (5,6),(5,7),(6,1)])
    colorlist =[0]*len(mygraph)
    solution(mygraph, colorlist,1,color_amount)
    if if_solution(colorlist):
        print('Solution is as follow: ')
        for j in range(1, len(mygraph)):
            print('Area A'+str(j)+' is in frequency No.'+str(colorlist[j]))
    else:
        print('No solutions, please add more frequency or (frequencies)!')