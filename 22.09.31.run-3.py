# 지역변수:함수 안에서 선언
# 전역변수:함수 밖에서 선언

number = 10
print(1,number)

'''
분을 초로 바꾸는 함수
함수이름:min_to_sec
파라미터:minutes
        분,int
리턴값:초,int
'''
def min_to_sec(minutes):
    number = 20
    print(2,number)
    second = minutes * 60
    return second

sec = min_to_sec(30)
print(3,number)
