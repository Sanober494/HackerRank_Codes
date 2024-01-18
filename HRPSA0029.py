#Solution for "Missing Numbersr" 
#Link: https://www.hackerrank.com/challenges/missing-numbers/problem?isFullScreen=true
#Problem Solving-> Algorithms-> Data Structures

def missingNumbers(arr, brr):    
    freq_arr = {}
    freq_brr = {}    
    for num in arr:
        freq_arr[num] = freq_arr.get(num, 0) + 1  
    for num in brr:
        freq_brr[num] = freq_brr.get(num, 0) + 1    
    missing_numbers = []
    for num in freq_brr:
        if num not in freq_arr or freq_brr[num] > freq_arr[num]:
            missing_numbers.append(num)  
    missing_numbers.sort()
    print(*missing_numbers)

lenarr = int(input())
arr_input = input()
arr = list(map(int, arr_input.split()))

lenarr1 = int(input())
arr1_input = input()
arr1 = list(map(int, arr1_input.split()))

missingNumbers(arr, arr1)
