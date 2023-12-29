#Solution for "Sales by Match" 
#Link: https://www.hackerrank.com/challenges/sock-merchant/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def sockMerchant(n, ar):
    pairs=0
    newList=[]
    for i in range(0,len(ar)):
        count=0
        if ar[i] in newList:
            continue
        else:
            for j in range(i+1,len(ar)):
                if (ar[i]==ar[j]):
                    count+=1
            newList.append(ar[i])
            if (int(count%2)==0):
                pairs+=int(count/2)
            else:
                count+=1
                pairs+=int(count/2)
    print(pairs)           


n1=int(input())
num=input()
Num=list(map(int,num.split()))
sockMerchant(n1,Num)
