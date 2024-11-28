n=int(input())
a=[0]*n
# Nhi phan
def Try(i):
    for j in range(0,2):
        a[i]=j
        if i==n-1:
            for k in range(n):
                print(a[k],end=' ')
            print()
        else:
            Try(i+1)
Try(0)

# Hoan vi
vst=[False]*1000
def Try(i):
    for j in range(1,n+1):
        if vst[j]==False:
            vst[j]=True
            a[i]=j
            if i==n-1:
                for k in range(n):
                    print(a[k],end=' ')
                print()
            else:
                Try(i+1)
            vst[j]=False
Try(0)

# To hop
k=int(input())
def Try(i):
    for j in range((a[i-1]+1),(n-k+i+1)):
        a[i]=j
        if i==k:
            for idx in range(1,k+1):
                print(a[idx],end=' ')
            print()
        else:
            Try(i+1)
Try(1)