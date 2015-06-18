def da3(P,Q):
    S=np.tile([-1],P.shape[0])
    free=range(P.shape[0])
    n=0
    while free:
        A=free.pop() 
        F=P[A,:][n]
        if F not in S:
            S[A]=F
            n=0        #nをリセット
        elif F==8:
            S[A]=8
        else:
            for y in range(5):
                if S[y]==F:
                    M=y #MはFがいる場所のindex
            for z in range(6):
                if Q[F,:][z]==M:
                    Z=z
                if Q[F,:][z]==A:
                    W=z
                if Q[F,:][z]==5:
                    V=z
            if V<W and V<Z:
                S[M]=-1
                free.append(A)    
                free.append(M)
                n+=1
            elif W<Z and W<V:
                S[A]=F
                S[M]=-1
                free.append(M)
                n+=1
            elif Z<W and Z<V:
                free.append(A)
                n+=1
        if len(free)==0:
            print S              