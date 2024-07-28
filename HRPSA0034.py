
def getMoneySpent(keyboards, drives, b):
    Tsum=0
    Fsum=0
    for i in range (0,len(keyboards)):
        for j in range(0,len(drives)):
            Tsum=keyboards[i]+drives[j]
            if Fsum<Tsum and Tsum<=b:
                Fsum=Tsum
    if Fsum!=0 and Fsum<=b:
        print(Fsum)
    else:
        print(-1)
        
arr=input()
Arr=list(map(int,arr.split()))
b=Arr[0]
arr1=input()
Arr1=list(map(int,arr1.split()))
arr2=input()
Arr2=list(map(int,arr2.split()))
getMoneySpent(Arr1, Arr2, b)
