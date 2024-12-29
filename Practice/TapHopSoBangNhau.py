n, m = map(int, input().split())
a = list(set(int(i) for i in input().split()))
b = list(set(int(i) for i in input().split()))

print("YES" if a==b else "NO")