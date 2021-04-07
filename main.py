#main program file

import fetch
import decode
import execute

instruction_dict={}    #dictionary storing instructions
data_dict={}    #dictionary storing data in memory

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