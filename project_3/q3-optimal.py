#ref: https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
import pandas as pd
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def optimal_bst(keys, freq):
    n = len(keys)

    # Initialize cost and root tables
    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    # Initialize cost table for single keys
    for i in range(n):
        cost[i][i] = freq[i]

    # Build the cost table
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            cost[i][j] = float('inf')

            # Try making each key in the sequence the root
            for r in range(i, j + 1):
                c = cost[i][r - 1] if r > i else 0
                c += sum(freq[i:j + 1]) + cost[r + 1][j] if r < j else 0

                if c < cost[i][j]:
                    cost[i][j] = c
                    root[i][j] = r

    return cost, root

def construct_optimal_bst(keys, root, i, j):
    if i > j:
        return None

    root_index = root[i][j]
    root_node = Node(keys[root_index])

    root_node.left = construct_optimal_bst(keys, root, i, root_index - 1)
    root_node.right = construct_optimal_bst(keys, root, root_index + 1, j)

    return root_node

def search_optimal_bst(root, key, tolerance=1):
    while root is not None:
        if abs(key - root.key) < tolerance:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None

data = pd.read_csv('worldcities.csv')

# Filter data for cities in Norway
norway_data = data[data['country'] == 'Norway']

# Access the 'lat' column directly without unique sorting
latitudes = norway_data['lat'].tolist()
# Example usage
frequency_dict = {lat: norway_data[norway_data['lat'] == lat].shape[0] for lat in latitudes}
#print(len(frequency_dict))
keys = list(frequency_dict.keys())
freq = list(frequency_dict.values())
#keys=[]
#freq=[]
for i in range(50,100):
    keys.append(i)
    freq.append(1)

cost_table, root_table = optimal_bst(keys, freq)
optimal_bst_root = construct_optimal_bst(keys, root_table, 0, len(keys) - 1)

# some Norwegian cities latitudes in the csv,and int 1-11 for wrong case test
test=[59.9133, 60.3894, 58.97, 58.8517, 63.4297, 59.8833, 58.1472, 59.7378, 59.2081, 67.2827,  68.2353, 69.2294, 69.7269, 64.8619, 69.6956, 60.63,58.2969, 61.5996, 62.3564, 64.4656,68.2353, 69.2294, 69.7269, 64.8619, 69.6956, 60.63,1,2,3,4,5,6,7,8,9,10,11,70.6634]
#all norwegian cities in the csv
#test=[59.9133, 60.3894, 58.97, 58.8517, 63.4297, 59.8833, 58.1472, 59.7378, 59.2081, 67.2827, 58.4608, 69.6828, 62.7375, 60.7945, 64.0148, 59.2053, 59.1306, 59.8331, 59.75, 59.2981, 59.2858, 62.474, 59.4592, 59.8989, 59.4464, 59.1156, 61.0242, 59.1264, 59.7419, 60.4667, 61.1167, 59.7925, 59.6694, 59.8675, 58.8561, 60.3475, 59.7647, 59.1343, 60.0731, 68.8011, 59.0811, 59.3799, 58.8922, 63.475, 59.7336, 59.2792, 59.2011, 60.8819, 60.6494, 59.6603, 59.4208, 60.7957, 58.8308, 58.7772, 59.8086, 60.2269, 58.7228, 59.8081, 66.3128, 59.575, 63.1104, 59.9871, 58.15, 60.1905, 69.6442, 59.3747, 60.1667, 59.6989, 60.7025, 60.6247, 58.0267, 69.9689, 58.3106, 60.2456, 63.793, 59.5861, 63.3728, 59.7798, 68.4363, 59.0197, 60.4411, 59.6667, 59.0633, 61.1684, 58.3405, 63.4712, 59.6294, 58.7354, 61.2297, 59.7794, 59.0017, 59.95, 59.24, 59.2801, 69.3836, 58.4497, 59.5369, 58.0942, 59.7639, 59.3617, 60.8836, 62.2003, 62.1468, 68.6982, 58.1333, 59.0955, 58.8869, 63.7465, 61.4522, 59.5936, 65.837, 58.0947, 67.2594, 62.6665, 60.2528, 58.2969, 61.5996, 62.3564, 64.4656, 70.6634, 70.0803, 68.2353, 69.2294, 69.7269, 64.8619, 69.6956, 60.63]
for i in test:
    result = search_optimal_bst(optimal_bst_root, i)

    if result:
        latitude_to_find = i  # Replace this with the latitude you want to search for

        # Find the city name with the given latitude
        city_name = norway_data[norway_data['lat'] == latitude_to_find]['city'].values
        if city_name.size>0:
            print(f"Latitude {i} found in the tree.Corresponding city:{city_name} ")
        else:
            print(f"Latitude {i} not found in the tree.")
            
    else:
        print(f"Latitude {i} not found in the tree.")
