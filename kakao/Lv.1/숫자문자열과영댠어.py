## My Solution 

num_string = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
    "nine"
]
def solution(s):
    answer = ""
    idx = 0
    while idx < len(s):
        if s[idx].isdecimal():
            answer += s[idx]
            idx += 1
            continue

        # 단어 길이 범위: 3~5
        for i in range(3, 6):
            if s[idx:idx + i] in num_string:
                word = s[idx:idx + i]
                num = num_string.index(word)
                idx += i
                answer += str(num)
                break

    return int(answer)
  
## 다른 답들을 보니 주로 replace로 썼더라. 그럼 굉장히 간단해진다.
## 단어 길이 범위를 하드코딩 해버렸는데 비슷한 논리로 푼 다른 답안도 참고하자. 반복문도 하나라 시간 복잡도 면에서도 더 좋아보인다.

## SeungJin Lee , sua1223 , temporary_lee , young_b , LHC 외 3 명
def solution(s):

    eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    if s.isdigit():
        return int(s) # 바로리턴 

    # 숫자면 넘어가고 문자열이라면 다음 숫자가 나올때까지 단어를 완성한다. 
    # 문자열이 이어져있을수도 있으므로 한단어씩 문자열에 합칠때마다 eng배열에 존재하는지 확인하고 있으면 temp를 빈문자열로 초기화시킨다.

    answer = ''
    temp = ''
    for i in s:
        if i.isdigit():
            answer+=i
        # 문자열이면 
        else:
            temp += i
            if temp in eng:
                answer += str(eng.index(temp))
                temp = ''
 
    return int(answer)
