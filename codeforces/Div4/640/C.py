import math
import sys


def kthNonDivisible(N, K):
     
    # Lowest possible value
    L = 1
   
    # Highest possible value
    H = sys.maxsize
   
    # To store the Kth non
    # divisible number of N
    ans = 0
 
    # Using binary search
    while (L <= H):
         
        # Calculating mid value
        mid = (L + H) // 2
 
        # Sol would have the value
        # by subtracting all
        # multiples of n till mid
        sol = mid - mid // N
 
        # Check if sol is greater than k
        if (sol > K):
           
            # H should be reduced to find
            # minimum possible value
            H = mid - 1
       
        # Check if sol is less than k
        # then L will be mid+1
        elif (sol < K):
          L = mid + 1
       
        # Check if sol is equal to k
        else:
             
            # ans will be mid
            ans = mid
           
            # H would be reduced to find any
            # more possible value
            H = mid - 1
   
    # Print the answer
    print(ans)

n = int(input())
for _ in range(n):
    a,b = list(map(int, input().split()))
    # if a == b:
    #     print(1)
    #     continue

        # listy = [i for i in range(1_000_000) if i%a != 0]
    kthNonDivisible(a,b)