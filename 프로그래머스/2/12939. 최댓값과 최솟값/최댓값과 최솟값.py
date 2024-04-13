def solution(s):
    str_nums = s.split(' ')
    nums = [int(n) for n in str_nums]
    max_num = max(nums)
    min_num = min(nums)
    answer = f'{min_num} {max_num}'
    return answer