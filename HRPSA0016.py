#Solution for "Bill Division" 
#Link: https://www.hackerrank.com/challenges/bon-appetit/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def bonAppetit(bill, k, b):
    total = sum(bill)
    anna = (total - bill[k]) // 2
    if b == anna:
        print("Bon Appetit")
    else:
        print(b - anna)

line = input()
arr = list(map(int, line.split()))

line1 = input()
arr1 = list(map(int, line1.split()))

amtCharged = int(input())
bonAppetit(arr1, arr[1], amtCharged)
