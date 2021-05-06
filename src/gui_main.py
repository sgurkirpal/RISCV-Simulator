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
    if no_of_sets==0:
        print("Invalid Input")
    instruction_cache_dict={}
    instruction_cache_dict=fetch.instruction_initialization(no_of_sets,kset,blocksize)
    instruction_dict,data_dict = fetch.fetch_file(file)
    
    pc="0x0"    #initial pc is by default 0x0
    pc_temp="0x0"
    pc_final="0x0"
    instruction_register=None
    Ins_hit=0
    Ins_miss=0
    Ins_access=0
    hit=0
    miss=0
    total_access=0
    cache_list=[memory_cache_dict,no_of_blocks,no_of_sets,blocksize,cachesize,instruction_cache_dict,hit,miss,total_access,Ins_hit,Ins_miss,Ins_access]
    return instruction_register,pc,reg,instruction_dict,data_dict,clock,pc_final,pc_temp,cache_list

def runstep(instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,cache_list):
    memory_cache_dict=cache_list[0]
    no_of_blocks=cache_list[1]
    no_of_sets=cache_list[2]
    blocksize=cache_list[3]
    cachesize=cache_list[4]
    instruction_cache_dict=cache_list[5]
    hit=cache_list[6]
    miss=cache_list[7]
    total_access=cache_list[8]
    Ins_hit=cache_list[9]
    Ins_miss=cache_list[10]
    Ins_access=cache_list[11]
    output=""
    pc="0x"+(10-len(pc))*'0'+pc[2:]
    if pc not in instruction_dict:
        pc=-1
        output+="Total Number of Data Cache Accesses: "+str(total_access)+"\n"+\
            "Total number of Misses in Data Cache: "+str(miss)+"\n"+\
                "Total number of Hits in Data Cache: "+str(hit)+"\n"+\
                    "Total Number of Instruction Cache Accesses: "+str(Ins_access)+"\n"+\
            "Total number of Misses in Instruction Cache: "+str(Ins_miss)+"\n"+\
                "Total number of Hits in Instruction Cache: "+str(Ins_hit)+"\n"
        cache_list=[memory_cache_dict,no_of_blocks,no_of_sets,blocksize,cachesize,instruction_cache_dict,hit,miss,total_access,Ins_hit,Ins_miss,Ins_access]
        return instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,output,cache_list
    clock+=1
    Ins_access+=4
    instruction_register,Ins_hit,Ins_miss,output=fetch.retrievingmachinecode(pc,instruction_dict,instruction_cache_dict,blocksize,no_of_sets,clock,Ins_hit,Ins_miss,output)
    #instruction_register=instruction_dict[pc]
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
        total_access+=4
        rz=int(rz,16)
        muxy='0x'
        am,memory_cache_dict,hit,miss,output=memory.doing_load_cache(hex(rz+3),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss,output)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
        am,memory_cache_dict,hit,miss,output=memory.doing_load_cache(hex(rz+2),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss,output)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
        am,memory_cache_dict,hit,miss,output=memory.doing_load_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss,output)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
        am,memory_cache_dict,hit,miss,output=memory.doing_load_cache(hex(rz),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss,output)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]

    elif(decoded_info['opr']=='lb'):
        total_access+=1
        muxy='0x'
        am,memory_cache_dict,hit,miss,output=memory.doing_load_cache(rz,memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss,output)
        if(len(am)==3):
            muxy+='0000000'+am[2]

        else:
            if(am[2]>=0x8):
                muxy+='111111'+am[2:4]
            else:
                muxy+='000000'+am[2:4]

    elif(decoded_info['opr']=='lh'):
        total_access+=2
        rz=int(rz,16)
        muxy='0x'
        am,memory_cache_dict,hit,miss,output=memory.doing_load_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss,output)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
        am,memory_cache_dict,hit,miss,output=memory.doing_load_cache(hex(rz),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss,output)
        if(len(am)==3):
            muxy+='0'+am[2]
        else:
            muxy+=am[2:4]
            if(muxy[2]>=0x8):
                muxy='0x1111'+muxy[2:]
            else:
                muxy='0x0000'+muxy[2:]
        
    elif(decoded_info['opr']=='sw'):
        total_access+=4
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
        rz=int(rz,16)
        rm=str(rm)
        memory_cache_dict,hit,miss,output=memory.doing_store_cache(hex(rz+3),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[0:2],16),clock,hit,miss,output)
        memory_cache_dict,hit,miss,output=memory.doing_store_cache(hex(rz+2),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[2:4],16),clock,hit,miss,output)
        memory_cache_dict,hit,miss,output=memory.doing_store_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[4:6],16),clock,hit,miss,output)
        memory_cache_dict,hit,miss,output=memory.doing_store_cache(hex(rz+0),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock,hit,miss,output)
    
    elif(decoded_info['opr']=='sh'):
        total_access+=2
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
        rz=int(rz,16)
        rm=str(rm)
        memory_cache_dict,hit,miss,output=memory.doing_store_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[4:6],16),clock,hit,miss,output)
        memory_cache_dict,hit,miss,output=memory.doing_store_cache(hex(rz+0),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock,hit,miss,output) 
    
    elif(decoded_info['opr']=='sb'):
        total_access+=1
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
        rm=str(rm)
        memory_cache_dict,hit,miss,output=memory.doing_store_cache(rz,memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock,hit,miss,output)
    
    else:
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)

    #output+=temp_string_memory
    if('rd' in decoded_info):
        if(int(decoded_info['rd'],2)!=0):
            reg,temp_string_writeback=Writeback.write_back(muxy,[decoded_info['type'],decoded_info['opr'],decoded_info['rd']],reg)
            output+=temp_string_writeback
    pc=pc_final
    #print(reg,data_dict)
    cache_list=[memory_cache_dict,no_of_blocks,no_of_sets,blocksize,cachesize,instruction_cache_dict,hit,miss,total_access,Ins_hit,Ins_miss,Ins_access]
    return instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,output,cache_list
