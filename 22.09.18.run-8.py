# 논리 연산자:and,or,not
# a and b 뜻:두 값 모두 참인 경우만 True
# a or b 뜻:두 값 중 하나라도 참인 경우 True
# not a 뜻:반대값 반환
# 논리연산자 테스트
# 수 입력받기
#x = int(input("수를 입력하세요. :"))

# and
# 입력 값이 100보다 크거나 같고, 200보다 작은지 확인하기
#bVal = (x >= 100) and (x < 200)
#print(bVal)

# or
# 입력 값이 100보다 작은지 또는 200보다 크거나 같은지 확인하기
#bVal = x < 100 or x >= 200
#print(bVal)

# not
#light_on = False
#print(light_on, not light_on)

# 논리연산자 연습문제
height = int(input("키를 입력하세요. :"))
weight = int(input("몸무게를 입력하세요."))

# A 놀이기구 탑승여부
bVal = height >= 150
print("A 놀이기구 탑승 가능:",bVal)

# B 놀이기구 탑승여부
bVal = height >= 150  and weight >= 45
print("B 놀이기구 탑승 가능:",bVal)

# C 놀이기구 탑승여부
bVal = height >= 150 or weight >= 45
print("C 놀이기구 탑승가능:",bVal)