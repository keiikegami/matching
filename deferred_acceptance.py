def da3(P,Q):
    import sys
    
    if isinstance(Q, list) != True and isinstance(Q,np.ndarray) != True:
        print "Input Error!!"
        sys.exit()
        
    if isinstance(P, list):
        P = np.array(P)
        Q = np.array(Q)
    elif isinstance(P, np.ndarray):
        print "ndarray"
    else:
        print "Input Error!!"
        sys.exit()
    N=P.shape[0]
    G=Q.shape[0]
    S=np.tile([-1],N)
    free=range(N)
    n=0
    
    while free:
        # print S
        """
        上のシャープを外すことで男性の婚約状況の一周ごとの推移を表示することができます
        正しくない結果が返ってきている疑いのある時に様子を見るため使いましょう
        """
        A=free.pop() 
        F=P[A,:][n]
        if F==G:
            S[A]=G
        else:
            for J in range(N+1):   
                if Q[F,:][J]==A:
                    D=J
                if Q[F,:][J]==N:
                    E=J
            if E<D:
                free.append(A)
                n+=1
            else:
                if F not in S:
                    S[A]=F
                    n=0        
                else:
                    for y in range(N):
                        if S[y]==F:
                            M=y         
                    for z in range(N+1):
                        if Q[F,:][z]==M:
                            Z=z
                        if Q[F,:][z]==A:
                            W=z
                    if W<Z:
                        S[A]=F
                        S[M]=-1
                        free.append(M)
                        n+=1
                    else:
                        free.append(A)
                        n+=1
        if len(free)==0:   
            s=list(S)
            L=np.tile([N],G)
            l=list(L)
            for u in s:
                if u==G: continue  
                else:
                    v=s.index(u)
                    l[u]=v
            return s,l
        else: continue