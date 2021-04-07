#main program file

import fetch
import decode
import execute
import memory

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
#print(data_dict)
pc="0x0"    #initial pc is by default 0x0

instruction_register=None

for i in range(10):
    if pc not in instruction_dict:
        break
    instruction_register=instruction_dict[pc]

    decoded_info=decode.decode(instruction_register)

    rm=None

    if 'rs2' in decoded_info:
        rm=reg[int(decoded_info['rs2'],2)]
        rm=rm[2:]
        for i in range(8-len(rm)):
            rm="0"+rm

    #print(decoded_info)
    #print(hex(int(decoded_info['imm'],2)))
    rz=execute.execute(decoded_info,reg)
    rz=hex(rz)
    #print(rz)
    ry=memory.memory(0x0,rz,[0,decoded_info['opr']],rm,data_dict,fetch.increment_pc(pc))
    #print(ry)
    if 'rd' in decoded_info:
        reg[int(decoded_info['rd'],2)]=ry
    pc=fetch.increment_pc(pc)
    #print(reg)

#print(reg)
#print(data_dict)