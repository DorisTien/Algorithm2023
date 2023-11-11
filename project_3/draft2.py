import pandas as pd

class Node:
    def __init__(self, key, city):
        self.key = key
        self.city = city
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

def construct_optimal_bst(keys, cities, root, i, j):
    if i > j:
        return None

    root_index = root[i][j]
    root_node = Node(keys[root_index], cities[root_index])

    root_node.left = construct_optimal_bst(keys, cities, root, i, root_index - 1)
    root_node.right = construct_optimal_bst(keys, cities, root, root_index + 1, j)

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

# Access the 'lat' and 'city' columns directly without unique sorting
latitudes_and_cities = norway_data[['lat', 'city']].values.tolist()

# Extract latitudes and city names
latitudes = ['lat' in latitudes_and_cities]
cities = [x[1] for x in latitudes_and_cities]

# Example usage
keys = latitudes
freq = [1] * len(keys)

cost_table, root_table = optimal_bst(keys, freq)
optimal_bst_root = construct_optimal_bst(keys, cities, root_table, 0, len(keys) - 1)

# Search for a key in the optimal BST
for i in keys:
    result = search_optimal_bst(optimal_bst_root, i)

    if result:
        print(f"Key {i} found in the tree. Corresponding city: {result.city}")
    # else:
    #     print(f"Key {i} not found in the tree.")
