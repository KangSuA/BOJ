def solution(myString, pat):
    myString = myString.replace('A','C')
    myString = myString.replace('B','A')
    myString = myString.replace('C','B')
    return int(pat in myString)