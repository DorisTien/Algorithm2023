class NFA:
    def __init__(self):
        self.states = {0, 1}
        self.alphabet = {'(', ')'}
        self.transitions = {
            0: {'(': {0, 1}},
            1: {')': {0}}
        }
        self.initial_state = 0
        self.accepting_states = {0}

    def is_accepted(self, input_string):
        current_states = {self.initial_state}

        for char in input_string:
            next_states = set()
            for state in current_states:
                if char in self.transitions[state]:
                    next_states.update(self.transitions[state][char])
            current_states = next_states

        return bool(current_states & self.accepting_states)


# Example usage:
nfa = NFA()
input_string = "(())"
print(nfa.is_accepted(input_string))  # True

input_string = "(()(())))"
print(nfa.is_accepted(input_string))  # False

input_string = "(((()))"
print(nfa.is_accepted(input_string))  # False