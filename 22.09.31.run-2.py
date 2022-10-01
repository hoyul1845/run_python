'''
분을 초로 바꾸는 함수
함수이름:min_to_sec
파라미터:minutes
        분,int
리턴값:초,int
'''
def min_to_sec(minutes):
    second = minutes * 60
    return second

sec = min_to_sec(30)
print(sec)