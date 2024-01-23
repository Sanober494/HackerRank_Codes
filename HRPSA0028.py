#Solution for "Angry Professor" 
#Link: https://www.hackerrank.com/challenges/angry-professor/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures


def angryProfessor(k, a):
    arr=input()
    c=0
    ARR=list(map(int,arr.split()))
    for i in range(0,len(ARR)):
        if ARR[i]<=0:
            c+=1
    if c>=a:
        print("NO")
    else:
        print("YES")
    
t=int(input())
for i in range (0,t):
    num=input()
    NUM=list(map(int,num.split()))
    angryProfessor(NUM[0],NUM[1])
    
