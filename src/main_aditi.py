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
clock=1
pc=fetch.increment_pc(pc)
decoded_info={}
rz=hex(0)
rm=hex(0)
muxy=hex(0)
btb={}
predicted={}
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
decode_pc.append("0x0")
#print("ffffff",buffer_val_for_rd)
control_inst=False
remove_decode=False
dummy_val=0
buffer_memory={}
new_var=0
while(1):
    new_var+=4
    if len(write_pc)==0 and len(mem_pc)==0 and len(execute_pc)==0 and len(decode_pc)==0:
        break
    clock+=1

    #write_back
    if len(write_pc)!=0:
        this_pc=write_pc[0]
        write_pc.pop(0)

        if('rd' in decoded_info[this_pc]):
            if(int(decoded_info[this_pc]['rd'],2)!=0):
                reg,temp_string_writeback=Writeback.write_back(muxy,[decoded_info[this_pc]['type'],decoded_info[this_pc]['opr'],decoded_info[this_pc]['rd']],reg)

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


    #execute
    if len(execute_pc)!=0:
        this_pc=execute_pc[0]

        execute_pc.pop(0)
        mem_pc.append(this_pc)

        pc_temp=fetch.increment_pc(this_pc)
        rz,pc_final,temp_string_execute=execute.execute(decoded_info[this_pc],reg,pc_temp)
        rz=hex(rz)

        if control_inst:
            control_inst=False
            if this_pc in btb:
                if pc_final==btb[this_pc]:
                    pass
                else:
                    remove_decode=True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if len(decode_pc)==1:
                            if decode_pc[0]==pc_final:
                                remove_decode=False
            else:
                btb[this_pc]=pc_final
                if pc_final==fetch.increment_pc(this_pc):
                    pass
                else:
                    remove_decode=True
                    if pc_final in instruction_dict:
                        decode_pc.append(pc_final)
                        if decode_pc[0]==pc_final:
                            remove_decode=False

    #decode 
    if(dummy_val>0):
        dummy_val-=4
        continue
    if len(decode_pc)!=0:
        this_pc=decode_pc[0]
        decode_pc.pop(0)

        if remove_decode==False:
            execute_pc.append(this_pc)
            if fetch.increment_pc(this_pc) in instruction_dict:
                decode_pc.append(fetch.increment_pc(this_pc))
            remove_decode=False
        else:
            remove_decode=False
            continue
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
            execute_pc.pop()
            if fetch.increment_pc(this_pc) in instruction_dict:
                decode_pc.pop()
            decode_pc.append(this_pc)

        if(dummy_val==0):
            opr=decoded_info[this_pc]['opr']

            if(opr=='jal' or opr=='jalr' or opr=='beq' or opr=='bne' or opr=='bge' or opr=='blt'):
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