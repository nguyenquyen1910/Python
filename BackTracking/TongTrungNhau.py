# Tìm các dãy có tổng bằng k cho trước với các phần tử có thể trùng nhau

res = []


def Try(i, ans, sum):
    global n, k, a
    if sum == k:
        res.append(ans[:])
        return
    if sum > k or i >= len(a):
        return
    ans.append(a[i])
    Try(i, ans, sum + a[i])
    ans.pop()
    Try(i + 1, ans, sum)


n, k = map(int, input().split())
a = list(map(int, input().split()))
Try(0, [], 0)
for i in res:
    print(*i)
