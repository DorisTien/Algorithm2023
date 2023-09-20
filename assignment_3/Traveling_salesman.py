import itertools
from sys import maxsize
#To calculate the begining city to the end city and then go back
def total_distance(via_points,weight_matrix):
    total_viapoints = len (via_points)
    total_distance =0
    for i in range(total_viapoints-1):
        total_distance+= weight_matrix[via_points[i]][via_points[i+1]]
    total_distance += weight_matrix[via_points[-1]][via_points[0]] #back home
    return total_distance

def traveling_salesman(weight_matrix):
    routine =None
    minimun_distance = maxsize
    viapoint_list = list (range(len(weight_matrix)))
    #Each elem represents a different permutation of the cities.
    for elem in itertools.permutations(viapoint_list): 
        distance=total_distance(elem,weight_matrix)
        if distance<minimun_distance:
            minimun_distance = distance
            routine= elem
    return routine, minimun_distance

if __name__ == '__main__':
  distances = [
        [0, 8, 13, 18, 20],
        [3, 0, 7, 8, 10],
        [4, 11, 0, 10, 7],
        [6, 6, 7, 0, 11],
        [10, 6, 2, 1, 0]
    ]
  
  optimal_tour, min_distance = traveling_salesman(distances)
  print("Optimal Tour:", optimal_tour)
  print("Minimum Distance:", min_distance)