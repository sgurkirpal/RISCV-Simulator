#main program file

import fetch
import decode
import execute
import memory
import Writeback
def assemble():
    clock=0
    instruction_dict={}    #dictionary storing instructions
    data_dict={}    #dictionary storing data in memory
    reg={} #registers
    reg[0]='0x0'
    for i in range(32):
        reg[i]='0x00000000'
        if i==2:
            reg[i]='0x7FFFFFF0'
        if i==3:
            reg[i]='0x10000000'
    file=open("data.mc","r")
    memory_cache_dict={}
    no_of_blocks,no_of_sets,memory_cache_dict,kset,blocksize,cachesize=fetch.cacheinitialization()
    instruction_cache_dict={}
    instruction_cache_dict=fetch.instruction_initialization(no_of_sets,k,blocksize)
    instruction_dict,data_dict = fetch.fetch_file(file)
    
    
    pc="0x0"    #initial pc is by default 0x0
    pc_temp="0x0"
    pc_final="0x0"
    instruction_register=None
    return instruction_register,pc,reg,instruction_dict,data_dict,clock,pc_final,pc_temp

def runstep(instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,memory_cache_dict,instruction_cache_dict,no_of_blocks,no_of_Sets,kset,blocksize,cachesize):
    output=""
    if pc not in instruction_dict:
        pc=-1
        return instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,output
    clock+=1
    instruction_register=instruction_dict[pc]
    pc_temp=fetch.increment_pc(pc)
    decoded_info=decode.decode(instruction_register)
    rm=None
    output+="Fetch Instruction "+instruction_register+" from address "+pc+"\n"
    if 'rs2' in decoded_info:
        rm=reg[int(decoded_info['rs2'],2)]
        rm=rm[2:]
        rm="0"*(8-len(rm))+rm
    for x in decoded_info:
        output+=str(x)+" is "+str(decoded_info[x])+"\n"
    #print(rm)
    #print(hex(int(decoded_info['imm'],2)))
    rz,pc_final,temp_string_execute=execute.execute(decoded_info,reg,pc_temp)
    output+=temp_string_execute
    rz=hex(rz)
    if(int(rz,16)<0):
        if(len(rz)!=11):
            rz='-'+rz[1:3]+'0'*(11-len(rz))+rz[3:]
    else:
        if(len(rz)!=10):
            rz=rz[:2]+'0'*(10-len(rz))+rz[2:]
    
    
    muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
    if(decoded_info['opr']=='lw'):
        rz=int(rz,16)
        am,memory_cache_dict=memory.doing_load_cache(hex(rz+3),memorycachedict,block_size,no_of_sets,memory_dictionary)
        am,memory_cache_dict=memory.doing_load_cache(hex(rz+2),memorycachedict,block_size,no_of_sets,memory_dictionary)
        am,memory_cache_dict=memory.doing_load_cache(hex(rz+1),memorycachedict,block_size,no_of_sets,memory_dictionary)
        am,memory_cache_dict=memory.doing_load_cache(hex(rz),memorycachedict,block_size,no_of_sets,memory_dictionary)
    
    elif(l[1]=='lb'):
        am,memory_cache_dict=memory.doing_load_cache(rz,memorycachedict,block_size,no_of_sets,memory_dictionary)

    elif(l[1]=='lh'):
        rz=int(rz,16)
        am,memory_cache_dict=memory.doing_load_cache(hex(rz+1),memorycachedict,block_size,no_of_sets,memory_dictionary)
        am,memory_cache_dict=memory.doing_load_cache(hex(rz),memorycachedict,block_size,no_of_sets,memory_dictionary)
    elif(l[1]=='sw'):
        rz=int(rz,16)
        rm=str(rm)
        memory_cache_dict=memory.doing_store_cache(hex(rz+3),memorycachedict,block_size,no_of_sets,memory_dictionary,int(rm[0:2],2),hit,miss,output)
        memory_cache_dict=memory.doing_store_cache(hex(rz+2),memorycachedict,block_size,no_of_sets,memory_dictionary,int(rm[2:4],2))
        memory_cache_dict=memory.doing_store_cache(hex(rz+1),memorycachedict,block_size,no_of_sets,memory_dictionary,int(rm[4:6],2))
        memory_cache_dict=memory.doing_store_cache(hex(rz+0),memorycachedict,block_size,no_of_sets,memory_dictionary,int(rm[6:8],2))
    elif(l[1]=='sh'):
        rz=int(rz,16)
        rm=str(rm)
        memory_cache_dict=memory.doing_store_cache(hex(rz+1),memorycachedict,block_size,no_of_sets,memory_dictionary,int(rm[4:6],2))
        memory_cache_dict=memory.doing_store_cache(hex(rz+0),memorycachedict,block_size,no_of_sets,memory_dictionary,int(rm[6:8],2)) 
    elif(l[1]=='sb'):
        rm=str(rm)
        memory_cache_dict=memory.doing_store_cache(rz,memorycachedict,block_size,no_of_sets,memory_dictionary,int(rm[6:8],2)) 
    output+=temp_string_memory
    if('rd' in decoded_info):
        if(int(decoded_info['rd'],2)!=0):
            reg,temp_string_writeback=Writeback.write_back(muxy,[decoded_info['type'],decoded_info['opr'],decoded_info['rd']],reg)
            output+=temp_string_writeback
    pc=pc_final
    #print(reg,data_dict)
    return instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,output
