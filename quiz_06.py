def std_weight(height, gender):
    if (gender == "남자"): return 0.0001*height*height*22
    else: return 0.0001*height*height*21

height = 175
gender = "남자"

print("키 {}cm {}의 표준 체중은 {}kg 입니다.".format(height, gender, round(std_weight(height, gender),2)))