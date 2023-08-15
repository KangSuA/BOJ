def solution(arr, k):
    return [a*k for a in arr] if k%2 else [a+k for a in arr]