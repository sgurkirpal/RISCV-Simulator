#main program file

import fetch
import decode
import execute
import memory
import Writeback
from math import ceil
def assemble(input_list):
    buffers={}
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
    decoded_info={}
    rz=hex(0)
    rm=hex(0)
    muxy=hex(0)
    btb={}
    mem_pc=[]
    write_pc=[]
    execute_pc=[]
    decode_pc=[]
    fetch_pc=[]
    buffer_var=0
    buffer_val_for_rd={}
    for i in range(32):
        buffer_val_for_rd[i]=-1
    #print(decoded_info["0x0"])
    if("0x4" in instruction_dict):
        fetch_pc.append("0x4")
    decode_pc.append("0x0")
    #print("ffffff",buffer_val_for_rd)
    control_inst=False
    remove_decode=False
    dummy_val=0
    buffer_memory={}
    new_var=0
    flowchart_list=["0x0","0x4"]
    output=""
    number_of_instructions=0
    number_of_load_instruction=0
    number_of_store_instruction=0
    number_of_control_instructions=0
    number_of_stall_instructions=0
    number_of_mispredictions=0
    number_of_datahazards=0
    number_of_contolhazards=0
    number_of_stalls_datahazards=0
    number_of_stalls_contolhazards=0
    number_of_alu_instructions=0
    hit=0
    miss=0
    total_access=0
    hit_miss_btb=-1
    cache_list=[memory_cache_dict,no_of_blocks,no_of_sets,blocksize,cachesize,instruction_cache_dict,hit,miss,total_access]    
    varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output,
        number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,number_of_stall_instructions,
        number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions,buffers,hit_miss_btb]
    return reg,instruction_dict,data_dict,clock,varlist,cache_list
def runstep(reg,instruction_dict,data_dict,clock,varlist,cache_list):
    pc=varlist[0]
    pc_temp=varlist[1]
    decoded_info=varlist[2]
    rz=varlist[3]
    rm=varlist[4]
    muxy=varlist[5]
    btb=varlist[6]
    mem_pc=varlist[7]
    write_pc=varlist[8]
    execute_pc=varlist[9]
    decode_pc=varlist[10]
    fetch_pc=varlist[11]
    buffer_var=varlist[12]
    buffer_val_for_rd=varlist[13]
    control_inst=varlist[14]
    remove_decode=varlist[15]
    dummy_val=varlist[16]
    buffer_memory=varlist[17]
    new_var=varlist[18]
    flowchart_list=varlist[19]
    output=varlist[20]
    memory_cache_dict=cache_list[0]
    no_of_blocks=cache_list[1]
    no_of_sets=cache_list[2]
    blocksize=cache_list[3]
    cachesize=cache_list[4]
    instruction_cache_dict=cache_list[5]
    hit=cache_list[6]
    miss=cache_list[7]
    total_access=cache_list[8]
    output=""
    number_of_instructions=varlist[21]
    number_of_load_instruction=varlist[22]
    number_of_store_instruction=varlist[23]
    number_of_control_instructions=varlist[24]
    number_of_stall_instructions=varlist[25]
    number_of_mispredictions=varlist[26]
    number_of_datahazards=varlist[27]
    number_of_contolhazards=varlist[28]
    number_of_stalls_datahazards=varlist[29]
    number_of_stalls_contolhazards=varlist[30]
    number_of_alu_instructions=varlist[31]
    buffers=varlist[32]
    hit_miss_btb=varlist[33]
    new_var+=4
    if pc==-1:
        output+="Number of clock cycles ="+str(clock)+"\n"+\
    "Total number of instructions executed = "+str(number_of_instructions)+"\n"+\
    "CPI value calculated = "+str(clock/number_of_instructions)+"\n"+\
    "Total number of load/store instructions = " + str(number_of_load_instruction+number_of_store_instruction)+"\n"+\
    "Number of ALU instructions = "+str(number_of_instructions-number_of_alu_instructions)+"\n"+\
    "Number of control instructions = "+ str(number_of_control_instructions)+"\n"+\
    "Number of bubbles and stalls in the pipeline = "+str(clock-number_of_instructions)+"\n"+\
    "Number of data hazards = "+str(number_of_datahazards)+"\n"+\
    "Number of control hazards = "+str(number_of_mispredictions)+"\n"+\
    "Number of branch mispredictions = "+ str(number_of_mispredictions)+"\n"+\
    "Number of stalls due to data hazards = "+str(clock-number_of_instructions-number_of_mispredictions)+"\n"+\
    "Number of stalls due to control hazards = "+str(number_of_mispredictions)+"\n"
        return output
    if len(write_pc)==0 and len(mem_pc)==0 and len(execute_pc)==0 and len(decode_pc)==0:
        varlist=[-1,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output,
                number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,number_of_stall_instructions,
                number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions,buffers,hit_miss_btb]    
        return reg,instruction_dict,data_dict,clock,varlist,cache_list
    clock+=1

    #write_back
    if len(write_pc)!=0:
        this_pc=write_pc[0]
        write_pc.pop(0)
        number_of_instructions+=1
        opr=decoded_info[this_pc]['opr']
        if(decoded_info[this_pc]['opr']=='lw' or decoded_info[this_pc]['opr']=='ld' or decoded_info[this_pc]['opr']=='lb' or decoded_info[this_pc]['opr']=='lh'):
            number_of_load_instruction+=1
        if(decoded_info[this_pc]['opr']=='sw' or decoded_info[this_pc]['opr']=='sd' or decoded_info[this_pc]['opr']=='sb' or decoded_info[this_pc]['opr']=='sh'):
            number_of_store_instruction+=1
        if(opr=='jal' or opr=='jalr' or opr=='beq' or opr=='bne' or opr=='bge' or opr=='blt'):
            number_of_alu_instructions+=1
        if('rd' in decoded_info[this_pc]):
            if(int(decoded_info[this_pc]['rd'],2)!=0):
                reg,temp_string_writeback=Writeback.write_back(muxy,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr'],decoded_info[this_pc]['rd']],reg)
                output+=temp_string_writeback

    #memory
    if len(mem_pc)!=0:
        this_pc=mem_pc[0]
        mem_pc.pop(0)
        write_pc.append(this_pc)

        rm=None
        if 'rs2' in decoded_info[this_pc]:
            rm=reg[int(decoded_info[this_pc]['rs2'],2)]
            rm=rm[2:]
            rm="0"*(8-len(rm))+rm
        if(int(rz,16)<0):
            if(len(rz)!=11):
                rz='-'+rz[1:3]+'0'*(11-len(rz))+rz[3:]
        else:
            if(len(rz)!=10):
                rz=rz[:2]+'0'*(10-len(rz))+rz[2:]


        if(decoded_info[this_pc]['opr']=='lw'):
            rz=int(rz,16)
            muxy='0x'
            am,memory_cache_dict,hit,miss=memory.doing_load_cache(hex(rz+3),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss)
            if(len(am)==3):
                muxy+='0'+am[2]
            else:
                muxy+=am[2:4]
            am,memory_cache_dict,hit,miss=memory.doing_load_cache(hex(rz+2),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss)
            if(len(am)==3):
                muxy+='0'+am[2]
            else:
                muxy+=am[2:4]
            am,memory_cache_dict,hit,miss=memory.doing_load_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss)
            if(len(am)==3):
                muxy+='0'+am[2]
            else:
                muxy+=am[2:4]
            am,memory_cache_dict,hit,miss=memory.doing_load_cache(hex(rz),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss)
            if(len(am)==3):
                muxy+='0'+am[2]
            else:
                muxy+=am[2:4]

        elif(decoded_info[this_pc]['opr']=='lb'):
            muxy='0x'
            am,memory_cache_dict,hit,miss=memory.doing_load_cache(rz,memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss)
            if(len(am)==3):
                muxy+='0000000'+am[2]

            else:
                if(am[2]>=0x8):
                    muxy+='111111'+am[2:4]
                else:
                    muxy+='000000'+am[2:4]

        elif(decoded_info[this_pc]['opr']=='lh'):
            rz=int(rz,16)
            muxy='0x'
            am,memory_cache_dict,hit,miss=memory.doing_load_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss)
            if(len(am)==3):
                muxy+='0'+am[2]
            else:
                muxy+=am[2:4]
            am,memory_cache_dict,hit,miss=memory.doing_load_cache(hex(rz),memory_cache_dict,blocksize,no_of_sets,data_dict,clock,hit,miss)
            if(len(am)==3):
                muxy+='0'+am[2]
            else:
                muxy+=am[2:4]
                if(muxy[2]>=0x8):
                    muxy='0x1111'+muxy[2:]
                else:
                    muxy='0x0000'+muxy[2:]
            
        elif(decoded_info[this_pc]['opr']=='sw'):
            muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr']],rm,data_dict,pc_temp)
            rz=int(rz,16)
            rm=str(rm)
            memory_cache_dict,hit,miss=memory.doing_store_cache(hex(rz+3),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[0:2],16),clock,hit,miss)
            memory_cache_dict,hit,miss=memory.doing_store_cache(hex(rz+2),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[2:4],16),clock,hit,miss)
            memory_cache_dict,hit,miss=memory.doing_store_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[4:6],16),clock,hit,miss)
            memory_cache_dict,hit,miss=memory.doing_store_cache(hex(rz+0),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock,hit,miss)
        elif(decoded_info[this_pc]['opr']=='sh'):
            muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr']],rm,data_dict,pc_temp)
            rz=int(rz,16)
            rm=str(rm)
            memory_cache_dict,hit,miss=memory.doing_store_cache(hex(rz+1),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[4:6],16),clock,hit,miss)
            memory_cache_dict,hit,miss=memory.doing_store_cache(hex(rz+0),memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock,hit,miss) 
        elif(decoded_info[this_pc]['opr']=='sb'):
            muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr']],rm,data_dict,pc_temp)
            rm=str(rm)
            memory_cache_dict,hit,miss=memory.doing_store_cache(rz,memory_cache_dict,blocksize,no_of_sets,data_dict,int(rm[6:8],16),clock,hit,miss)
        else:
            muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr']],rm,data_dict,pc_temp)

        #muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr']],rm,data_dict,pc_temp)
        if this_pc not in buffers:
            buffers[this_pc]={}
            buffers[this_pc]['mem']=muxy
        else:
            buffers[this_pc]['mem']=muxy
        #output+=temp_string_memory


    #execute
    if len(execute_pc)!=0:
        this_pc=execute_pc[0]
        for x in decoded_info[this_pc]:
            output+=str(x)+" is "+str(decoded_info[this_pc][x])+"\n"
        execute_pc.pop(0)
        mem_pc.append(this_pc)

        pc_temp=fetch.increment_pc(this_pc)
        rz,pc_final,temp_string_execute=execute.execute(decoded_info[this_pc],reg,pc_temp)
        output+=temp_string_execute
        rz=hex(rz)
        if this_pc not in buffers:
            buffers[this_pc]={}
            buffers[this_pc]['exe']=rz
        else:
            buffers[this_pc]['exe']=rz
        if control_inst:
            control_inst=False
            if this_pc in btb:
                if pc_final==btb[this_pc]:
                    output+="Prediction Successful ! for pc, "+str(this_pc)+"\n"
                    hit_miss_btb=1
                    pass
                else:
                    output+="Prediction MisMatched ! for pc, "+str(this_pc)+"\n"
                    hit_miss_btb=0
                    number_of_mispredictions+=1
                    remove_decode=True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if len(decode_pc)==1:
                            if decode_pc[0]==pc_final:
                                remove_decode=False
            else:
                btb[this_pc]=pc_final
                if pc_final==fetch.increment_pc(this_pc):
                    output+="Prediction Successful ! for pc, "+str(this_pc)+"\n"
                    hit_miss_btb=1
                    pass
                else:
                    output+="Prediction MisMatched ! for pc, "+str(this_pc)+"\n"
                    hit_miss_btb=0
                    number_of_mispredictions+=1
                    remove_decode=True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if decode_pc[0]==pc_final:
                            remove_decode=False

    #decode 
    if(dummy_val>0):
        number_of_stall_instructions+=1
        dummy_val-=4
        cache_list=[memory_cache_dict,no_of_blocks,no_of_sets,blocksize,cachesize,instruction_cache_dict,hit,miss,total_access]
        varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output,
            number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,number_of_stall_instructions,
            number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions,buffers,hit_miss_btb]
        return reg,instruction_dict,data_dict,clock,varlist,cache_list
    if len(decode_pc)!=0:
        this_pc=decode_pc[0]
        this_pc="0x"+(10-len(this_pc))*'0'+this_pc[2:]
        instruction_register=instruction_register,hit,miss=fetch.retrievingmachinecode(this_pc,instruction_dict,instruction_cache_dict,blocksize,no_of_sets,clock,hit,miss)
        output+="Fetch Instruction "+str(instruction_register)+" from address "+str(this_pc)+"\n"
        if(this_pc!='0x00000000' and this_pc!='0x00000004'):
            flowchart_list.append(this_pc)
        decode_pc.pop(0)
        if remove_decode==False:
            execute_pc.append(this_pc)
            if fetch.increment_pc(this_pc) in instruction_dict:
                decode_pc.append(fetch.increment_pc(this_pc))
            remove_decode=False
        else:
            output+="pc "+str(this_pc)+" is flushed because of prediction mismatched\n"
            flowchart_list[len(flowchart_list)-1]=-1
            remove_decode=False
            cache_list=[memory_cache_dict,no_of_blocks,no_of_sets,blocksize,cachesize,instruction_cache_dict,hit,miss,total_access]
            varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output,
                number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,number_of_stall_instructions,
                number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions,buffers,hit_miss_btb]
            return reg,instruction_dict,data_dict,clock,varlist,cache_list
        remove_decode=False
        pc_temp=fetch.increment_pc(this_pc)

        decoded_info[this_pc]=decode.decode(instruction_register)
        if this_pc not in buffers:
            buffers[this_pc]={}
            buffers[this_pc]['dec']=decoded_info[this_pc]
        else:
            buffers[this_pc]['dec']=decoded_info[this_pc]
        
        if('rs1' in decoded_info[this_pc] and buffer_val_for_rd[int(decoded_info[this_pc]['rs1'],2)]!=-1):
            dummy_val=8-(new_var-buffer_val_for_rd[int(decoded_info[this_pc]['rs1'],2)])

        if('rs2' in decoded_info[this_pc] and buffer_val_for_rd[int(decoded_info[this_pc]['rs2'],2)]!=-1):
            if((8-(new_var-buffer_val_for_rd[int(decoded_info[this_pc]['rs2'],2)]))>dummy_val):
                dummy_val=8-(new_var-buffer_val_for_rd[int(decoded_info[this_pc]['rs2'],2)])

        if('rd' in decoded_info[this_pc]):
            buffer_val_for_rd[int(decoded_info[this_pc]['rd'],2)]=new_var
        if(dummy_val<0):
            dummy_val=0
        #if stalling I am again adding the decode instruction in decode queue

        if(dummy_val!=0):
            number_of_datahazards+=1
            number_of_stall_instructions+=1
            execute_pc.pop()
            if fetch.increment_pc(this_pc) in instruction_dict:
                decode_pc.pop()
            decode_pc.append(this_pc)

        if(dummy_val==0):
            opr=decoded_info[this_pc]['opr']
            if(len(fetch_pc)!=0):
                fetch_pc.pop(0)
            if(hex(int(this_pc,16)+8) in instruction_dict):
                fetch_pc.append(this_pc)
            if(opr=='jal' or opr=='jalr' or opr=='beq' or opr=='bne' or opr=='bge' or opr=='blt'):
                number_of_control_instructions+=1
                control_inst=True
                
                if len(decode_pc)!=0:
                    decode_pc.pop()

                if this_pc in btb:
                    if btb[this_pc] in instruction_dict:
                        decode_pc.append(btb[this_pc])
                else:
                    if fetch.increment_pc(this_pc) in instruction_dict:
                        decode_pc.append(fetch.increment_pc(this_pc))
                    
    
    varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output,
            number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,number_of_stall_instructions,
            number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions,buffers,hit_miss_btb]
    cache_list=[memory_cache_dict,no_of_blocks,no_of_sets,blocksize,cachesize,instruction_cache_dict,hit,miss,total_access]
    return reg,instruction_dict,data_dict,clock,varlist,cache_list