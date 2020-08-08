"""
inputtext = input("파일명만 입력 :")
joins= ".txt"
merge = inputtext + joins
"""

f = open("input.txt", 'r')
ff = f.read().split()
f.close()

ch = input("대문자로1 소문자로2 :")
apk = input("apk 붙일꺼면1 없앨꺼면2 :")
apkplus = ".apk"

f2 = open("result.txt", "w")
for change in ff:
    if ".apk" in change:
        change = change.replace(".apk", "")


    if apk == "1":
        if ch == "1":
                change = change.upper()
        elif ch == "2":
                change = change.lower()
        change = change + apkplus + "\n"

    else:
        if ch == "1":
                change = change.upper()
        elif ch == "2":
                change = change.lower()
        if ".apk" in change:
            change = change.replace(".apk", "\n")
        else:
            change = change + "\n"
    f2.write(change)
f2.close()
"""

"""









