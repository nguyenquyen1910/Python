# Trả về vị trí 2 số đầu tiêntiên trong dãy có tổng bằng k cho trước
def solve(a, n, k):
    cnt = {}
    for i in range(n):
        tmp = k - a[i]
        if tmp in cnt:
            print(cnt[tmp], i)
            return
        cnt[a[i]] = i
    print("Not Found")


n, k = map(int, input().split())
a = list(map(int, input().split()))
solve(a, n, k)
