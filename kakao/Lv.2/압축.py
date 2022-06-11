✅
## My Solution
from collections import defaultdict
def solution(msg):
    answer = []
    words = defaultdict()
    for k in range(1, 27):
        words[chr(64+k)] = k   ## words = {chr(e + 64): e for e in range(1, 27)} 로 쓰자

    while msg:
        e = -1
        if msg in words:
            e = -1
            w = msg
            msg = ''
        else:
            for i in range(1, len(msg)):   ### for문으로 돌리니 slice시, 맨 마지막 문자는 포함이 안되는 문제가 발생해서 위의 조건을 추가했다. while을 쓰는것이 더 좋았을듯
                if msg[:i] in words:
                    e = i
                    w = msg[:i]
                else:
                    break

        answer.append(words[w])
        if e > 0:
            new_word = w+msg[e] ## msg[:e+1]이 더 좋은 답이다. 만약 맨 끝자리까지 포함이라면 e==len(msg)이므로 index 에러가 발생한다.
            words[new_word] = len(words)+1
            msg = msg[e:]

    return answer
  

## Best Solution: - , 염기웅 , - , JiSun Lim , Lim_heejin 외 2 명
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
