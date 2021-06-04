for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding = "utf8") as bogo_file:
        bogo_file.write("- " + str(i) + " 주차 주간보고 -")
        bogo_file.write("\n부서 :")
        bogo_file.write("\n이름 :")
        bogo_file.write("\n업무 요약 :")