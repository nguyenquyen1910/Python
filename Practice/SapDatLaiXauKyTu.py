n = int(input())
for t in range(n):
    s1 = input()
    s2 = input()
    print("Test " + str(t + 1) + ": ", end="")
    if len(s1) != len(s2):
        print("NO")
    else:
        if sorted(s1) != sorted(s2):
            print("NO")
        else:
            print("YES")