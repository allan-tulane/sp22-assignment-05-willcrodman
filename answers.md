# CMPS 2200 Assignment 5
## Answers

**Name:**____Will Rodman_________


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**


Greedy algo sudo code:
```
function(N, coin_count = 0):
  if 0 == N:
    return coin_count
  
  largest_coin = floor(log2(N))
  remaining_dollars = N - largest_coin
  
  return function(remaining_dollars, coin_count++)
```
This algo produced the optimal number of coins needed for N dollars. 


- **1b.**

W(n) = W(n - floor(log2(n))) + 1

S(n) = S(n - floor(log2(n))) + 1


- **2a.**


- **2b.**



