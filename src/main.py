#main program file

import fetch
import decode
import execute
import memory
import Writeback

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
pc_final=-1

instruction_register=None
clock=0
pc=fetch.increment_pc(pc)
decoded_info={}
rz=hex(0)
rm=hex(0)
muxy=hex(0)
btb={}
predicted={}
buffer_for_rd={}

while(1):
    if pc not in instruction_dict and fetch.decrement_pc(pc,16) not in instruction_dict:
        break
    clock+=1

    #write_back
    if fetch.decrement_pc(pc, 16) in instruction_dict:
        this_pc=fetch.decrement_pc(pc, 16)
        print("write",this_pc)
        if('rd' in decoded_info[this_pc]):
            if(int(decoded_info[this_pc]['rd'],2)!=0):
                reg,temp_string_writeback=Writeback.write_back(muxy,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr'],decoded_info[this_pc]['rd']],reg)

    #memory
    if fetch.decrement_pc(pc,12) in instruction_dict:
        this_pc=fetch.decrement_pc(pc,12)
        print("mem",this_pc)
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
        print(rz)
        muxy,data_dict,temp_string_memory=memory.memory(0x0,rz,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr']],rm,data_dict,pc_temp)


    #execute
    if fetch.decrement_pc(pc,8) in instruction_dict:
        this_pc=fetch.decrement_pc(pc,8)
        print("execute",this_pc)
        pc_temp=fetch.increment_pc(this_pc)
        print("nonoo")
        rz,pc_final,temp_string_execute=execute.execute(decoded_info[this_pc],reg,pc_temp)
        rz=hex(rz)
    

    #decode
    if fetch.decrement_pc(pc,4) in instruction_dict:
        this_pc=fetch.decrement_pc(pc,4)
        print("decode",this_pc)
        instruction_register=instruction_dict[this_pc]
        pc_temp=fetch.increment_pc(this_pc)
        decoded_info[this_pc]=decode.decode(instruction_register)
        opr=decoded_info[this_pc]['opr']
        if(opr=='jal' or opr=='jalr' or opr=='beq' or opr=='bne' or opr=='bge' or opr=='blt'):
            if(decoded_info[this_pc]['imm']>0):
                predicted[this_pc]=fetch.increment_pc(pc)
            else:
                if(opr=='jal'):
                    predicted[this_pc]=this_pc+decoded_info[this_pc]['imm']
                elif(opr=='jalr'):
                    predicted[this_pc]=decoded_info[this_pc]['rs1']+decoded_info[this_pc]['imm']
                else:
                    predicted[this_pc]=this_pc+decoded_info[this_pc]['imm']

    pc=fetch.increment_pc(pc)

print(data_dict)
print(reg)