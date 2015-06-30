import numpy as np
def deferred_acceptance(m_pref_input,f_pref_input,caps):
    
    m_pref_array=np.array(m_pref_input)
    f_pref_array=np.array(f_pref_input)
    f_prefsort=np.argsort(f_pref_array)
    m_popu=m_pref_array.shape[0]
    f_popu=f_pref_array.shape[0]
    
    if caps == None:
        caps = [1] * f_popu
    
    caps_array=np.array(caps)
    
    
    free=list(range(m_popu))
    
    
    m_match=np.tile([f_popu],m_popu)

   
    f_accept = {}
    for i in range(f_popu):
        f_accept[i] = []
            
    
    
    while len(free) > 0:
        applyman = free.pop()
        print applyman
        apply_prefs=m_pref_array[applyman]
        print apply_prefs
       
        for prefered in apply_prefs:
            print prefered
            if prefered == f_popu:
                m_match[applyman]=f_popu
                print m_match
                break
            
            else:
                prefered_pref = f_prefsort[prefered]
                print prefered_pref
                rank_apply = prefered_pref[applyman]
                rank_non_match = prefered_pref[m_popu]
                
                if rank_non_match > rank_apply:
                    prefered_accept = f_accept[prefered]
                    print prefered_accept
                    
                    if len(prefered_accept) < caps[prefered]:
                        
                        if len(prefered_accept) == 0:
                            prefered_accept.append(applyman)
                            print prefered_accept
                            m_match[applyman] = prefered
                            print m_match
                            break
                        
                
                        else:
                            for i in range(len(prefered_accept)):
                                
                                rank_already = prefered_pref[prefered_accept[i]]
                                m_match[applyman] = prefered
                                print m_match
                                
                                if rank_already > rank_apply:
                                    prefered_accept.insert(i,applyman)
                                    print prefered_accept
                                    break
                                    
                                else:
                                    if i == len(prefered_accept)-1:
                                        prefered_accept.append(applyman)
                                        print prefered_accept
                            break
                     
                 
                    else:
                        for i in range(len(prefered_accept)): 
                            rank_already = prefered_pref[prefered_accept[i]]
                            
                            if rank_already > rank_apply: 
                                
                                prefered_accept.insert(i,applyman)
                                
                                unmatch_man = prefered_accept.pop()
                                print unmatch_man
                                m_match[unmatch_man]=f_popu
                                m_match[applyman] = prefered
                                print m_match
                                free.append(unmatch_man)
                                print free
                                print prefered_accept
                                break
                                    
                                
                        if applyman in prefered_accept:
                            break
                        
                        else:
                            continue
                            
                
    for i in range(f_popu):
        f_indi = f_accept[i]
        gap = caps[i] - len(f_indi)
        
        if gap > 0:
            residual = [m_popu] * gap
            f_indi.extend(residual)
    
 
    f_match = []
    for i in range(f_popu):
        f_match.extend(f_accept[i])
        
    
    indptr = np.cumsum(caps)
    l_indptr = list(indptr)
    l_indptr.insert(0,0)

    return [list(m_match),f_match,l_indptr]