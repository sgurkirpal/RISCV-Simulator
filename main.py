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


file=open("sample.mc","r")

instruction_dict,data_dict = fetch.fetch_file(file)
#print(instruction_dict)
#print(data_dict)
#print(data_dict)
pc="0x0"    #initial pc is by default 0x0
pc_temp="0x0"
pc_final="0x0"

instruction_register=None
print(data_dict)
cnt=0
while(1):
    cnt+=1
    if pc not in instruction_dict:
        break
    print("pc",pc)
    instruction_register=instruction_dict[pc]
    pc_temp=fetch.increment_pc(pc)
    decoded_info=decode.decode(instruction_register)
    print(decoded_info)
    rm=None
    
    if 'rs2' in decoded_info:
        rm=reg[int(decoded_info['rs2'],2)]
        rm=rm[2:]
        rm="0"*(8-len(rm))+rm
    #print(rm)
    #print(hex(int(decoded_info['imm'],2)))
    rz,pc_final=execute.execute(decoded_info,reg,pc_temp)
    
    #print(rz)
    rz=hex(rz)
    print(rz,pc_final)
    if(len(rz)!=10):
        rz=rz[:2]+'0'*(10-len(rz))+rz[2:]
    #print(rz)
    
    muxy,data_dict=memory.memory(0x0,rz,[decoded_info['type'],decoded_info['opr']],rm,data_dict,pc_temp)
    #print(ry)
    if('rd' in decoded_info):
        if(int(decoded_info['rd'],2)!=0):
            reg=Writeback.write_back(muxy,[decoded_info['type'],decoded_info['opr'],decoded_info['rd']],reg)
    pc=pc_final
    #print(reg,data_dict)
    print(reg,data_dict)
    print("================================================================================================")
print("Done")
print(reg)
print(data_dict)
print(")))))))))",cnt)