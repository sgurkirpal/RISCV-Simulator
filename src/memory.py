

def memory(return_address,rz,l,rm,memory_dictionary,pc_temp):
    if(l[1]=='lw'):
        rz=int(rz,16)
        output="MEMORY: Loaded values from addresses: "+str(rz)+" "+str(rz+1)+" "+str(rz+2)+" "+str(rz+3)+".\n"
        am='0x'
        if(hex(rz+3) in memory_dictionary):
            am+=memory_dictionary[hex(rz+3)][2:]
        else:
            am+='00'
        if(hex(rz+2) in memory_dictionary):
            am+=memory_dictionary[hex(rz+2)][2:]
        else:
            am+='00'
        if(hex(rz+1) in memory_dictionary):
            am+=memory_dictionary[hex(rz+1)][2:]
        else:
            am+='00'
        if(hex(rz) in memory_dictionary):
            am+=memory_dictionary[hex(rz)][2:]
        else:
            am+='00'
        return am,memory_dictionary,output
    elif(l[1]=='lb'):
        output="MEMORY: Loaded values from address: "+str(rz)+" .\n"
        am='0x'
        if(rz in memory_dictionary):
            am+=memory_dictionary[hex(rz)][2:]
        else:
            am+='00'
        if(am[2]<0x8):
            return '0x000000'+am[2:],memory_dictionary,output
        else:
            return '0x111111'+am[2:],memory_dictionary,output
    elif(l[1]=='lh'):
        rz=int(rz,16)
        output="MEMORY: Loaded values from addresses: "+str(rz)+" "+str(rz+1)+".\n"
        am='0x'
        if(hex(rz+1) in memory_dictionary):
            am+=memory_dictionary[hex(rz+1)][2:]
        else:
            am+='00'
        if(hex(rz) in memory_dictionary):
            am+=memory_dictionary[hex(rz)][2:]
        else:
            am+='00'
        if(am[2]<0x8):
            return '0x0000'+am[2:],memory_dictionary,output
        else:
            return '0x1111'+am[2:],memory_dictionary,output
    elif(l[1]=='jalr'):
        output="MEMORY: No memory operation.\n"
        return pc_temp,memory_dictionary,output
    elif(l[1]=='sw'):
        rz=int(rz,16)
        rm=str(rm)
        output="MEMORY: Stored "+str(rm)+" into addresses: "+str(rz)+" "+str(rz+1)+" "+str(rz+2)+" "+str(rz+3)+".\n"
        memory_dictionary[hex(rz+3)]='0x'+rm[0:2]
        memory_dictionary[hex(rz+2)]='0x'+rm[2:4]
        memory_dictionary[hex(rz+1)]='0x'+rm[4:6]
        memory_dictionary[hex(rz)]='0x'+rm[6:8]
        return rz,memory_dictionary,output
    elif(l[1]=='sh'):
        rz=int(rz,16)
        rm=str(rm)
        output="MEMORY: Stored "+str(rm)+" into addresses: "+str(rz)+" "+str(rz+1)+".\n"
        memory_dictionary[hex(rz+1)]='0x'+rm[4:6]
        memory_dictionary[hex(rz)]='0x'+rm[6:8]
        return rz,memory_dictionary,output
    elif(l[1]=='sb'):
        rm=str(rm)
        memory_dictionary[rz]='0x'+rm[6:8]
        output="MEMORY: Stored "+str(rm)+" into addresses: "+str(rz)+".\n"
        return rz,memory_dictionary,output
    else:
        output="MEMORY: No memory operation.\n"
        return rz,memory_dictionary,output
    