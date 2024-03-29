
####### Problem 3 #######

import math

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    if (S == ""):
        return len(T)
    elif (T == ""):
        return len(S)
    else:
        if (S[0] == T[0]):
            return MED(S[1:], T[1:])
        else:
            return 1 + min(MED(S, T[1:]),     # insertion 
                           MED(S[1:], T[1:]), # subsituution 
                           MED(S[1:], T))     # deletion 

def print2dlist(list_): 
  for i in list_:
    for j in list(reversed(i)):
        print(f" {j} ", end="")
    print("")

def fast_MED(S, T, mem={}):
    mem = [[0 for x in range(len(S))] for x in range(len(T))]

    for i in range(len(T)):
        for j in range(len(S)):
          
            if i == 0: mem[i][j] = j
            elif j == 0: mem[i][j] = i
            elif T[i-1] == S[j-1]: mem[i][j] = mem[i-1][j-1]
            else: mem[i][j] = 1 + min(mem[i][j-1], 
                                      mem[i-1][j-1],
                                      mem[i-1][j])
  
    return mem[-1][-1]

def fast_align_MED(S, T, MED={}):
    mem = [[0 for x in range(len(S))] for x in range(len(T))]
    align_path = list()
  
    for i in range(len(T)):
        for j in range(len(S)):
          
            if i == 0: mem[i][j] = j
            elif j == 0: mem[i][j] = i
            elif T[i-1] == S[j-1]: mem[i][j] = mem[i-1][j-1]
            else: mem[i][j] = 1 + min(mem[i][j-1], 
                                      mem[i-1][j-1],
                                      mem[i-1][j])

    # find alignment path 
    i, j = len(T) - 1, len(S) - 1
    align_path.append((i, j))
    while i != 0 and j != 0:
      min_ = min(mem[i-1][j-1], mem[i][j-1], mem[i-1][j])

      # diagonal decreasing case
      if mem[i-1][j-1] == min_:
        i -= 1
        j -= 1
        align_path.append((i, j))

      # horizontal non-decreasing
      elif mem[i][j-1] == min_:
        j -= 1
        align_path.append((i, j))

      # vetical decreasing
      elif mem[i-1][j] == min_:
        i -= 1
        align_path.append((i, j))

    # finding traceback for string edits
    # note : t char index = i , then s char index = j 
    align_S, align_T = str(), str()  
    i, j = len(T) - 1, len(S) - 1
    for t, s in align_path:
      
      # diagonal increase case
      if t == i and s == j:
        align_T += T[t]
        align_S += S[s]
        i -= 1
        j -= 1

      # horizontal non-increase
      if t == i and s > j:
        align_T += T[t]
        align_S += '-'
        i -= 1
        j = s - 1
        
      # vetical increasing
      if t > i and s == j:
        align_T += '-'
        align_S += S[s]
        i = t - 1
        j -= 1

    return align_S[::-1], align_T[::-1]

def test_MED():
    for S, T in test_cases:
      assert fast_MED(S, T) == MED(S, T)
                       
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
  