animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "입니다.")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요.")
print(name + "는 어른일까요? " + str(is_adult))

print(2**3)
print(8%3)
print(10//3)

print(1 != 3) #true
print(not(1 != 5)) #false

print((3>0) and (4<0)) #false
print((3>0) & (4<0)) #false
print((3>0) or (4<0)) #true
print((3>0) | (4<0)) #true

num = 16
print(num)
num += 2 #num = num + 2 와 같은 의미
print(num)
num *= 2
print(num)
num /= 2
print(num)
num -= 2
print(num)
num %= 5
print(num)

print(abs(-5)) #절댓값
print(pow(4,2)) #4^2
print(max(5,23)) #최댓값
print(min(5,23)) #최솟값
print(round(3.14)) #반올림

from math import *
print(floor(4.99)) #내림
print(ceil(3.14)) #올림
print(sqrt(81)) #제곱근

from random import *
print(random()) #0.0 ~ 1.0 미만의 임의의 값
print(random()*10) #0.0 ~ 10.0 미만의 임의의 값
print(int(random()*10)) #0.0 ~ 10.0 미만의 임의의 정수
print(int(random()*10+1)) #1 ~ 10 이하의 임의의 정수

print(randrange(1,46))
print(randint(1, 45)) # 두 범위는 같다.
