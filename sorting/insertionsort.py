def insertion_sort(a):
    l=len(a)
    for i in range(l-1):
        m=min(a[i:])
        s=a.index(m)
        a[i],a[s]=a[s],a[i]
    print(a)

a=list(map(int,input().split()))
insertion_sort(a)
