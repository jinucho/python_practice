import numpy as np

def solution(arr1, arr2):
    answer = [[int(j) for j in list(i)] for i in np.array(arr1)+np.array(arr2)]
    return answer