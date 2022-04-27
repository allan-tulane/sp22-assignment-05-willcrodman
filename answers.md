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
  
  largest_coin = 2 ^ floor(log2(N))
  remaining_dollars = N - largest_coin
  
  return function(remaining_dollars, coin_count++)
```
This algo produced the optimal number of coins needed for N dollars. 


- **1b.**

W(n) = W(n - n^lg(n)) + 1

S(n) = S(n - n^lg(n)) + 1

- **2a.**

Given the set of denominations: {{1, 2, 4, 8}, {1, 10, 100}}

If N = 118, the greedy algorithum will scan denominations from largest to smallest:

0 + 100 = 100 -> 100 + 10 -> = 110 -> 110 + 1 = 110 -> 111 + 4 = 115 
-> 115 + 2 = 117 -> 117 + 1 = 118 

100 + 10 + 1 + 4 + 2 + 1 = 118

This prodcued a coin count of 6, however the optimal coin count is 3. 

100 + 10 + 8 = 118

Greedy algorithum does not produce the optimal number of coins because the 
set of denominations is not constant across banks. Therefore multiple 
sub problems must be solved for each bank inorder to prodcue the optimal number
of coins. 

- **2b.**

Let k = the number of denominations, n = the dollar ammount

W(n) = O(n * k)

S(n) = O(n)

