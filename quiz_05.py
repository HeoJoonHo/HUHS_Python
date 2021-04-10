from random import*

user = 0
for customer in range(1, 51):
    time = randint(5, 50)
    if 15 < time or 5 > time:
        print("[ ] {}번째 손님 (소요시간 : {}분)".format(customer, time))
    else:
        print("[O] {}번째 손님 (소요시간 : {}분)".format(customer, time))
        user += 1
print("총 탑승 승객: {}분".format(user))