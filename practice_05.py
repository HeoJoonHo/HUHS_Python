weather = "비"
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요 없어요")

'''
temp = int(input("기온이 어때요?"))
if 30 <= temp:
    print("너무 더워요")
elif 10 <= temp and temp <30:
    print("날씨가 괜찮아요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요")
'''

for waiting_no in range(0, 5):
    print("대기번호: {}".format(waiting_no))

starbucks = ["아이언맨", "토르", "그루트"]
for customer in starbucks:
    print("{}, 커피가 준비되었습니다".format(customer))

'''
sonnim = "토르"
index = 5
while index >= 1:
    print("{}, 커피가 준비되었습니다. {}번 남았습니다.".format(sonnim, index))
    index -= 1
    if index ==0:
        print("커피를 폐기합니다.")

sonnim = "토르"
person = "Unknown"

while person != sonnim: # 이 조건을 만족할 때까지 계속 반복 (!=는 같음을 확인)
    print("{}, 커피가 준비되었습니다.".format(sonnim))
    person = input("이름이 어떻게 되세요?")
'''




absent = [2,5]
nobook = [7]
for student in range(1,11):
    if student in absent:
        continue # 결석한 경우 실행하지 않고 그 번호는 스킵
    elif student in nobook:
        print("오늘 수업 여기까지. {}는 교무실로 따라와.".format(student))
        break
    print("{}, 책 읽어봐".format(student))





students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

member = ["Iron Man", "Thor", "I am Groot"]
member = [len(i) for i in member]
print(member)

members = ["Iron Man", "Thor", "I am Groot"]
members = [i.upper() for i in members]
print (members)