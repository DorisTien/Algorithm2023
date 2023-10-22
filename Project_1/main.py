
import matplotlib.pyplot as plt
import random
def sorted(n,list_S):
    for i in range(0,n-1):
        if list_S[i]> list_S[i+1]:
            return False
    return True
def randomindex(a,b):
    if not a<b:
        return a
    result= random.randint(a, b)
    return result

def randomsort(n,list_S):
    excahnge_iteration=0
    while not sorted(n,list_S):
        i = randomindex(0,n-1)
        j= randomindex (0,n-1)
        #print('i:'+str(i)+'; j:'+str(j))
        if i<j and list_S[i]>list_S[j]:
            list_S[i], list_S[j] = list_S[j], list_S[i]
            excahnge_iteration+=1
            #print('swap is done')
    return excahnge_iteration

def experiment(size,times):
    total_iteration=0
    for time in range(times):
        arr = [random.randint(1, 100) for _ in range(size)]
        #print(' '.join(map(str, arr)))
        while not sorted(size,arr):
            sub_interation =randomsort(size,arr)
            total_iteration += sub_interation
    average= total_iteration/times
    return average

def plot(sizes_list,values_list):
    # Plotting
    plt.plot(sizes_list, values_list, marker='o', linestyle='-')

    # Adding title and labels
    plt.title('Plot of average number of iterations against Sizes')
    plt.xlabel('Sizes')
    plt.ylabel('Average number of iterations')

    # Display the plot
    plt.show()

    
   


    

if __name__ == '__main__':

    sizes = [10, 20, 30, 40, 50, 100, 200, 400, 800, 1600]
    '''
    list_results= []
    
    for i in sizes:
        result=experiment(i,1)
        list_results.append(result)
    for elem in list_results:
        print(elem)    
  '''
    values = [11.0, 38.0, 79.0, 124.0, 160.0, 366.0, 871.0, 1976.0, 4211.0, 8784.0]
    plot(sizes,values)