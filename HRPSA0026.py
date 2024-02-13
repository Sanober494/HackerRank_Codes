#Solution for "Drawing Book" 
#Link: https://www.hackerrank.com/challenges/drawing-book/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def pageCount(n, p):
    
    front = p // 2  
    back = (n // 2) - (p // 2)  
    return min(front, back)
                   
n= int(input())
p=int(input())
print(pageCount(n,p))
