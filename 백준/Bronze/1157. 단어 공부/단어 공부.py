word = list(input().upper())
arr = [0]*30
for w in word:
  arr[ord(w)-ord('A')]+=1
mx = max(arr)
if arr.count(mx)==1:
  print(chr(arr.index(mx)+ord('A')))
else:
  print("?")