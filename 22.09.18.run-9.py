# 리스트:여러데이타를 저장 할 수 있음(예:number = [1,2,3,4,5])
# list는 다양한 자료형을 가진다.

# 나의 운동 점수 리스트에 저장
score = [500, 470, 420, 330, 250, 180, 100]
print(score)

# 인덱싱 하기
#print(score [2])

# 슬라이싱 하기
# 앞에서부터 높은 점수 3개 가져오기
#print(score[:3])

# 뒤에서 낮은점수 3개 가져오기
#print(score[-3:])

# list 인덱스로 값 변경 삭제를 할 수 있다.

# 리스트 값 변경
score[1] = 450
print(score)

# 리스트의 값 삭제
del score[3]
print(score)