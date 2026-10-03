# Formal Languages - Assignment 2: Subset Construction

- **Full name:** Isabela Valencia Pino
- **Class:** SI2002

## Description

This project implements the **Subset Construction** algorithm presented in Kozen 1997, Lecture 6. It converts a Non-Deterministic Finite Automaton (NFA) into an equivalent Deterministic Finite Automaton (DFA).

The program reads one or more NFAs from standard input, builds the DFA by generating only the reachable subsets of NFA states, and prints for each case the initial state, the final states, and the transition table of the DFA.

## Technologies

- **Programming language:** Python
- **Python version:** 3.14.2

## How to Run

From the project directory:

```bash
python main.py
```

Then type (or paste) the input described below. You can also read the input from a file:

```bash
python main.py < input.txt
```

## Input Format

```text
c                      number of cases (c > 0)
n                      number of NFA states (states are 1..n)
S                      initial states, separated by spaces
alphabet               lowercase letters, separated by spaces
F                      final states, separated by spaces
n lines                one row of the transition table per state, in order
```

Each table row starts with the state number, followed by one entry per alphabet symbol, in the same order as the alphabet line. Sets are written with `{` and `}` and elements separated by spaces. The empty set is `0`.

### Example input

```text
1
5
3 5
a b
1 4
1 {1 5} 0
2 {1} 0
3 {2 4} 0
4 0 {5}
5 {1 5} {4}
```

## Output Format

For each case the program prints:

1. `Initial state:` the initial state of the DFA.
2. `Final states:` the final states of the DFA.
3. The transition table, one row per DFA state, with one column per alphabet symbol.

DFA states are named by the subset of NFA states they represent, e.g. `{1 2 4 5}`. The empty subset is written `0` (the dead state; all its transitions go to itself).

### Example output (for the input above)

```text
Initial state: {3 5}
Final states: {1 2 4 5} {4} {1 5} {4 5}
State      a          b
{3 5}      {1 2 4 5}  {4}
{1 2 4 5}  {1 5}      {4 5}
{4}        0          {5}
{1 5}      {1 5}      {4}
{4 5}      {1 5}      {4 5}
0          0          0
{5}        {1 5}      {4}
```

## Algorithm

1. The set of initial states `S` of the NFA is the initial state of the DFA.
2. For each DFA state `T` (a subset of NFA states) and each symbol `a`, compute the union of the NFA transitions on `a` of every state in `T`.
3. If the resulting subset has not been seen before, add it as a new DFA state to a work queue.
4. Repeat until the queue is empty, so only reachable subsets are generated.
5. A DFA state is final if its subset contains at least one final state of the NFA.

### Worked example

Starting from `{3 5}` with the example NFA:

- On `a`: `δ(3,a) ∪ δ(5,a) = {2 4} ∪ {1 5} = {1 2 4 5}`
- On `b`: `δ(3,b) ∪ δ(5,b) = ∅ ∪ {4} = {4}`

New states `{1 2 4 5}` and `{4}` are queued and processed the same way until no new subsets appear. Final states are those containing 1 or 4.

### Complexity

In the worst case the DFA has up to 2^n states, but generating only the reachable subsets usually produces far fewer (7 in the example, out of 32 possible).

## Reference

Kozen, Dexter C. (1997). *Automata and Computability*. 1st ed. Berlin, Heidelberg: Springer-Verlag.