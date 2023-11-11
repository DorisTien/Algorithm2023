#ref: https://www.geeksforgeeks.org/python-program-for-merge-sort/
import pandas as pd

# Load the data
data = pd.read_csv('worldcities.csv')

# Extract unique latitude values
unique_latitudes = data['lat'].unique().tolist()

def merge(arr, l, m, r, count):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        count += 1
        k += 1

    # Copy the remaining elements of L[], if there are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    return count

# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r, count=0):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for large l and h
        m = l + (r - l) // 2

        # Sort first and second halves
        count = mergeSort(arr, l, m, count)
        count = mergeSort(arr, m + 1, r, count)
        count = merge(arr, l, m, r, count)
    return count


original_order_merges = mergeSort(unique_latitudes, 0, len(unique_latitudes) - 1)
#(ii) Count the number of merges needed to sort the dataset.
import random
random.shuffle(unique_latitudes)

random_order_merges = mergeSort(unique_latitudes, 0, len(unique_latitudes) - 1)

print("Merges for the original order:", original_order_merges)
print("Merges for the random order:", random_order_merges)

#(iii) Implement a proper merge sort algorithm so that the (latitude, longitude) pairs are in an ordered list

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    return ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5

# Merge sort function with Euclidean distance
def merge_sort_distance(arr, reference_point, distance_func):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort_distance(left_half, reference_point, distance_func)
        merge_sort_distance(right_half, reference_point, distance_func)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            dist_left = distance_func(left_half[i], reference_point)
            dist_right = distance_func(right_half[j], reference_point)

            if dist_left < dist_right:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Example usage
# Ref point is Grimstad
grimstad=(58.3405,8.5934)
coordinates_list = list(zip(data['lat'], data['lng']))
merge_sort_distance(coordinates_list, grimstad, euclidean_distance)

# Display the sorted coordinates (nearest 20 to Grimstad)
for i in range(20):
    print(coordinates_list[i])




