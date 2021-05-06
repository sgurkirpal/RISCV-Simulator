

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
    



def rowConversion(memory_address,block_offset,memory_dictionary,tag,clockcycle,blocksize):
    #memory address should be a string of hex form and it is a normal memory address
    #I am assuming blockoffset value is an integer in decimal format
    l=[1,tag,clockcycle]
    for i in range(block_offset):
        a=hex(int(memory_address,16)-(block_offset-i))
        if a not in memory_dictionary:
            l.append('0x00')
        else:
            l.append(memory_dictionary[a])
    for i in range(block_offset,blocksize):
        a=hex(int(memory_address,16)+i)
        if a not in memory_dictionary:
            l.append('0x00')
        else:
            l.append(memory_dictionary[a])
    return l


def address_conversion(memory_address,block_size,no_of_sets):
    #memory address in hexa form
    dicti={}
    new_mem=bin(int(memory_address,16))
    new_mem=new_mem[2:]
    new_mem='0'*(32-len(new_mem))+new_mem
    import math
    bloc_size=int(math.log(block_size,2))
    sets=int(math.log(no_of_sets,2))
    a=new_mem
    if bloc_size!=0 and len(a)!=0:
        dicti['block_offset']=int(a[len(a)-bloc_size:len(a)],2)
    else:
        dicti['block_offset']=0
    a=a[:len(a)-bloc_size]
    if sets!=0 and len(a)!=0:
        dicti['index']=int(a[len(a)-sets:len(a)],2)
    else:
        dicti['index']=0
    a=a[:len(a)-bloc_size]
    if len(a)==0:
        dicti['tag']=0
    else:
        dicti['tag']=int(a,2)
    dicti['memory_address']=memory_address
    return dicti
    
def lru_policy(l):
    mini=l[0][2]
    val=0
    for i in range(len(l)):
        if(l[i][2]<mini):
            mini=l[i][2]
            val=i
    return val

def doing_load_cache(memory_address,memorycachedict,block_size,no_of_sets,memory_dictionary,clockcycle):
    values={}
    values=address_conversion(memory_address,block_size,no_of_sets)
    for i in range(len(memorycachedict[values['index']])):
        if(memorycachedict[values['index']][i][1]==values['tag']):
            return memorycachedict[values['index']][i][3+values['block_offset']],memorycachedict
    val=lru_policy(memorycachedict[values['index']])
    memorycachedict[values['index']][val]=rowConversion(memory_address,values['block_offset'],memory_dictionary,values['tag'],clockcycle,block_size)
    return memorycachedict[values['index']][val][3+values['block_offset']],memorycachedict


def doing_store_cache(memory_address,memorycachedict,block_size,no_of_sets,memory_dictionary,byte_val,clockcycle):
    values={}
    values=address_conversion(memory_address,block_size,no_of_sets)
    for i in range(len(memorycachedict[values['index']])):
        if(memorycachedict[values['index']][i][1]==values['tag']):
            memorycachedict[values['index']][i][3+values['block_offset']]=hex(byte_val)
    val=lru_policy(memorycachedict[values['index']])
    memorycachedict[values['index']][val]=rowConversion(memory_address,values['block_offset'],memory_dictionary,values['tag'],clockcycle,block_size)
    memorycachedict[values['index']][i][3+values['block_offset']]=hex(byte_val)
    return memorycachedict
