def memory(return_address,rz,l,rm):
    if(l[0]=='R' or l[0]=='I'):
        return rz
    elif(l[0]=='S'):
        #we need one structure for memory where we store memory
        