# 값:숫자,문자 뿐 아니라 리스트 같은 다양한 데이타 사용 가능

# 과일과 과일개수를 dict에 넣기
# 사과 5개,오렌지 7개
fruits = {"사과":5,"오렌지":7}
print(fruits)

# 키를 이용해서 값 가져오기
#print(fruits["사과"],fruits["오렌지"])

# 데이타 추가
# 딸기 20
fruits["딸기"] = 20
print(fruits)

# 키를 이용해서 값 변경
# 사과 10개로 변경
fruits["사과"] = 10
print(fruits)

# 키를 이용해서 삭제
# 오렌지 삭제
del fruits["오렌지"]
print(fruits)