#Solution for "Flipping Bits" 
#Link: https://www.hackerrank.com/challenges/flipping-bits/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def flippingBits(n):
    binaryRep = bin(n)[2:].zfill(32)  
    flippedString = ''.join('1' if bit == '0' else '0' for bit in binaryRep)
    decimalNum = int(flippedString, 2)  
    return decimalNum

n1 = int(input())

for i in range(n1):
    num = int(input())
    print(flippingBits(num))
