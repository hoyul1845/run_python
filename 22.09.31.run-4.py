'''
함수이름:my_print
기능:문자,가로반복횟수,세로반복횟수 입력받아서 가로,세로 반복하는 문자를 출력한다.
매걔변수 : string(str),width(int),height(int)
리턴값:x
'''
def my_print(string, width, height):
    cnt = 0
    while cnt <= height:
        print(string * width)
        cnt += 1
    
my_print("@",10, 5)