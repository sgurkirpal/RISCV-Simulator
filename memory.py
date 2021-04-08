

def memory(return_address,rz,l,rm,memory_dictionary,pc_temp):
    if(l[1]=='lw'):
        sam=memory_dictionary[rz]
        sam=sam[2:]
        am=sam[6:8]+sam[4:6]+sam[2:4]+sam[:2]
        return am,memory_dictionary
    elif(l[1]=='lb'):
        a=memory_dictionary[rz]
        a=a[2:]
        return '000000'+a[:2],memory_dictionary
    elif(l[1]=='lh'):
        a=memory_dictionary[rz]
        a=a[2:]
        return '0000'+a[:4],memory_dictionary
    elif(l[1]=='jalr'):
        return pc_temp,memory_dictionary
    elif(l[1]=='sw'):
        rm=str(rm)
        am=rm[6:8]+rm[4:6]+rm[2:4]+rm[:2]
        memory_dictionary[rz]='0x'+am
        return rz,memory_dictionary
    elif(l[1]=='sh'):
        rm=str(rm)
        am=rm[6:8]+rm[4:6]
        memory_dictionary[rz]='0x'+am+'0000'
        return rz,memory_dictionary
    elif(l[1]=='sb'):
        rm=str(rm)
        am=rm[6:8]
        memory_dictionary[rz]='0x'+am+'000000'
        return rz,memory_dictionary
    else:
        return rz,memory_dictionary
    