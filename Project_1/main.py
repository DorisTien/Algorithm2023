
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
    iteration=0
    while not sorted(n,list_S):
        i = randomindex(0,n-1)
        j= randomindex (0,n-1)
        iteration+=1
        #print('i:'+str(i)+'; j:'+str(j))
        if i<j and list_S[i]>list_S[j]:
            list_S[i], list_S[j] = list_S[j], list_S[i]
            iteration+=1
            #print('swap is done')
    return iteration

def randomsort2(n,list_S):
    iteration=0
    while not sorted(n,list_S):
        i = randomindex(0,n-1)
        j= randomindex (i,n-1)
        iteration+=1
        #print('i:'+str(i)+'; j:'+str(j))
        if i<j and list_S[i]>list_S[j]:
            list_S[i], list_S[j] = list_S[j], list_S[i]
            iteration+=1
            #print('swap is done')
    return iteration

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

def experiment2(size,times):
    total_iteration=0
    for time in range(times):
        arr = [random.randint(1, 100) for _ in range(size)]
        #print(' '.join(map(str, arr)))
        while not sorted(size,arr):
            sub_interation =randomsort2(size,arr)
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

    list_results= []
    '''
    for i in sizes:
        result=experiment(i,2)
        list_results.append(result)
    for elem in list_results:
        print(elem)    
    '''
    values = [177.0, 1931.5, 2550.0, 9617.5, 11998.0, 53287.5, 314298.0, 1014111.5, 3951446.0, 15541535.0]
    #plot(sizes,values)
    compare=[]
    for i in sizes:
        result=4*i*i*i*i
        compare.append(result)

    compare2=[]
    for i in sizes:
        result=4*i*i*i
        compare2.append(result)

    list_results2= []
    for i in sizes:
        result=experiment2(i,2)
        list_results2.append(result)
    for elem in list_results2:
        print(elem)

    values2 = [279.0, 1222.5, 3064.5, 4674.0, 6644.5, 41799.5, 181293.0, 800356.5, 2527792.5, 9655031.5]
 

    print(compare2)