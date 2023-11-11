def find_addition_chains(n):
    def backtrack(curr_chain, current_sum):
        nonlocal chains, n

        if current_sum == n:
            chains.append(curr_chain[:])
            return

        for num in curr_chain:
            next_sum = current_sum + num
            if next_sum <= n:
                curr_chain.append(next_sum)
                backtrack(curr_chain, next_sum)
                curr_chain.pop()

    chains = []
    backtrack([1], 1)
    return chains

# Example usage:
ns = [2,3,4,5,6,7,10]
for n in ns:
    all_chains = find_addition_chains(n)
    length =[]

    for chain in all_chains:
        #print(len(chain))
        length.append(len(chain))
    print('Minimum length addition chain for the given positive integer '+ str(n)+' is '+str(min(length)-1))
