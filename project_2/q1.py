def max_result_tree(lst, current_int, current_result, index):
    if index == len(lst):
        return current_result

    if lst[index] != current_int:
        # Swap case
        swap_result = max_result_tree(lst, lst[index], current_result - 1, index + 1)
        # keep your own relic case
        skip_result = max_result_tree(lst, current_int, current_result, index + 1)
        return max(swap_result, skip_result)
    else:
        # you must exchange the relic when the creature has the same relic to get the max result
        return max_result_tree(lst, current_int, current_result + 1, index + 1)

# Example usage
#lst represents the relices of the i creatures, '1' is the Whispering Oak Leaf, '2' is the Sparkling Crystal, and '3' is the Ember Phoenix Feather
lsts = [[1,2,3],[1,2,3,1,2,1,2,1,2,2,2,2,2],[2,2,2],[1,1,1],[3,3,3],[1,2,3,1,2,3],[1,2,3,1,2,2,2,2,2,3,3,3] ]
for lst in lsts:
    lst.insert(0,1)# the initial situation is that you have the Whispering Oak Leaf, which I ues '1' to represent
    result = max_result_tree(lst, lst[0], 0, 0)
    print('Test case:'+str(lst))
    print("Maximum Result:", result)
