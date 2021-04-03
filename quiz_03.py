url = "https://google.com"
first =  url[8:]
index = first.index(".")
site = first[:index]

pw = site[:3] + str(len(site)) + str(site.count("e")) + "!"
print(str(url) + "의 비밀번호: " + str(pw))