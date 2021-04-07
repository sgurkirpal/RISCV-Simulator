#main program file

import fetch
import decode
import execute
import memory

instruction_dict={}    #dictionary storing instructions
data_dict={}    #dictionary storing data in memory

reg={} #registers
for i in range(32):
    reg[i]=0x00000000
    if i==2:
        reg[i]=0x7FFFFFF0
    if i==3:
        reg[i]=0x10000000


file=open("sample.mc","r")

instruction_dict,data_dict = fetch.fetch_file(file)

pc="0x0"    #initial pc is by default 0x0

instruction_register=None

for i in range(10):
    if pc not in instruction_dict:
        break
    instruction_register=instruction_dict[pc]

    decoded_info=decode.decode(instruction_register)
    print(decoded_info)
    #rz=execute.execute(decoded_info)
    
    pc=fetch.increment_pc(pc)