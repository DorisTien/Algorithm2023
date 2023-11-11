def is_balanced_parentheses(input_string):
    stack = []
    for char in input_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if  not stack :
                return True
            if stack[-1] != "(":
                return False
            stack.pop()
    return len(stack) == 0



def longest_balanced_subsequence_string(s):
    stack_index=[0]
    mm=0
    count=0
    for i in range(len(s)):
        if s[i]==')':
            #print('where am i'+str(i))
            #print(s[stack_index [-1]:i+1])
            count+=1
            if is_balanced_parentheses(s[stack_index [-1]:i+1]):
                stack_index.append(i+1)
                mm=max(mm,count)
                #print('count:'+str(count))
                count=0
                #print('mm: '+str(mm))
    return mm*2


test_cases = [[('(', '(', ')', ')', '(', ')')], [('(', '(', ')', ')')], [('(', ')', ')')], [('(')], [('(', ')', ')', '(')], []]

for test in test_cases:
    if is_balanced_parentheses(test):
        print(f"The string '{test}' is balanced.")
    else:
        print(f"The string '{test}' is not balanced.")

tests=[('(', '(', ')', '(', ')', '(', ')', ')', '(', ')'), ('(', ')', '(', ')', '(', ')'), ('(', '(', '(', ')', ')', ')'), ('(', ')', '(', ')', '(', ')', ')')]
for test in tests:
    print('longest_balanced_subsequence_string:'+str(longest_balanced_subsequence_string(test)))
