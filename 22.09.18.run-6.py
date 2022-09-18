# indexing:(문자를 숫자로 바꾼다.)(예:[index]game = "브롤스타즈"브=0롤=1스=2타=3즈=4)
# 인덱싱 하기
#game = "브롤스타즈"
#print(game)
#print(game[0],game[1],game[2],game[3],game[-1])

#print(game[5])(X)

# slicing(여러문자를 가져 올 수 있다.)(예:game1:3)

# 슬라이싱 하기
# "롤스"
#print(game[1:3])

#"브롤"
#print(game[:2])

#"스타즈"
#print(game[2:])

animal = "토끼고양이강아지물고기"
rabbit = animal[:2]
cat = animal[2:5]
dog = animal[5:8]
fish = animal[8:]

print(rabbit)
print(cat)
print(dog)
print(fish)