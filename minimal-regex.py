import NFA
def infix_to_postfix(infix_regex: str) -> str:
  postfix_regex = ""
  operands = {"?": 5, "+": 4, "*": 3, ".": 2, "|": 1}
  stack = []
  for char in infix_regex:
    if char.isalnum():
      postfix_regex += char
    elif char == "(":
      stack.append(char)
    elif char == ")":
    while stack and (stack[-1] != "("):
      postfix_regex += stack.pop()
      stack.pop()
    else:
      while (
      stack
      and (stack[-1] in operands)
      and (operands[char] <= operands[stack[-1]])
      ):
        postfix_regex += stack.pop()
        stack.append(char)
  while stack:
    postfix_regex += stack.pop()
  return postfix_regex

def build_NFA_from_regex(postfix_regex: str) -> NFA.NFA:
  stack = []
  for char in postfix_regex:
    if char == "?":
      a = stack.pop()
      stack.append(NFA.nfa_union(a, NFA.unit_nfa(None)))
    elif char == "+":
      a = stack.pop()
      stack.append(NFA.nfa_concat(a, NFA.nfa_kleene(a)))
    elif char == "*":
      a = stack.pop()
      stack.append(NFA.nfa_kleene(a))
    elif char == ".":
      b = stack.pop()
      a = stack.pop()
      stack.append(NFA.nfa_concat(a, b))
    elif char == "|":
      b = stack.pop()
      a = stack.pop()
      stack.append(NFA.nfa_union(a, b))
    else:
      stack.append(NFA.unit_nfa(char))
  return stack.pop()

def match(infix_regex: str, input_string: str) -> bool:
  automaton = build_NFA_from_regex(infix_to_postfix(infix_regex))
  current = set()
  next = set()
  current |= NFA.epsilon_closure(automaton.start_state)
  for char in input_string:
    for s in current:
      if s.label == char:
        next |= NFA.epsilon_closure(s.transition1)
    current = next
    next = set()
  return automaton.accept_state in current
