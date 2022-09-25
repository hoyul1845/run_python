# 함수:특정 작업을 한 뒤 결과값을 돌려주는 것
# 사용법:리턴값 = 함수이름(전달값)

# remove:전달값 삭제
# pop:맨뒤에서 값 꺼내오기
# clear:모두삭제

# 과일리스트
fruits = ["오렌지","사과","배","바나나","키위","사과","바나나"]
print(fruits)

# 리스트에서 값 삭제
#fruits.remove("배")
#print(fruits)

# 맨 뒤에서 값 꺼내오기
#my_frits = fruits.pop()
#print(my_frits)
#print(fruits)

# 리스트의 모든 값 삭제
#fruits.clear()
#print(fruits)

# index:전달값의 인덱스 가져오기
# count:전달값의 개수 가져오기

# 바나나 개수 가져오기
#count = fruits.count("바나나")
#print(count)

# 인덱스 가져오기
#idx = fruits.index("바나나")
#print(idx)

# sort:오름차순으로 정렬
# reverse:리스트 요소를 제자리에서 뒤집기

# 오름차순으로 정렬
fruits.sort()
print(fruits)

# 거꾸로 뒤집어서 졍렬하기
fruits.reverse()
print(fruits)