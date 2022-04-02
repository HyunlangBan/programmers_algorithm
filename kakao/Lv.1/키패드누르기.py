## My Solution - ❌
## *, #에서 시작하는걸 간과했다.. 배열로 풀었어야 했는데.. 뭐 그외에도 코드도 복잡스럽고...별로다..😢
def move(p, e):
    cnt = [0]*10
    q = [p]
    while q:
        s = q.pop(0)
        if s == e:
            return cnt[e]
        for m in [1, -1, 3, -3]:
            if 0<=s+m<10 and cnt[s+m]==0:
                cnt[s+m]=cnt[s]+1
                q.append(s+m)

def solution(numbers, hand):
    # numbers = list(map(int, numbers))
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    last_right = -1
    left_right = -1
    for n in numbers:
        if n in left:
            answer += 'L'
            last_left = n
        elif n in right:
            answer += 'R'
            last_right = n
        else:
            # last_left와 last_right 거리 비교
            l_s = move(last_left, n)
            r_s = move(last_right, n)
            if l_s == r_s:
                if hand == 'right':
                    last_right = n
                    answer += 'R'
                else:
                    last_left = n
                    answer += 'L'
            else:
                if l_s > r_s:
                    last_right = n
                    answer += 'R'
                elif l_s < r_s:
                    last_left = n
                    answer += 'L'
    return answer
  
## Best Solution
# 백서인 , 양정민 , 박건진 , 이윤선 , YUN-YUNHO 외 35 명
def solution(numbers, hand):
    answer = ''
    key_dict = {1:(0,0),2:(0,1),3:(0,2),
                4:(1,0),5:(1,1),6:(1,2),
                7:(2,0),8:(2,1),9:(2,2),
                '*':(3,0),0:(3,1),'#':(3,2)}

    left = [1,4,7]
    right = [3,6,9]
    lhand = '*'
    rhand = '#'
    for i in numbers:
        if i in left:
            answer += 'L'
            lhand = i
        elif i in right:
            answer += 'R'
            rhand = i
        else:
            curPos = key_dict[i]
            lPos = key_dict[lhand]
            rPos = key_dict[rhand]
            ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
            rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])

            if ldist < rdist:
                answer += 'L'
                lhand = i
            elif ldist > rdist:
                answer += 'R'
                rhand = i
            else:
                if hand == 'left':
                    answer += 'L'
                    lhand = i
                else:
                    answer += 'R'
                    rhand = i

    return answer
## 나처럼 비효율적으로 거리를 모두 구하는게 아니라, 좌표로 간단히 해결 :) ... 
