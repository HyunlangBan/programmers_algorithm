## ✅
# 맨 처음에 문자열 길이가 1개일때를 고려 안해서 테스트 케이스 하나가 통과가 안되었었다. 놓치기 쉬우니 주의하자.

def compress(s, n):
    prev = s[0:n]
    cnt = 1
    res = ''
    for i in range(n, len(s), n):
        word = s[i:i+n]
        # print(word)
        if word == prev:
            cnt += 1
        else:
            if cnt > 1:
                res = res + f'{cnt}{prev}'
                cnt = 1
            else:
                res += prev
            prev = word
    if cnt > 1:
        res += f'{cnt}{prev}'
    else:
        res += prev
    # print(res)
    return len(res)
            


def solution(s):
    answer = 1001
    if len(s)==1:
        return 1
    for i in range(1, len(s)):
        res = compress(s, i)
        answer = min(res, answer)
    return answer
  
 
## 다른 사람 풀이 
# - , TACKHYUN JUNG , Youngwook-Jeon , - , ㅂ신유환

def solution(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1):
        d = 0
        comp = ''
        c = 1
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            if comp == temp:
                c += 1
            elif comp != temp:
                d += len(temp)
                if c > 1:
                    d += len("{}".format(c))
                c = 1
                comp = temp
        if c > 1:
            d += len("{}".format(c))
        answer = min(answer, d)
    return answer
  
## solution 첫번째 loop에서 나는 s의 길이만큼 돌았는데 조각의 갯수를 세는 것이므로 조각이 n//2일때까지만 압축의 의미가 있다. 따라서 길이의 절반만큼만 돌면 된다.
## 나는 전체 압축된 문자를 만들고 거기서 길이를 알아냈는데, 위 답안에선 갯수 자체에만 포커스를 맞춰서 풀이하고 있어서 더 간단하다.
## 또한 answer의 초기값을 s의 길이로 먼저 설정해주면 문자 1개인 경우를 따로 확인할 필요가 없다.
