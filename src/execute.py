
#we are assuming that after decode function we have some information
#like whether the instruction is r type s type....
#we also have the value of immediate rs1, rs2...whatever required

def rshift(val, n):  #logical right shift
    return val>>n if val >= 0 else (val+0x100000000)>>n


def R_type(l,pc_temp,output): #l[0] is operation
    if l[0]=='add':  
        output+="EXECUTE: Adding "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]+l[2],pc_temp,output    #l[1] is rs1 and l[2] is rs[2]
    if(l[0]=='sub'):
        output+="EXECUTE: Subtracting "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]-l[2],pc_temp,output
    if(l[0]=='or'):
        output+="EXECUTE: Bitwise OR of "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]|l[2],pc_temp,output
    if(l[0]=='and'):
        output+="EXECUTE: Bitwise AND of "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]&l[2],pc_temp,output
    if(l[0]=='sll'):
        output+="EXECUTE: Shift left of "+str(l[1])+" by "+str(l[2])+"\n"
        return l[1]<<l[2],pc_temp,output
    if(l[0]=='slt'):
        output+="EXECUTE: Set if "+str(l[1])+" is less than "+str(l[2])+"\n"
        if(l[1]<l[2]):
            return 1,pc_temp,output
        else:
            return 0,pc_temp,output
    if(l[0]=='sra'):
        output+="EXECUTE: Shift Right arithmatic of "+str(l[1])+" by "+str(l[2])+"\n"
        return rshift(l[1],l[2]),pc_temp,output
    if(l[0]=='srl'):
        output+="EXECUTE: Shift Right logical of "+str(l[1])+" by "+str(l[2])+"\n"
        return l[1]>>l[2],pc_temp,output
    if(l[0]=='xor'):
        output+="EXECUTE: XOR of "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]^l[2],pc_temp,output
    if(l[0]=='rem'):
        output+="EXECUTE: Remainder on dividing "+str(l[1])+" by "+str(l[2])+"\n"
        return l[1]%l[2],pc_temp,output
    if(l[0]=='div'):
        output+="EXECUTE: Division of "+str(l[1])+" by "+str(l[2])+"\n"
        return l[1]//l[2],pc_temp,output
    if(l[0]=='mul'):
        output+="EXECUTE: Multiplication of "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]*l[2],pc_temp,output


def S_type(l,pc_temp,output):  #l[1] is rs1 and l[2] is immmedirdiate
    output+="EXECUTE: Calculating net memory address by adding "+str(l[1])+" and "+str(l[2])+" in S-type instructions\n"
    return l[1]+l[2],pc_temp,output


def SB_type(l,pc_temp,output):
    if l[1]>=(1<<31):
        l[1]=(1<<31)-l[1]
    if l[2]>=(1<<31):
        l[2]=(1<<31)-l[2]
    if(l[0]=='beq'):
        if(l[1]==l[2]):
            output+="EXECUTE: "+str(l[1])+" and "+str(l[2])+" are equal, hence, pc incremented. \n"
            #yahan kuch pc final type ki baat hori hai..we have to go in pc final 
            #we don't have to return the value of other things.
            ha=hex(int(pc_temp,16)-4+l[3])
            ha=str(ha)
            ha="0x"+(10-len(ha))*'0'+ha[2:]
            return 1,ha,output
        else:
            output+="EXECUTE: "+str(l[1])+" and "+str(l[2])+" are not equal, hence, pc not updated. \n"
            return 0,pc_temp,output
    if(l[0]=='bne'):
        if(l[1]!=l[2]):
            output+="EXECUTE: "+str(l[1])+" and "+str(l[2])+" are not equal, hence, pc incremented. \n"
            ha=hex(int(pc_temp,16)-4+l[3])
            ha=str(ha)
            ha="0x"+(10-len(ha))*'0'+ha[2:]
            return 1,ha,output
        else:
            output+="EXECUTE: "+str(l[1])+" and "+str(l[2])+" are equal, hence, pc not updated. \n"
            return 0,pc_temp,output
    if(l[0]=='bge'):
        if(l[1]>=l[2]):
            output+="EXECUTE: "+str(l[1])+" is greater than "+str(l[2])+" hence, pc incremented. \n"
            ha=hex(int(pc_temp,16)+l[3]-4)
            ha=str(ha)
            ha="0x"+(10-len(ha))*'0'+ha[2:]
            return 1,ha,output
        else:
            output+="EXECUTE: "+str(l[1])+" is not greater than "+str(l[2])+" hence, pc not updated. \n"
            return 0,pc_temp,output
    if(l[0]=='blt'):
        if(l[1]<l[2]):
            output+="EXECUTE: "+str(l[1])+" is less than "+str(l[2])+" hence, pc incremented. \n"
            hex(int(pc_temp,16)-4+l[3])
            ha=str(ha)
            ha="0x"+(10-len(ha))*'0'+ha[2:]
            return 1,ha,output
        else:
            output+="EXECUTE: "+str(l[1])+" is not less than "+str(l[2])+" hence, pc not updated. \n"
            return 0,pc_temp,output   

def I_type(l,pc_temp,output):  #l[0] is operation , l[1] is rs1 and l[2] is immediate
    if l[0]=='addi':
        output+="EXECUTE: Adding "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]+l[2],pc_temp,output
    if l[0]=='ori':
        output+="EXECUTE: OR of "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]|l[2],pc_temp,output
    if l[0]=='andi':
        output+="EXECUTE: AND of "+str(l[1])+" and "+str(l[2])+"\n"
        return l[1]&l[2],pc_temp,output
    if l[0]=='lb' or l[0]=='lh' or l[0]=='ld' or l[0]=='lw':
        output+="EXECUTE: Calculating net memory address by adding "+str(l[1])+" and "+str(l[2])+" in Load instructions\n"
        return l[1]+l[2],pc_temp,output
    if l[0]=='jalr':
        output+="EXECUTE: Calculating net memory address by adding "+str(l[1])+" and "+str(l[2])+" in jalr instruction\n"
        ha=hex(l[1]+l[2])
        ha=str(ha)
        ha="0x"+(10-len(ha))*'0'+ha[2:]
        return int(pc_temp,16),ha,output


def UJ_type(l,pc_temp,output):
    #we have to change the value of pc final to pc_immediate and also we have to store the value of next thing in register
    #we have to store the value of pc_temp also
    output+="EXECUTE: Calculating net memory address by adding "+str(l[1])+" in jal instruction\n"
    ha=hex(int(pc_temp,16)+l[1]-4)
    ha=str(ha)
    ha="0x"+(10-len(ha))*'0'+ha[2:]
    return int(pc_temp,16),ha,output
    #we don't have to do anything in uj_type instruction in execution step

def U_type(l,pc_temp,output):
    #in case of auipc just add the value of pc temp in it
    if(l[0]=='auipc'):
        output+="EXECUTE: PC added to "+str(l[1])+"\n"
        return int(pc_temp,16)+l[1]-4,pc_temp,output
    #in case of lui we don't have to do anything.
    output+="EXECUTE: No execute operation"
    return l[1],pc_temp,output



def execute(d,reg,pc_temp,val_df_reg=None):
    output=""
    if 'rs1' in d:
        rs1=int(reg[int(d['rs1'],2)],16)
    if 'rs2' in d:
        rs2=int(reg[int(d['rs2'],2)],16)
    if 'imm' in d:
        imm=int(d['imm'],2)
    if val_df_reg is not None:
        #print("haha")
        if 'rs1' in d:
            if int(d['rs1'],2) in val_df_reg:
                #print("yoyo")
                #print(val_df_reg[int(d['rs1'],2)])
                if(val_df_reg[int(d['rs1'],2)]==0):
                    pass
                else:
                    rs1=int(val_df_reg[int(d['rs1'],2)],16)
        if 'rs2' in d and 'rs2' in val_df_reg:
            if int(d['rs2'],2) in val_df_reg:
                #print("nono")
                #print(val_df_reg[int(d['rs2'],2)])
                if(val_df_reg[int(d['rs2'],2)]==0):
                    pass
                else:
                    rs1=int(val_df_reg[int(d['rs2'],2)],16)
    if(d['type']=='R'):
        l=[d['opr'],rs1,rs2]
        return R_type(l,pc_temp,output)
    elif(d['type']=='S'):
        l=[d['opr'],rs1,imm]
        return S_type(l,pc_temp,output)
    elif d['type']=='I':
        l=[d['opr'],rs1,imm]
        return I_type(l,pc_temp,output)
    elif d['type']=='SB':
        l=[d['opr'],rs1,rs2,imm]
        return SB_type(l,pc_temp,output)
    elif d['type']=='U':
        l=[d['opr'],imm]
        return U_type(l,pc_temp,output)
    elif d['type']=='UJ':
        l=[d['opr'],imm]
        return UJ_type(l,pc_temp,output)
    else:
        print("Invalid Instruction type!")
        return 0,0,""






