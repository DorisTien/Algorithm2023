class Solution:
    def __init__(self):
        self.gray_code_result = []
        self.visited = set()
        self.visited_count = 0
        self.promising_count = 0

    def grayCode(self, n):
        self.backTrack(0, [], n, 2 ** n)
        return self.gray_code_result, self.visited_count, self.promising_count

    def backTrack(self, state, code, n, size):
        if len(code) >= size:
            return
        code.append(state)
        self.visited.add(state)
        self.visited_count += 1
        for i in range(n):
            self.promising_count += 1
            new_state = self.flipBit(state, i)
            if len(code) == size:
                self.gray_code_result = list(code)
            if new_state not in self.visited:
                self.backTrack(new_state, code, n, size)
    

    def flipBit(self, state, i):
        return state ^ (1 << i)

# Testing the Solution class with an example
ns=[2,3,4,5,6]

for n in ns:
    print('****** n='+str(n)+' ******')
    solution = Solution()
    result, visited_count, promising_count = solution.grayCode(n)
    print("Visited Count:", visited_count)
    print("Promising Count:", promising_count)
