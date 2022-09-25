# break는 반복문에서 벗어난다.
# countinue는 다음코드로 건너뛰고 반복으로 돌아간다.

# 1부터 시작해서 1씩 증가하는 반복문
i = 0
while True:
    i += 1
    # 20보다 크면 반복문 벗어나기
    if i > 20:
        break
    # 짝수인 경우 건너뛰기
    if i % 2 == 0:
        continue
    
    # 홀수인 경우만 출력하기
    print(i)
