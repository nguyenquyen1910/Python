def testCase():
    cnt4 = 0
    cnt7 = 0
    s = list(input())
    for i in s:
        if i == "4":
            cnt4 += 1
        elif i == "7":
            cnt7 += 1
    if cnt4 + cnt7 == 4 or cnt4 + cnt7 == 7:
        print("YES")
    else:
        print("NO")


testCase()
