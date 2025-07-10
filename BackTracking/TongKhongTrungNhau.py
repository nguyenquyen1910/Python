# Tìm các dãy có tổng bằng k cho trước với các phần tử chỉ có trong danh sách và mỗi số dùng 1 lần
res = []


def Try(index, ans, sum):
    if sum == k:
        res.append(ans[:])
        return
    if index >= n or sum > k:
        return
    for i in range(index, n):
        if i > index and a[i] == a[i - 1]:
            continue
        ans.append(a[i])
        Try(i + 1, ans, sum + a[i])
        ans.pop()


n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))
Try(0, [], 0)
for i in res:
    print(*i)
