sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """나는 소년이고,
파이썬은 쉬워요.
"""
print(sentence3)


jumin = "020405-1234567"
print("성별: " + jumin[7])
print("연: " + jumin[0:2]) # 0부터 2 직전까지 (즉, 0~1)
print("월: " + jumin[2:4])
print("일: " + jumin[4:6])

print("생년월일: " + jumin[:6])
print("뒤 7자리: " + jumin[7:])
print("뒤 7자리 (뒤부터): " + jumin[-7:])
# jumin 에서 마지막 7은 13이기도 하고, -1이기도 함.

python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper()) # python 의 첫 글자가 대문자인가?
print(len(python))
print(python.replace("Python", "Java")) # Python 을 Jave로 바꿔서 출력

index = python.index("n")
print(index) # python 에 n이 몇번째에 있는지를 출력
index = python.index("n", index + 1) # 앞에서부터 두번째 n을 찾아 출력
print(index)

print(python.find("Java")) # 없는 값을 찾으면 -1이 나옴 (이후 과정 계속 진행)
#print(python.index("Java")) # 없는 값을 찾으면 오류가 나옴 (이후 과정 진행 불가)
print(python.count("n")) # n이 몇번 들어가는지를 출력


print("a"+"b") # ab
print("a", "b") # a b

# 방법 1
print("나는 %d살입니다." % 20)
print("나는 %s을 좋아해요." % "파이썬")
print("Apple 은 %c로 시작해요." % "A")
# 사실 %s는 어느 곳에서나 쓸 수 있다
print("나는 %s와 %s를 좋아해요." % ("파란거", "빨간거"))

# 방법 2
print("나는 {}살입니다.".format(20))
print("나는 {}와 {}를 좋아해요.".format("파란거","빨간거"))
print("나는 {0}와 {1}를 좋아해요.".format("파란거","빨간거"))
print("나는 {1}와 {0}를 좋아해요.".format("파란거","빨간거"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="검정"))

# 방법 4
age = 20
color = "검정"
print(f"나는 {age}살이며, {color}색을 좋아해요.")


print("백문이 불여일견\n백견이 불여일타") # 줄바꾸기
print('저는 "나도코딩"입니다.') # 중간에 큰따옴표 넣기 1 (양끝을 작따로)
print("저는 \"나도코딩\"입니다.") # 중간에 큰따옴표 넣기 2 (큰따 앞에 역슬래시)

print("D:\\학교에서쓸꺼\\HUHS\\PythonWorkplace>") # \\는 문장 내에서 \ 하나로 취급
print("Red Zone\rPine") # 커서를 맨 앞으로 옮겨 Pine을 입력 -> PineApple
print("Redd\bZone") # \b로 백스페이스를 입력 -> d 하나 삭제
print("Red\tZone") # 탭