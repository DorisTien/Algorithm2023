#ref: https://www.geeksforgeeks.org/optimal-binary-search-tree-dp-24/
import pandas as pd

# Load the data
data = pd.read_csv('worldcities.csv')

# Filter data for cities in Norway
norway_data = data[data['country'] == 'Norway']

# Access the 'lat' column directly without unique sorting
latitudes = norway_data['lat'].tolist()
#latitudes = [round(10000*x) for x in latitudes]

print(latitudes)
# Initialize a frequency dictionary for dynamic frequency construction
frequency_dict = {lat: norway_data[norway_data['lat'] == lat].shape[0] for lat in latitudes}
print(len(frequency_dict))
keys = list(frequency_dict.keys())
freq = list(frequency_dict.values())

print(keys)
print(freq)
    # Build the cost table
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


# Utility function to calculate the sum of frequencies
def sum(freq, i, j):
    s = 0
    for k in range(i, j + 1):
        s += freq[k]
    return s


# Example usage
class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

#recursion for tree
def create_tree(keys, freq):
    if not keys:
        return None

    n = len(keys)
    mid = n // 2
    root = Node(keys[mid])
    root.left = create_tree(keys[:mid], freq[:mid])
    root.right = create_tree(keys[mid + 1:], freq[mid + 1:])
    return root
def print_tree(node, level=0, label='Root'):
    if node is not None:
        print(' ' * (level * 4) + f'[{label}] {node.val}')
        print_tree(node.left, level + 1, 'L')
        print_tree(node.right, level + 1, 'R')

#tolerance = 1e-5  # Set the tolerance as per your requirement

def search(root, key):
    if root is None or root.val == key:
        return root

    # If the key is smaller than the root's key,
    # then it lies in the left subtree
    if key < root.val:
        return search(root.left, key)

    # If the key is larger than the root's key,
    # then it lies in the right subtree
    return search(root.right, key)


#test=[59.7925,60.1905,58.8517, 59.8989]
#test= [59.9133, 60.3894, 58.97, 58.8517, 63.4297, 59.8833, 58.1472, 59.7378, 59.2081, 67.2827, 58.4608, 69.6828, 62.7375, 60.7945, 64.0148, 59.2053, 59.1306, 59.8331, 59.75, 59.2981, 59.2858, 62.474, 59.4592, 59.8989, 59.4464, 59.1156, 61.0242, 59.1264, 59.7419, 60.4667, 61.1167, 59.7925, 59.6694, 59.8675, 58.8561, 60.3475, 59.7647, 59.1343, 60.0731, 68.8011, 59.0811, 59.3799, 58.8922, 63.475, 59.7336, 59.2792, 59.2011, 60.8819, 60.6494, 59.6603, 59.4208, 60.7957, 58.8308, 58.7772, 59.8086, 60.2269, 58.7228, 59.8081, 66.3128, 59.575, 63.1104, 59.9871, 58.15, 60.1905, 69.6442, 59.3747, 60.1667, 59.6989, 60.7025, 60.6247, 58.0267, 69.9689, 58.3106, 60.2456, 63.793, 59.5861, 63.3728, 59.7798, 68.4363, 59.0197, 60.4411, 59.6667, 59.0633, 61.1684, 58.3405, 63.4712, 59.6294, 58.7354, 61.2297, 59.7794, 59.0017, 59.95, 59.24, 59.2801, 69.3836, 58.4497, 59.5369, 58.0942, 59.7639, 59.3617, 60.8836, 62.2003, 62.1468, 68.6982, 58.1333, 59.0955, 58.8869, 63.7465, 61.4522, 59.5936, 65.837, 58.0947, 67.2594, 62.6665, 60.2528, 58.2969, 61.5996, 62.3564, 64.4656, 70.6634, 70.0803, 68.2353, 69.2294, 69.7269, 64.8619, 69.6956, 60.63]
test=latitudes
root = create_tree(keys, freq)
print_tree(root)
for i in test:
    #root = create_tree(keys, freq)
    #print_tree(root)
    search_result = search(root, i)
    if search_result:
        #city_name = norway_data.loc[norway_data['lat'] == search_result.val, 'city'].values[0]
        print(f"Key {search_result.val} found in the tree. ")
    #else:
        print("Key not found in the tree.")
        
