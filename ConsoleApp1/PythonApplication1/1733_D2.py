t=int(input())
while t:
    n,x,y=map(int,input().split(' '))
    a,b=input(),input()
    Indexes=[]
    Changes=[]
    for i in range(n):
        if a[i]!=b[i]:
            Indexes.append(i)
    if len(Indexes)%2!=0:
        print(-1)
    else:
        for i in range(1,len(Indexes),1):
           Changes.append(Indexes[i]-Indexes[i-1])
        print(*Changes)    

    t-=1    
    input("Press Enter To End ...")