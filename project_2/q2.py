def print_all_ways_to_add_parentheses(expression):
    n = len(expression)
    if n == 0:
        return []

    dp = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        dp[i][i].append(expression[i])

    for l  in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            dp[i][j] = []
            for k in range(i + 1, j + 1, 2):
                if expression[k] in ['+', '-']:
                    left_expressions = dp[i][k - 1] if k - 1 >= i else ['']
                    right_expressions = dp[k + 1][j] if k + 1 <= j else ['']
                    for left in left_expressions:
                        for right in right_expressions:
                            dp[i][j].append('({}){}({})'.format(left, expression[k], right))
    #print(dp)
    #print(dp[0][n - 1])
    return dp[0][n - 1]
# Example usage
expressions = ["8+2-3"]
for expression in expressions:
    ways = print_all_ways_to_add_parentheses(expression)
    print('The test case is: ' +str(expression))
    list_result= []
    list_expression= []
    for way in ways:
        list_expression.append(way)
        print(way)
        print(eval(way))
        list_result.append(eval(way))
    max_result=max(list_result)
    print('The max result is:'+str(max_result))
    print('The following expressions can get the max result: ')
    for elem in list_expression:
        if eval(elem)==max_result:
            print(elem)
