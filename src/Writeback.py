def write_back(muxy,l,register_dictionary):
    if(l[0]=='R' or l[0]=='I' or l[0]=='U' or l[0]=='UJ'):
        #muxy=muxy[2:]
        #muxy+='0'*(8-len(muxy))
        #muxy=muxy[6:8]+muxy[4:6]+muxy[2:4]+muxy[:2]
        output="WRITEBACK: Register "+str(int(l[len(l)-1],2))+" updated with " +str(muxy)+".\n"
        register_dictionary[int(l[len(l)-1],2)]=muxy
        return register_dictionary,output
    else:
        output="WRITEBACK: No writeback operation.\n"
        return register_dictionary,output