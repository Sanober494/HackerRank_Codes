#Solution for "Sherlock and Array" 
#Link: https://www.hackerrank.com/challenges/sherlock-and-array/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def balancedSums(arr):
    total_sum = sum(arr)
    left_sum = 0    
    for num in arr:
        total_sum -= num
        if left_sum == total_sum:
            return "YES"
        left_sum += num        
    return "NO"

t = int(input())

for _ in range(t):
    num_elements = int(input())
    num_list = list(map(int, input().split()))
    result = balancedSums(num_list)
    print(result)
