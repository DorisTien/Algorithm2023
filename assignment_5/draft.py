# Sample list with repeated tuples
original_list = ['(1,4)', '(3,2)', '(5,0)', '(0,5)', '(2,3)', '(4,1)']
['(2,3)', '(5,0)', '(1,4)', '(4,1)', '(0,5)', '(3,2)']
['(3,2)', '(0,5)', '(4,1)', '(1,4)', '(5,0)', '(2,3)']
['(4,1)', '(2,3)', '(0,5)', '(5,0)', '(3,2)', '(1,4)']

# Convert the strings to tuples and store them in a set
unique_set = set(tuple(eval(item)) for item in original_list)

# Convert the unique set of tuples back to a list
unique_list = [str(item) for item in unique_set]

# Sort the unique list to get a consistent order
unique_list.sort()

# Print the unique list
for item in unique_list:
    print(item)