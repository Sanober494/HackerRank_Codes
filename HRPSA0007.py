#Solution for "Day of the Programmer" 
#Link: https://www.hackerrank.com/challenges/day-of-the-programmer/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures



def dayOfProgrammer(year):
    Year=1918
    if (year==1918):
        print("26.09.1918")
    elif (year>Year and (((year%4)==0 and ((year%100)!=0))or ((year%400)==0))):
        print("12.09.",end="")
        print(year)
    elif (year<Year and ((year%4)==0)):
        print("12.09.",end="")
        print(year)
    else:
        print("13.09.",end="")
        print(year)

n=int(input())
dayOfProgrammer(n)
        

