def solution(myStr):
    myStr = myStr.replace('a','-').replace('b','-').replace('c','-')
    myStr = myStr.split('-')
    myStr = [s for s in myStr if s!=""]
    if myStr:
        return myStr
    else:
        return["EMPTY"]