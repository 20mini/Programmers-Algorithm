#https://school.programmers.co.kr/learn/courses/30/lessons/12948?language=python3

def solution(phone_number):
    answer='*' * (len(phone_number)-4)+phone_number[-4:]
    return answer