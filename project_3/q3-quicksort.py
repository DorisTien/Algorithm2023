#ref: https://www.geeksforgeeks.org/python-program-for-quicksort/
import pandas as pd

# Load the data
data = pd.read_csv('worldcities.csv')

# Extract unique latitude values
unique_latitudes = data['lat'].unique().tolist()



# Function to find the partition position
def partition(array, low, high, count):
    # choose the rightmost element as pivot
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
            count += 1
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    count += 1
    return i + 1, count

# function to perform quicksort
def quickSort(array, low, high, count):
    if low < high:
        pi, count = partition(array, low, high, count)
        count = quickSort(array, low, pi - 1, count)+quickSort(array, pi + 1, high, count)
    return count

# Sort the unique latitude values using quicksort
count = quickSort(unique_latitudes,0,len(unique_latitudes)-1,0)
#print("Sorted Latitudes:", unique_latitudes)
print("Number of Comparisons of original:", count)


#(ii) Count the number of comparisons needed to sort the dataset. 
import random
random.shuffle(unique_latitudes)
count = quickSort(unique_latitudes,0,len(unique_latitudes)-1,0)
print("Number of Comparisons of the random order:", count)

#(iii) Quick Sort for (latitude, longitude) Pairs 
def euclidean_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5

def quick_sort_distance(arr, reference_point, distance_func):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        pivot_distance = distance_func(pivot, reference_point)

        less = [x for x in arr[1:] if distance_func(x, reference_point) < pivot_distance]
        greater = [x for x in arr[1:] if distance_func(x, reference_point) >= pivot_distance]

        return quick_sort_distance(less, reference_point, distance_func) + [pivot] + quick_sort_distance(greater, reference_point, distance_func)

# Convert DataFrame columns to a list of (latitude, longitude) pairs
coordinates_list = list(zip(data['lat'], data['lng']))

# Ref point is Grimstad
grimstad=(58.3405,8.5934)

# Apply Quick Sort with Euclidean distance
sorted_coordinates = quick_sort_distance(coordinates_list, grimstad, euclidean_distance)

# Display the sorted coordinates (nearest 20 to Grimstad)
for i in range(20):
    print(sorted_coordinates[i])



