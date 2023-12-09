#Solution for "Grading Students" 
#Link: https://www.hackerrank.com/challenges/grading/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def gradingStudents(grades):
    c=0
    a2=[]
    for i in range(len(grades)):
        if (((grades[i]%5)==0) and (grades[i]>37)):
            a2.append(grades[i])      
        elif (grades[i]>37):
            c=grades[i]
            while((c%5)!=0):
                c+=1
            if (((c-grades[i])<3)):
                a2.append(c)
            else:
                a2.append(grades[i])
        else:
            a2.append(grades[i])
    for k in range(len(a2)):
        print(a2[k])
            
                


n=int(input())
a1=[]
for i in range(n):
    a=int(input())
    a1.append(a)
gradingStudents(a1)
