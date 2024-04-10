def solution(babbling):
    answer = 0
    pronounceables = ["aya", "ye", "woo", "ma"]
    for word in babbling:
        for pronounceable in pronounceables:
            while pronounceable in word:
                word = word.replace(pronounceable,",")
                if not any(c.isalpha() for c in word) :
                    answer += 1
    return answer

'''
aya / ye / woo / ma 를 조합한 단어만 발음 가능
'''