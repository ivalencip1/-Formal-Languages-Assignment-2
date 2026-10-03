# Step 1: Read one transition row
def read_transition_row(row):
    state = int(row[0])
    transitions = []

    current_transition = ""
    inside_set = False

    for value in row[1:]:
        if value.startswith("{"):
            inside_set = True
            current_transition = value

            if value.endswith("}"):
                inside_set = False
                transitions.append(current_transition)

        elif inside_set:
            current_transition += " " + value

            if value.endswith("}"):
                inside_set = False
                transitions.append(current_transition)

        else:
            transitions.append(value)

    parsed_transitions = []

    for transition in transitions:
        if transition == "0":
            parsed_transitions.append(set())
        else:
            transition = transition.replace("{", "").replace("}", "")
            parsed_transitions.append(set(map(int, transition.split())))

    return state, parsed_transitions


# Step 2: Read the NFA transition table
def read_transition_table(states):
    transition_table = {}

    for _ in range(states):
        row = input().split()

        state, transitions = read_transition_row(row)

        transition_table[state] = transitions

    return transition_table


# Step 3: Calculate the transition of a set of states
def calculate_transition(state_set, symbol_index, transition_table):
    result = set()

    for state in state_set:
        result.update(transition_table[state][symbol_index])

    return result


# Step 4: Build the DFA using Subset Construction
def subset_construction(initial_states, alphabet, transition_table):
    dfa_states = []
    dfa_transitions = {}

    initial_state = frozenset(initial_states)

    dfa_states.append(initial_state)

    index = 0

    while index < len(dfa_states):
        current_state = dfa_states[index]
        dfa_transitions[current_state] = []

        for symbol_index in range(len(alphabet)):
            next_state = calculate_transition(
                current_state,
                symbol_index,
                transition_table
            )

            next_state = frozenset(next_state)

            dfa_transitions[current_state].append(next_state)

            if next_state not in dfa_states:
                dfa_states.append(next_state)

        index += 1

    return dfa_states, dfa_transitions


# Step 5: Identify the final states
def identify_final_states(dfa_states, final_states):
    dfa_final_states = []

    for state in dfa_states:
        if any(element in final_states for element in state):
            dfa_final_states.append(state)

    return dfa_final_states


# Step 6: Format a DFA state
def format_state(state):
    if not state:
        return "0"

    return "{" + " ".join(map(str, sorted(state))) + "}"


# Step 7: Print the DFA
def print_dfa(dfa_states, dfa_transitions, alphabet, initial_state, final_states):
    print("Initial state:", format_state(initial_state))

    print("Final states:", end=" ")

    for state in final_states:
        print(format_state(state), end=" ")

    print()

    headers = ["State"] + alphabet

    rows = []

    for state in dfa_states:
        row = [format_state(state)]

        for transition in dfa_transitions[state]:
            row.append(format_state(transition))

        rows.append(row)

    column_widths = []

    for column in range(len(headers)):
        width = len(headers[column])

        for row in rows:
            width = max(width, len(row[column]))

        column_widths.append(width)

    for column in range(len(headers)):
        print(headers[column].ljust(column_widths[column] + 2), end="")

    print()

    for row in rows:
        for column in range(len(row)):
            print(row[column].ljust(column_widths[column] + 2), end="")

        print()


# Main algorithm
def subset_construction_algorithm(cases):
    for _ in range(cases):
        states = int(input())

        initial_states = set(map(int, input().split()))

        alphabet = input().split()

        final_states = set(map(int, input().split()))

        transition_table = read_transition_table(states)

        dfa_states, dfa_transitions = subset_construction(
            initial_states,
            alphabet,
            transition_table
        )

        dfa_final_states = identify_final_states(
            dfa_states,
            final_states
        )

        initial_state = frozenset(initial_states)

        print_dfa(
            dfa_states,
            dfa_transitions,
            alphabet,
            initial_state,
            dfa_final_states
        )


def main():
    cases = int(input())

    subset_construction_algorithm(cases)


if __name__ == "__main__":
    main()