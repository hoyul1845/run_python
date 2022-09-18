# list함수는 리스트변수를 쓰고 뒤에.을 꼭 쓰고한다.
# 메소드:특정객체에 종속된 함수
# append:리스트 맨 뒤에 추가
# insert:위치 지정해서 추가
# extend:여러값,새로운 리스트 붙이기

# 과일 리스트
fruits = ["오렌지","사과","배","바나나","키위","사과","바나나"]
print(fruits)

# 리스트에 값 추가
# 리스트 맨 뒤에 값 추가
fruits.append("포도")
print(fruits)

# 특정 위치에 값 추가
fruits.insert(2,"복숭아")
print(fruits)

# 여러값 또는 새로운 리스트 추가
new_fruits = ["수박","체리"]
fruits.extend(new_fruits)
print(fruits)