from heapq import heappush, heappop, heapify
def solution(scoville, K):
    heapify(scoville)
    res = 0
    while scoville:
        a = heappop(scoville)
        if a >= K:
            break
        if not scoville:
            return -1
        b = heappop(scoville)
        heappush(scoville,a+(b*2))
        res += 1
    return res