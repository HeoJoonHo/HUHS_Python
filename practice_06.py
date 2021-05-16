def open_account():
    print("새로운 계좌가 생성되었습니다.")

def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance+money))
    return balance + money

def withdraw(balance, money): #출금
    if (balance >= money):
        print("출금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission

balance = 0 #잔액
balance = deposit(balance, 1000)
#balance = withdraw(balance, 2000)
commission, balance = withdraw_night(balance, 500)
print("수수료 {} 원이며, 잔액은 {} 원입니다.".format(commission, balance))


#def profile(name, age, main_lang):
#    print("이름: {}\t나이: {}\t주 사용 언어: {}".format(name, age, main_lang))

#profile("유재석", 30, "파이썬")
#profile("조세호", 25, "자바")


# 같은 수업의 같은 학년일 경우 기본값을 사용해 쉽게 표기
def profile(name, age = 17, main_lang = "파이썬"):
    print("이름: {}\t나이: {}\t주 사용 언어: {}".format(name, age, main_lang))

profile("김민재")
profile("정준혁")


def profile2(name, age, main_lang):
    print(name, age, main_lang)

profile2(name="김민재", main_lang="파이썬", age=19) #매개변수 키워드를 통해 입력할 경우 순서는 상관없음


def profile3(name, age, *language):
    print("이름: {}\t나이: {}".format(name, age), end=" ") #end=" "은 print가 끝난 후 줄을 바꾸지 않고 같은 줄에 계속 이어나간다는 뜻임.
    for lang in language:
        print(lang, end=" ")
    print()

profile3("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile3("김태호", 25, "Kotlin", "Swift")


gun = 10 #전역변수

def checkpoint(soldiers): #경계근무
    global gun #전역변수 gun 사용
    gun = gun - soldiers #여기 있는 gun은 58번에 있는 gun과 다르므로, 초기화를 따로 하지 않거나 61번처럼 전역변수를 사용하겠다고 말하지 않으면 오류가 발생함
    print("[함수 내] 남은 총: {}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내] 남은 총: {}".format(gun))
    return gun

print("전체 총: {}".format(gun))
#checkpoint(2) #2명이 경계근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총: {}".format(gun))