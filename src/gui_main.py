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
    #print(instruction_dict)
    #print(data_dict)
    #print(data_dict)
    pc="0x0"    #initial pc is by default 0x0
    pc_temp="0x0"
    pc_final="0x0"
    instruction_register=None
    return instruction_register,pc,reg,instruction_dict,data_dict,clock,pc_final,pc_temp
def runstep(instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock):
    output=""
    if pc not in instruction_dict:
        pc=-1
        return instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,output
    clock+=1
    instruction_register=instruction_dict[pc]
    pc_temp=fetch.increment_pc(pc)
    decoded_info=decode.decode(instruction_register)
    print(decoded_info)
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
    rz,pc_final=execute.execute(decoded_info,reg,pc_temp)
    
    #print(rz)
    rz=hex(rz)
    if(int(rz,16)<0):
        if(len(rz)!=11):
            rz='-'+rz[1:3]+'0'*(11-len(rz))+rz[3:]
    else:
        if(len(rz)!=10):
            rz=rz[:2]+'0'*(10-len(rz))+rz[2:]
    print(int(rz,16))
    print(rz,pc_final)
    #print(rz)
    
    muxy,data_dict=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
    #print(ry)
    if('rd' in decoded_info):
        if(int(decoded_info['rd'],2)!=0):
            reg=Writeback.write_back(muxy,[decoded_info['type'],decoded_info['opr'],decoded_info['rd']],reg)
    pc=pc_final
    #print(reg,data_dict)
    return instruction_dict,pc,pc_final,pc_temp,reg,data_dict,instruction_register,clock,output
print("Done")
