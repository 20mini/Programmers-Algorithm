#https://school.programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    answer = 0
    while(num!=1):
        if num%2==0:
            num/=2
        else:
            num=num*3+1
        answer+=1
        if answer==501:
            answer=-1
            break
    return answer