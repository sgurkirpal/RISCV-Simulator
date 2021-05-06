#main program file

import fetch
import decode
import execute
import memory
import Writeback
def assemble(input_list):
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
    no_of_blocks,no_of_sets,memory_cache_dict,kset,blocksize,cachesize=fetch.cacheinitialization(input_list)
    instruction_cache_dict={}
    instruction_cache_dict=fetch.instruction_initialization(no_of_sets,kset,blocksize)
    instruction_dict,data_dict = fetch.fetch_file(file)
    
    pc="0x0"    #initial pc is by default 0x0
    pc_temp="0x0"
    pc_final="0x0"
    instruction_register=None
    cache_list=[memory_cache_dict,no_of_blocks,no_of_sets,blocksize,cachesize,instruction_cache_dict]
    return instruction_register,pc,reg,instruction_dict,data_dict,clock,pc_final,pc_temp,cache_list
def runstep(instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,cache_list):
    memory_cache_dict=cache_list[0]
    no_of_blocks=cache_list[1]
    no_of_sets=cache_list[2]
    blocksize=cache_list[3]
    cachesize=cache_list[4]
    instruction_cache_dict=cache_list[5]
    output=""
    if pc not in instruction_dict:
        pc=-1
        return instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,output,cache_list
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
    
    
    if(decoded_info['opr']=='lw'):
        rz=int(rz,16)
        muxy='0x'
        am,memory_cache_dict=memory.doing_load_cache(hex(rz+3),memory_cache_dict,blocksize,no_of_sets,data_dict,clock)
        print(type(am))
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
        am,memory_cache_dict=memory.doing_load_cache(hex(rz+2),memory_cache_dict,blocksize,no_of_sets,data_dict,clock)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
        am,memory_cache_dict=memory.doing_load_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,clock)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
        am,memory_cache_dict=memory.doing_load_cache(hex(rz),memory_cache_dict,blocksize,no_of_sets,data_dict,clock)
        print(am)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]

    elif(decoded_info['opr']=='lb'):
        muxy='0x'
        am,memory_cache_dict=memory.doing_load_cache(rz,memory_cache_dict,blocksize,no_of_sets,data_dict,clock)
        if(len(am)==3):
            muxy+='0000000'+am[2]

        else:
            if(am[2]>=0x8):
                muxy+='111111'+am[2:4]
            else:
                muxy+='000000'+am[2:4]

    elif(decoded_info['opr']=='lh'):
        rz=int(rz,16)
        muxy='0x'
        am,memory_cache_dict=memory.doing_load_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,clock)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
        am,memory_cache_dict=memory.doing_load_cache(hex(rz),memory_cache_dict,blocksize,no_of_sets,data_dict,clock)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
            if(muxy[2]>=0x8):
                muxy='0x1111'+muxy[2:]
            else:
                muxy='0x0000'+muxy[2:]
        
    elif(decoded_info['opr']=='sw'):
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
        rz=int(rz,16)
        rm=str(rm)
        memory_cache_dict=memory.doing_store_cache(hex(rz+3),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[0:2],16),clock)
        memory_cache_dict=memory.doing_store_cache(hex(rz+2),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[2:4],16),clock)
        memory_cache_dict=memory.doing_store_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[4:6],16),clock)
        memory_cache_dict=memory.doing_store_cache(hex(rz+0),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock)
    elif(decoded_info['opr']=='sh'):
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
        rz=int(rz,16)
        rm=str(rm)
        memory_cache_dict=memory.doing_store_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[4:6],16),clock)
        memory_cache_dict=memory.doing_store_cache(hex(rz+0),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock) 
    elif(decoded_info['opr']=='sb'):
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
        rm=str(rm)
        memory_cache_dict=memory.doing_store_cache(rz,memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock)
    else:
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)

    #output+=temp_string_memory
    if('rd' in decoded_info):
        if(int(decoded_info['rd'],2)!=0):
            reg,temp_string_writeback=Writeback.write_back(muxy,[decoded_info['type'],decoded_info['opr'],decoded_info['rd']],reg)
            output+=temp_string_writeback
    pc=pc_final
    #print(reg,data_dict)
    return instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,output,cache_list
