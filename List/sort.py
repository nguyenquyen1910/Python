n=int(input())
a=[int(i) for i in input().split()]

def linearSort(a,n):
    for i in range(n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
        print('Buoc',i+1,':',' '.join(map(str,a))) # Thay cho vong lap for 

def selectionSort(a,n):
    for i in range(n-1):
        min_index=i
        for j in range(i+1,n):
            if a[j]<a[min_index]:
                min_index=j
        a[i],a[min_index]=a[min_index],a[i]
        print('Buoc',i+1,':',' '.join(map(str,a)))

def insertionSort(a,n):
    for i in range(0,n):
        key=a[i]
        j=i-1
        while j>=0 and a[j]>key:
            a[j+1]=a[j]
            j-=1
        a[j+1]=key
        for k in range(0,i+1):
            print(a[k],end=' ')
        print()
def bubbleSort(a,n):
    m=1
    for i in range(n-1):
        ok=True
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                ok=False
        if ok==True:
            break
        print('Buoc',m,':',' '.join(map(str,a)))
        m+=1
a.sort() # Co do phuc tap la O(nlogn)