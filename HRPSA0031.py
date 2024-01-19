#Solution for "Morgan and String" 
#Link: https://www.hackerrank.com/challenges/morgan-and-a-string/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structure


from collections import deque

for i in range(int(input())):
    a = input() + ']'
    b = input() + ']'
    string = deque()
    while len(a) > 1 and len(b) > 1:
        if a < b:
            string.append(a[0])
            a = a[1:]
        else:
            string.append(b[0])
            b = b[1:]
    print(''.join(string) + a[:-1] + b[:-1])
