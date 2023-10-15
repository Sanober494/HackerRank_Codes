#Solution for "Time Conversion" https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures



from datetime import datetime

def timeConversion(s):
    t=datetime.strptime(s,"%I:%M:%S%p")
    return (t.strftime("%H:%M:%S"))

time=input()
print(timeConversion(time))
