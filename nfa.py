class NFAState:
  label, transition1, transition2 = None, None, None
class NFA:
  start_state, accept_state = None, None
  def __init__(self, start: NFAState, accept: NFAState) -> None:
    self.start_state = start
    self.accept_state = accept
def unit_nfa(inp: str) -> NFA:
  q = NFAState()
  f = NFAState()
  q.label = inp
  q.transition1 = f
  res_nfa = NFA(q, f)
  return res_nfa
def nfa_union(nfa1: NFA, nfa2: NFA) -> NFA:
  q = NFAState()
  f = NFAState()
  q.transition1 = nfa1.start_state
  q.transition2 = nfa2.start_state
  nfa1.accept_state.transition1 = f
  nfa2.accept_state.transition1 = f
  res_nfa = NFA(q, f)
  return res_nfa
def nfa_concat(nfa1: NFA, nfa2: NFA) -> NFA:
  nfa1.accept_state.transition1 = nfa2.start_state
  res_nfa = NFA(nfa1.start_state, nfa2.accept_state)
  return res_nfa
def nfa_kleene(nfa1: NFA) -> NFA:
  q = NFAState()
  f = NFAState()
  q.transition1 = nfa1.start_state
  q.transition2 = f
  nfa1.accept_state.transition1 = nfa1.start_state
  nfa1.accept_state.transition2 = f
  res_nfa = NFA(q, f)
  return res_nfa
def epsilon_closure(state: NFAState) -> set[NFAState]:
  states = set()
  states.add(state)
  if state.label is None:
  if state.transition1 is not None:
    states |= epsilon_closure(state.transition1)
  if state.transition2 is not None:
    states |= epsilon_closure(state.transition2)
  return states
