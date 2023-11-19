#Solution for "Counting Valleys" 
#Link: https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures


def countingValleys(steps, path):
    level = 0 
    valley_count = 0  
    for step in path:
        if step == "U":
            level += 1
        else:
            level -= 1
        if step == "U" and level == 0:
            valley_count += 1
    return valley_count
    
n1 = int(input())
stInput = input()
st = list(stInput)
result = countingValleys(n1, st)
print(result)
