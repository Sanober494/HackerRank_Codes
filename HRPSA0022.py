#Solution for "Mini-Max Sum" 
#Link: https://www.hackerrank.com/challenges/mini-max-sum/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structure

def miniMaxSum(arr):
    min_val = min(arr)
    max_val = max(arr)
    total_sum = sum(arr)
    min_sum = total_sum - max_val
    max_sum = total_sum - min_val

    print(min_sum, max_sum)

# Input
a1 = input()
n = list(map(int, a1.split()))

# Function call
miniMaxSum(n)
