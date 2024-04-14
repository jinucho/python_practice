def solution(n, arr1, arr2):
    arr_1 = [("0"*(n-len(bin(number)[2:]))+bin(number)[2:]) for number in arr1]
    arr_2 = [("0"*(n-len(bin(number)[2:]))+bin(number)[2:]) for number in arr2]
    answer = []
    for x,y in zip(arr_1,arr_2):
        result = ""
        for i in range(n):
            if x[i] == "0" and y[i] == "0":
                result += " "
            else:
                result += "#"
        answer.append(result)                
        
    return answer