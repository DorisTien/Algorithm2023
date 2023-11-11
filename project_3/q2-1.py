#ref: https://leetcode.com/problems/gray-code/solutions/3779472/backtracking-bit-manipulation-java/
# https://www.youtube.com/watch?v=OaH5Zf6zVqc&t=16s
import time
class Solution:
    def __init__(self):
        self.gray_code_result = []
        self.visited = set()

    def grayCode(self, n):
        self.backTrack(0, [], n, 2 ** n)
        return self.gray_code_result

    def backTrack(self, state, code, n, size):
        if len(code) >= size:
            return
        code.append(state)
        self.visited.add(state)
        for i in range(n):
            new_state = self.flipBit(state, i)
            if len(code) == size :
                self.gray_code_result = list(code)
            if new_state not in self.visited:
                self.backTrack(new_state, code, n, size)

    #change at i th position. IF 1,THEN 0. IF 0, THEN 1.
    def flipBit(self, state, i):
        return state ^ (1 << i)

import timeit

# Placeholder for Solution class
class Solution:
    def grayCode(self, n):
        # Your implementation here
        pass

ns = [2, 3, 4, 8]
processing_times = []

for n in ns:
    print('****************** Gray code of ' + str(n) + ' ******************')
    solution = Solution()
    stmt = "solution.grayCode(n)"
    setup = "from __main__ import solution, n"
    # Measure the execution time
    execution_time = timeit.timeit(stmt, setup=setup, number=1)
    processing_times.append(execution_time)
    print(f"Processing time: {execution_time} seconds")

print("List of processing times:", processing_times)







