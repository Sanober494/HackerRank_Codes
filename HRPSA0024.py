#Solution for "Subarray Division" 
#Link: https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structure

def birthday(s, d, m):
    
    ways = 0
 
    for i in range(len(s) - m + 1):
       
        if sum(s[i:i+m]) == d:
            ways += 1

    return ways



s1=int(input())
S =input()
S_new=list(map(int,S.split()))
D=input()
New=list(map(int,D.split()))
D1=New[0]
M1=New[1]
print(birthday(S_new, D1, M1))
