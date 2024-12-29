s1 = input().strip().lower().split()
s2 = input().strip().lower().split()

intersection = sorted(set(s1) & set(s2))
union = sorted(set(s1) | set(s2))
print(" ".join(union))
print(" ".join(intersection))
