#import sys
#print("A", "B", sep=" and ", end="?")
#print("Hey", "Hello", file=sys.stderr)
#print("Hey", "Hello", file=sys.stdout)

scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust는 좌측정렬, rjust는 우측정렬

#은행 대기순번표
for num in range(1, 6): #1,2,3,4,5
    print("대기번호 : " + str(num).zfill(3)) #zfill은 빈공간을 0으로 채워주며, 총 3칸만큼 하라는 뜻임.

#answer = input("아무 값이나 입력하세요 : ") #input으로 받으면 무조건 문자열(str) 형태로 저장이 됨
#print("입력한 값은 " + answer + "입니다.")

# 빈자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0:>10}".format(500))
# 양수일 때는 +로, 음수일 때는 -로 표시
print("{0:>+10}".format(500))
print("{0:>+10}".format(-500))
# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
# 3자리마다 콤마 찍기, +-도 붙이기
print("{0:+,}".format(-1000103223952))
# 3자리마다 콤마를 찍되 부호를 붙이고 자릿수를 확보 (총 30자리)
# 돈이 많으면 행복하니까 빈자리는 ^로 채움
print("{0:^<+30,}".format(-1000103223952))
# 소수점 출력
print("{0:f}".format(5/3))
# 특정 자릿수까지만 소수점 출력
print("{0:.2f}".format(5/3))

score_file = open("score.txt", "w", encoding="utf8") # 여기서 w는 쓰기 전용
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8") # 덮어쓰지 않고 이어적고싶을 떄 a를 쓴다
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100")
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # r은 읽기용
print(score_file.read())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # 줄별로 읽기, 한 줄 읽고 난 후 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()

score_file = open("score.txt", "r", encoding="utf8") # 총 몇 줄인지를 모를때
while True:
    line = score_file.readline()
    if not line: # 읽어올 내용이 없을 경우
        break
    print(line, end="") # 줄 바꿈 없이 출력
score_file.close()
print("\n")
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
print("\n")

import pickle
profile_file = open("profile.pickle", "wb") # wb는 쓰기(w)+바이너리(b) 피클은 항상 b를 쓰며, utf8같은 인코딩 형식을 정의할 필요도 없음
profile = {"이름":"유지", "나이":30, "취미":["축구", "농구", "배구"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 있는 정보를 profile_file에 저장함
profile_file.close()

profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러옴
print(profile)
profile_file.close()

with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file)) # with는 따로 close할 필요 없음

with open("study.txt", "w", encoding = "utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding = "utf8") as study_file:
    print(study_file.read())