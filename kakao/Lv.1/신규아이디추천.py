## My Solution
def solution(new_id):
    new_id_1 = new_id.lower()
    
    new_id_2 = []
    new_id_1 = list(new_id_1)
    while new_id_1:
        c = new_id_1.pop(0)
        if c.islower():
            new_id_2.append(c)
        elif c.isdigit():
            new_id_2.append(c)
        elif c in ['-', '_', '.']:
            if len(new_id_2) and new_id_2[-1]=='.' and c=='.':
                continue
            new_id_2.append(c)

    if len(new_id_2)>0 and new_id_2[0] == '.':
        new_id_2 = new_id_2[1:]
    if len(new_id_2)>0 and new_id_2[-1] == '.':
        new_id_2 = new_id_2[:-1]
    
    if new_id_2==[]:
        new_id_2.append('a')
        
    if len(new_id_2)>=16:
        new_id_2 = new_id_2[:15]
        if new_id_2[-1] == '.':
            new_id_2.pop()
    
    if len(new_id_2)<=2:
        last_char = new_id_2[-1]
        while len(new_id_2)<3:
            new_id_2.append(last_char)
            
    answer = ''.join(new_id_2)
    return answer
  
## 맞았닫는 기쁨도 잠시 우아한 답안들에 기가 죽었다.
## 우아한 답안들 ✨

## Sol1
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)
    st = re.sub('\.+', '.', st)
    st = re.sub('^[.]|[.]$', '', st)
    st = 'a' if len(st) == 0 else st[:15]
    st = re.sub('^[.]|[.]$', '', st)
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st
## 그동안 정규식을 등한시(?) 했었는데... 이래서 정규식을 쓰는거구나....

## Sol2
def solution(new_id):
    answer = ''
    # 1
    new_id = new_id.lower()
    # 2
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c
    # 3
    while '..' in answer:
        answer = answer.replace('..', '.')
    # 4
    if answer[0] == '.':
        answer = answer[1:] if len(answer) > 1 else '.'
    if answer[-1] == '.':
        answer = answer[:-1]
    # 5
    if answer == '':
        answer = 'a'
    # 6
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer
## 풀이가 너무 깔끔함! 특히 나는 겁나게 늘어쓴 2번 3번 과정이 쏘 씸플..
