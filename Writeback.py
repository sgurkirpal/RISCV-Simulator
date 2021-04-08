def write_back(muxy,l,register_dictionary):
    if(l[0]=='R' or l[0]=='I' or l[0]=='U' or l[0]=='UJ'):
        muxy=muxy[2:]
        muxy+='0'*(8-len(muxy))
        muxy=muxy[6:8]+muxy[4:6]+muxy[2:4]+muxy[:2]
        register_dictionary[int(l[len(l)-1],2)]='0x'+muxy
        return register_dictionary
    else:
        return register_dictionary