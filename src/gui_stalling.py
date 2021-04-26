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
    flowchart_list=[]
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
    varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output,
        number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,number_of_stall_instructions,
        number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions]
    return reg,instruction_dict,data_dict,clock,varlist
def runstep(reg,instruction_dict,data_dict,clock,varlist):
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
    new_var+=4
    if len(write_pc)==0 and len(mem_pc)==0 and len(execute_pc)==0 and len(decode_pc)==0:
        varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output,
                number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,number_of_stall_instructions,
                number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions]    
        return reg,instruction_dict,data_dict,clock,varlist
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

        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr']],rm,data_dict,pc_temp)
        output+=temp_string_memory


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

        if control_inst:
            control_inst=False
            if this_pc in btb:
                if pc_final==btb[this_pc]:
                    output+="Prediction Successful ! for pc, "+this_pc+"\n"
                    pass
                else:
                    output+="Prediction MisMatched ! for pc, "+this_pc+"\n"
                    remove_decode=True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if len(decode_pc)==1:
                            if decode_pc[0]==pc_final:
                                remove_decode=False
            else:
                btb[this_pc]=pc_final
                if pc_final==fetch.increment_pc(this_pc):
                    output+="Prediction Successful ! for pc, "+this_pc+"\n"
                    pass
                else:
                    output+="Prediction MisMatched ! for pc, "+this_pc+"\n"
                    remove_decode=True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if decode_pc[0]==pc_final:
                            remove_decode=False

    #decode 
    if(dummy_val>0):
        number_of_stall_instructions+=1
        dummy_val-=4
        varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output,
            number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,number_of_stall_instructions,
            number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions]
        return reg,instruction_dict,data_dict,clock,varlist
    if len(decode_pc)!=0:
        this_pc=decode_pc[0]
        output+="Fetch Instruction "+instruction_dict[this_pc]+" from address "+this_pc+"\n"
        flowchart_list.append(this_pc)
        decode_pc.pop(0)
        if remove_decode==False:
            execute_pc.append(this_pc)
            if fetch.increment_pc(this_pc) in instruction_dict:
                decode_pc.append(fetch.increment_pc(this_pc))
            remove_decode=False
        else:
            output+="pc "+this_pc+" is flushed because of prediction mismatched\n"
            flowchart_list[len(flowchart_list)-1]=-1
            remove_decode=False
            varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output]
            return reg,instruction_dict,data_dict,clock,varlist
        remove_decode=False
        pc_temp=fetch.increment_pc(this_pc)

        decoded_info[this_pc]=decode.decode(instruction_dict[this_pc])
        
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
                    
    print(data_dict)
    print(reg)
    print(clock)
    varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,buffer_var,buffer_val_for_rd,control_inst,remove_decode,dummy_val,buffer_memory,new_var,flowchart_list,output]
    
    return reg,instruction_dict,data_dict,clock,varlist