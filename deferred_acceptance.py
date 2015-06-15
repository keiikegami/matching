def da2(a,b):
    S={}
    free=[]
    T={}
    wfree=[]
    for i in a:
        free.append(i)
    for i in b:
        wfree.append(i)
    c=len(free)
    n=1
    while free:
        m=free.pop()
        f=a[m][n]
        if f not in S:
            S[f]=m
        else:
            l=S[f]
            for j in range(1,c+1):
                if b[f][j]==m:
                    d=j
                else: continue
            for k in range(1,c+1):
                if b[f][k]==l:
                    e=k
                else: continue
            if e<d:
                free.append(m)
                n+=1
            else:
                S[f]=m
                free.append(l)
                n+=1
        if len(free)==0: continue
    g=1
    while wfree:
        m=wfree.pop()
        f=b[m][g]
        if f not in T:
            T[f]=m
        else:
            l=T[f]
            for j in range(1,c+1):
                if a[f][j]==m:
                    d=j
                else: continue
            for k in range(1,c+1):
                if a[f][k]==l:
                    e=k
                else: continue
            if e<d:
                wfree.append(m)
                g+=1
            else:
                T[f]=m
                wfree.append(l)
                g+=1
        if len(wfree)==0:
            return S,T