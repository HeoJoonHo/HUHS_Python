menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])
# 튜플은 추가 및 변경이 안됨

name, age, hobby = "김종국", 20 ,"코딩"
print(name, age, hobby)

# 집합(set): 중복 안됨, 순서 없음
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"]) # 위에랑 똑같은건데 형식이 다른거

# 교집합
print(java & python)

# 합집합
print(java | python)

# 차집합
print(java - python)

# python 추가와 제외
python.add("김태호")
java.remove("김태호")

# 자료구조의 변경
menu = {"커피", "우유", "주스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))