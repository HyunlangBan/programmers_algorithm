def solution(id_list, report, k):
    dict = {}
    res = {}
    for id in id_list:
        dict[id] = set()
        res[id] = 0
    for rep in report:
        x, y = rep.split()
        dict[y].add(x)
    for key, val in dict.items():
        if len(val) >= int(k):
            reporter = tuple(val)
            for name in reporter:
                res[name] += 1
    answer = list(res.values())
    return answer
  
## 문제 풀기 바로 전에 tuple은 immutable해서 dict의 key로 쓸 수 있다 보고 왔는데 문제에서 의도치않게(?) 써먹음
## list.index()가 기억이 안나서 결국 dict를 두개 만들어버림
