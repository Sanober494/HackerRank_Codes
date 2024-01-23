#Solution for "Picking Numbers"
#Link: https://www.hackerrank.com/challenges/picking-numbers/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def pickingNumbers(a):
    numCount = {}    
    for num in a:
        numCount[num] = numCount.get(num, 0) + 1
        numCount[num + 1] = numCount.get(num + 1, 0) + 1    
    maxlen = max(numCount.values())    
    return maxlen


n = int(input())
arr = list(map(int, input().split()))

result = pickingNumbers(arr)
print(result)
