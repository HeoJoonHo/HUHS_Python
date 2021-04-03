subway = [10, 20, 30]
print(subway)

subway = ["정회동", "윤하람", "이희준"]
print(subway)

# 이희준은 몇번째 칸에 있는가?
print(subway.index("이희준"))

# 박성완이 지하철에 또 탔을 경우
subway.append("박성완")
print(subway)

# 김민수가 이희준 앞에 탔을 경우 (넣을 자리 뒤에 있는 애의 번호를 적음)
subway.insert(2, "김민수")
print(subway)

# 맨 끝에 탄 사람부터 한명씩 꺼냄
print(subway.pop())
print(subway.pop())
print(subway)

# 같은 이름의 사람 수 찾기
subway.append("정회동")
print(subway)
print(subway.count("정회동"))

# 정렬하기
numlist = [5,2,3,1,8]
numlist.sort()
print(numlist)

numlist.reverse()
print(numlist)

# 모두 지우기
# numlist.clear()
# print(numlist)

# 다양한 자료형 함께 사용 가능
mixlist = ["정회동", 2003, True]
print(mixlist)

# 리스트 확장 (합치기)
numlist.extend(mixlist)
print(numlist)


cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3]) # 없는 키를 적으면 뒤 과정 진행 불가
print(cabinet.get(100)) # 없는 키를 적어도 뒤 과정 진행 가능
print(cabinet.get(5, "비어있음")) # 없는 키를 적었을 떄 기본값 설정
print(3 in cabinet) # 3이라는 키가 cabinet에 있는가?

locker = {"A-1": "나", "B-2": "너"} # 문자열 키도 사용 가능
print(locker["A-1"])
print("B-2" in locker)

# 새 손님 받기, 기존 손님 갈아치우기
cabinet[235] = "박명수"
cabinet[100] = "황광희"
print(cabinet)

# 손님 퇴장
del cabinet[3]
print(cabinet)

# 각각 출력
print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())

# 폐점
cabinet.clear()
print(cabinet)