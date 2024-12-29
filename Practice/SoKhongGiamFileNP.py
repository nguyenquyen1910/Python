import pickle
from collections import Counter

def check(n):
    n = str(n)
    if len(n) < 2:
        return False
    for i in range(len(n) - 1):
        if n[i] > n[i + 1]:
            return False
    return True

try:
    with open("DATA1.in", "rb") as f1, open("DATA2.in", "rb") as f2:
        data1 = pickle.load(f1)
        data2 = pickle.load(f2)

    list1 = list(int(i) for i in data1 if check(i))
    list2 = list(int(i) for i in data2 if check(i))

    cnt1 = Counter(list1)
    cnt2 = Counter(list2)

    res = sorted(set(list1) & set(list2))
    for i in res:
        print(f"{i} {cnt1[i]} {cnt2[i]}")
except FileNotFoundError as e:
    print(e)