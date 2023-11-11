#ref: https://www.geeksforgeeks.org/python-program-for-binary-search/
import pandas as pd

# Load the data
data = pd.read_csv('worldcities.csv')

# Extract unique latitude values and sort them
unique_latitudes = sorted(data['lat'].unique().tolist())

# Binary search implementation
def binary_search(arr, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == x:
            return data[data['lat'] == x]['city'].values[0]
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)
        else:
            return binary_search(arr, mid + 1, high, x)
    else:
        return None

# Example usage:
test=[59.9133, 60.3894, 58.97, 58.8517, 63.4297, 59.8833, 58.1472, 59.7378, 59.2081, 67.2827,  68.2353, 69.2294, 69.7269, 64.8619, 69.6956, 60.63,58.2969, 61.5996, 62.3564, 64.4656,68.2353, 69.2294, 69.7269, 64.8619, 69.6956, 60.63,1,2,3,4,5,6,7,8,9,10,11,0]
for i in test:    
    target_latitude =  i # Example latitude value
    result_city = binary_search(unique_latitudes, 0, len(unique_latitudes) - 1, target_latitude)
    if result_city:
        print(f"The corresponding city for latitude {target_latitude} is {result_city}.")
    else:
        print(f"No city found for latitude {target_latitude}.")
