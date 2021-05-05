# main program file
from math import ceil
import fetch
import decode
import execute
import memory
import Writeback

def assemble():
    instruction_dict = {}  # dictionary storing instructions
    data_dict = {}  # dictionary storing data in memory

    reg = {}  # registers
    write_df_reg = {}
    val_df_reg = {}
    clock=1
    reg[0] = '0x0'
    for i in range(32):
        reg[i] = '0x00000000'
        write_df_reg[i] = 0
        if i == 2:
            reg[i] = '0x7FFFFFF0'
        if i == 3:
            reg[i] = '0x10000000'


    file = open("data.mc", "r")

    instruction_dict, data_dict = fetch.fetch_file(file)

    pc = "0x0"  # initial pc is by default 0x0
    pc_temp = "0x0"
    pc = fetch.increment_pc(pc)
    decoded_info = {}
    rz = hex(0)
    rm = hex(0)
    muxy = hex(0)
    btb = {}
    mem_pc = []
    write_pc = []
    execute_pc = []
    decode_pc = []
    fetch_pc = []
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
    decode_pc.append("0x0")
    control_inst = False
    remove_decode = False
    flowchart_list=[]
    output=""
    buffers={}
    varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,control_inst,remove_decode,write_df_reg,val_df_reg,flowchart_list,output,
    number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,
    number_of_stall_instructions,number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions,buffers]
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
    control_inst=varlist[12]
    remove_decode=varlist[13]
    write_df_reg=varlist[14]
    val_df_reg=varlist[15]
    flowchart_list=varlist[16]
    output=varlist[17]
    number_of_instructions=varlist[18]
    number_of_load_instruction=varlist[19]
    number_of_store_instruction=varlist[20]
    number_of_control_instructions=varlist[21]
    number_of_stall_instructions=varlist[22]
    number_of_mispredictions=varlist[23]
    number_of_datahazards=varlist[24]
    number_of_contolhazards=varlist[25]
    number_of_stalls_datahazards=varlist[26]
    number_of_stalls_contolhazards=varlist[27]
    number_of_alu_instructions=varlist[28]
    buffers=varlist[29]
    output=""
    if pc==-1:
        output+="Number of clock cycles ="+str(clock)+"\n"+\
    "Total number of instructions executed = "+str(number_of_instructions)+"\n"+\
    "CPI value calculated = "+str(clock/number_of_instructions)+"\n"+\
    "Total number of load/store instructions = " + str(number_of_load_instruction+number_of_store_instruction)+"\n"+\
    "Number of ALU instructions = "+str(number_of_instructions-number_of_alu_instructions)+"\n"+\
    "Number of control instructions = "+str(number_of_control_instructions)+"\n"+\
    "Number of bubbles and stalls in the pipeline = "+str(clock-number_of_instructions)+"\n"+\
    "Number of data hazards = "+str(number_of_datahazards)+"\n"+\
    "Number of control hazards = "+str(number_of_mispredictions)+"\n"+\
    "Number of branch mispredictions = "+ str(number_of_mispredictions)+"\n"+\
    "Number of stalls due to data hazards = "+str(clock-number_of_instructions-number_of_mispredictions)+"\n"+\
    "Number of stalls due to control hazards = "+str(number_of_mispredictions)+"\n"
        return output
    if (len(write_pc) == 0 and len(mem_pc) == 0 and len(execute_pc) == 0 and len(decode_pc) == 0):
        varlist=[-1,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,control_inst,remove_decode,write_df_reg,val_df_reg,flowchart_list,output,
            number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,
            number_of_stall_instructions,number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions,buffers]
        return reg,instruction_dict,data_dict,clock,varlist
    clock += 1

    # write_back
    if len(write_pc) != 0:
        this_pc = write_pc[0]
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
            x = int(decoded_info[this_pc]['rd'], 2)
            write_df_reg[x] = write_df_reg[x]-1  # as now its use has ended
            if(x == 0):
                write_df_reg[x] = 0

            if(int(decoded_info[this_pc]['rd'], 2) != 0):
                reg, temp_string_writeback = Writeback.write_back(muxy, [decoded_info[this_pc]['type'], decoded_info[this_pc]['opr'], decoded_info[this_pc]['rd']], reg)
                output+=temp_string_writeback


    # memory
    if len(mem_pc) != 0:
        this_pc = mem_pc[0]

        mem_pc.pop(0)
        write_pc.append(this_pc)

        rm = None
        if 'rs2' in decoded_info[this_pc]:
            rm = reg[int(decoded_info[this_pc]['rs2'], 2)]
            rm = rm[2:]
            rm = "0"*(8-len(rm))+rm
        if(int(rz, 16) < 0):
            if(len(rz) != 11):
                rz = '-'+rz[1:3]+'0'*(11-len(rz))+rz[3:]
        else:
            if(len(rz) != 10):
                rz = rz[:2]+'0'*(10-len(rz))+rz[2:]

        opr = decoded_info[this_pc].get('opr', '-1')

        muxy, data_dict, temp_string_memory = memory.memory(
            0x0, rz, [decoded_info[this_pc]['type'], decoded_info[this_pc]['opr']], rm, data_dict, pc_temp)
        if this_pc not in buffers:
            buffers[this_pc]={}
            buffers[this_pc]['mem']=muxy
        else:
            buffers[this_pc]['exe']=muxy
        output+=temp_string_memory


    # execute
    if len(execute_pc) != 0:
        this_pc = execute_pc[0]
        for x in decoded_info[this_pc]:
            output+=str(x)+" is "+str(decoded_info[this_pc][x])+"\n"
        execute_pc.pop(0)
        mem_pc.append(this_pc)

        pc_temp = fetch.increment_pc(this_pc)
        #print('\n\n\n')
        #print(reg,val_df_reg)
        rz, pc_final, temp_string_execute = execute.execute(
            decoded_info[this_pc], reg, pc_temp,val_df_reg)
        output+=temp_string_execute
        rz = hex(rz)
        #print(this_pc,end=" ")
        #print(rz)
        buffer_exec = rz
        rd = decoded_info[this_pc].get('rd', '-1')
        if this_pc not in buffers:
            buffers[this_pc]={}
            buffers[this_pc]['exe']=rz
        else:
            buffers[this_pc]['exe']=rz
        if(rd != '-1'):
            x = int(rd, 2)
            val_df_reg[x] = rz
            if(x == 0):
                val_df_reg[x] = 0
            if(decoded_info[this_pc]['opr'] == 'lw'):
                val_df_reg[x] = data_dict[rz]
        #print(reg)
        #print(val_df_reg)
        if control_inst:
            control_inst = False
            if this_pc in btb:
                if pc_final == btb[this_pc]:
                    pass
                else:
                    number_of_mispredictions+=1

                    remove_decode = True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if decode_pc[0] == pc_final:
                            remove_decode = False
            else:
                btb[this_pc] = pc_final
                if pc_final == fetch.increment_pc(this_pc):
                    pass
                else:
                    number_of_mispredictions+=1
                    remove_decode = True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if decode_pc[0] == pc_final:
                            remove_decode = False

    # decode
    if len(decode_pc) != 0:
        this_pc = decode_pc[0]
        output+="Fetch Instruction "+instruction_dict[this_pc]+" from address "+this_pc+"\n"
        flowchart_list.append(this_pc)
        decode_pc.pop(0)
        flg = 0
        if remove_decode == False:
            execute_pc.append(this_pc)
            flg = 1
            if fetch.increment_pc(this_pc) in instruction_dict:
                decode_pc.append(fetch.increment_pc(this_pc))
        else:
            flowchart_list[len(flowchart_list)-1]=-1
        remove_decode = False
        instruction_register = instruction_dict[this_pc]

        pc_temp = fetch.increment_pc(this_pc)
        decoded_info[this_pc] = decode.decode(instruction_register)
        if this_pc not in buffers:
            buffers[this_pc]={}
            buffers[this_pc]['dec']=decoded_info[this_pc]
        else:
            buffers[this_pc]['dec']=decoded_info[this_pc]

        rd = decoded_info[this_pc].get('rd', '-1')
        rs1 = decoded_info[this_pc].get('rs1', '-1')
        rs2 = decoded_info[this_pc].get('rs2', '-1')
        if(rs1 != '-1' and flg == 1):
            x = int(rs1, 2)
            if(write_df_reg[x] == 1):  # that means data forwarding is required
                number_of_datahazards+=1
                reg[x] = val_df_reg[x]  # i add the value stored in the buffer
        if(rs2 != '-1' and flg == 1):
            x = int(rs2, 2)
            if(write_df_reg[x] == 1):  # that means data forwarding is required
                number_of_datahazards+=1
                reg[x] = val_df_reg[x]  # i add the value stored in the buffer

        if(rd != '-1' and flg == 1):
            x = int(rd, 2)
            if(x != 0):
                write_df_reg[x] = write_df_reg[x]+1
            else:
                write_df_reg[x] = 0

        # print(write_df_reg)
        opr = decoded_info[this_pc]['opr']
        if(opr == 'jal' or opr == 'jalr' or opr == 'beq' or opr == 'bne' or opr == 'bge' or opr == 'blt'):
            number_of_control_instructions+=1
            control_inst = True
            if len(decode_pc) != 0:
                decode_pc.pop()
            if this_pc in btb:
                if btb[this_pc] in instruction_dict:
                    decode_pc.append(btb[this_pc])
            else:
                if fetch.increment_pc(this_pc) in instruction_dict:
                    decode_pc.append(fetch.increment_pc(this_pc))

    # print(remove_decode)

    varlist=[pc,pc_temp,decoded_info,rz,rm,muxy,btb,mem_pc,write_pc,execute_pc,decode_pc,fetch_pc,control_inst,remove_decode,write_df_reg,val_df_reg,flowchart_list,output,
        number_of_instructions,number_of_load_instruction,number_of_store_instruction,number_of_control_instructions,
        number_of_stall_instructions,number_of_mispredictions,number_of_datahazards,number_of_contolhazards,number_of_stalls_datahazards,number_of_stalls_contolhazards,number_of_alu_instructions,buffers]    
    return reg,instruction_dict,data_dict,clock,varlist