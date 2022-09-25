# 회원의 로그인 정보를 dict변수에 저장하기
loginn = {"lion":"lionok!","apeach":"apeachok!","muzi":"muziok!"}
print(loginn)

# 2. 아이디와 비밀번호 입력받아 확인하기
my_id = ""
my_pwd = ""
while True:
    my_id = input("아이디를 입력하세요: ")
    my_pwd = input("비밀번호를 입력하세요: ")
    
    # 아이디와 비밀번호 맞는지 확인하기
    if my_pwd == loginn.get(my_id):
        print("로그인 되었습니다.")
        break
    else:
        print("잘못된 정보입니다.다시 입력하세요.")
