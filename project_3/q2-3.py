import time
def generate_gray_code(n):
    if n == 1:
        return ['0', '1']
    else:
        l1 = generate_gray_code(n - 1)
        l2 = l1[::-1]
        l1 = ['0' + code for code in l1]
        l2 = ['1' + code for code in l2]
        return l1 + l2

import timeit

ns = [2, 3, 4, 8]
processing_times = []

for n in ns:
    print('****************** Gray code of ' + str(n) + ' ******************')
    stmt = "generate_gray_code(n)"
    setup = "from __main__ import generate_gray_code, n"
    # Measure the execution time
    execution_time = timeit.timeit(stmt, setup=setup, number=1)
    processing_times.append(execution_time)
    print(f"Processing time: {execution_time} seconds")

print("List of processing times:", processing_times)