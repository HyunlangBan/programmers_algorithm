## ✅
from collections import defaultdict
def solution(record):
    # record에서 변하지 않는 것은 uid임
    # uid에 해당하는 최종 닉네임만 찾아내면 된다.
    answer = []
    
    users = defaultdict()
    actions = {"Enter": "들어왔습니다", "Leave": "나갔습니다"}
    
    for rec in record:
        if "Leave" not in rec:
            action, uid, nickname = rec.split()
        users[uid] = nickname
    
    for rec in record:
        action, uid = rec.split()[:2]
        if action in actions:
            answer.append(f"{users[uid]}님이 {actions[action]}.")
    
    return answer
