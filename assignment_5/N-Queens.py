#This code is based on https://www.youtube.com/watch?v=A80YzvNwqXA&t=925s, which is provided on Canvas
class Solution:
    def __init__(self, listp, n):
        # Initialize attributes here
        self.listp = n*[0]
    
    def solveNQueens(self, n):
        print(str(n)+' Queens Problem: ')        
        solutions = []
        state = []
        self.search(state, solutions, n,0)
        return solutions
    def is_valid_state(self, state, n):
        # check if it is a valid solution
        return len(state) == n
    def get_candidates(self, state, n):
        #if the state is empty
        if not state:
            return range(n)
        # find the next position in the state to populate
        position = len(state)
        candidates= set(range(n))
        #prune down
        for row, colum in enumerate(state):
            candidates.discard(colum)
            dist= position-row
            #discard diagonal
            candidates.discard(colum+dist)
            candidates.discard(colum-dist)
        return candidates
    
    #promissing_list = [0] * n
    def search (self, state, solutions, n,level):
        
        if self.is_valid_state(state,n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return 

        for candidate in self.get_candidates(state,n):
            #recurse
            state.append(candidate)
            #print('promissing +1:'+str(level)) # promising node of each level 
            self.listp[level] +=1
            self.search(state,solutions,n,level+1)
            state.pop()
       

    def state_to_string(self, state, n):
        ret = []
        for i in state:
            string = '('+str(i+1) + ',' + str(n - i)+')'
            ret.append(string)
        return ret

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for i in range(2,7):
        n = i
        solution_instance = Solution(list,n)
        # Call the 'solveNQueens' method to find solutions
        solutions = solution_instance.solveNQueens(n)

        non_p_list= n*[0]
        for i in range(n):
            if i ==0:
                non_p_list[i]=0
            else:
                non_p_list[i]= solution_instance.listp[i-1]*n-solution_instance.listp[i]
        print('The number of nodes at level 0: 1 promising node(s);0 nonpromising node(s).')
        for i in range(n):
            print('The number of nodes at level '+str(i+1)+': '+str(solution_instance.listp[i])+' promising node(s);'+
                str(non_p_list[i])+' nonpromising node(s). ')
            
        print ('The number of solutions is '+str(len(solutions))+'.')
        for solution in solutions:
            print(solution)
