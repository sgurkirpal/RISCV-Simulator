
#we are assuming that after decode function we have some information
#like whether the instruction is r type s type....
#we also have the value of immediate rs1, rs2...whatever required

def rshift(val, n):  #logical right shift
    return val>>n if val >= 0 else (val+0x100000000)>>n


def R_type(l,pc_temp): #l[0] is operation
    if l[0]=='add':  
        return l[1]+l[2],pc_temp    #l[1] is rs1 and l[2] is rs[2]
    if(l[0]=='sub'):
        return l[1]-l[2],pc_temp
    if(l[0]=='or'):
        return l[1]|l[2],pc_temp
    if(l[0]=='and'):
        return l[1]&l[2],pc_temp
    if(l[0]=='sll'):
        return l[1]<<l[2],pc_temp
    if(l[0]=='slt'):
        if(l[1]<l[2]):
            return 1,pc_temp
        else:
            return 0,pc_temp
    if(l[0]=='sra'):
        return rshift(l[1],l[2]),pc_temp
    if(l[0]=='srl'):
        return l[1]>>l[2],pc_temp
    if(l[0]=='xor'):
        return l[1]^l[2],pc_temp
    if(l[0]=='rem'):
        return l[1]%l[2],pc_temp
    if(l[0]=='div'):
        return l[1]//l[2],pc_temp
    if(l[0]=='mul'):
        return l[1]*l[2],pc_temp


def S_type(l,pc_temp):  #l[1] is rs1 and l[2] is immmedirdiate
    return l[1]+l[2],pc_temp


def SB_type(l,pc_temp):
    if l[1]>=(1<<31):
        l[1]=(1<<31)-l[1]
    if l[2]>=(1<<31):
        l[2]=(1<<31)-l[2]
    if(l[0]=='beq'):
        if(l[1]==l[2]):
            #yahan kuch pc final type ki baat hori hai..we have to go in pc final 
            #we don't have to return the value of other things.
            return 1,hex(int(pc_temp,16)-4+l[3])
        else:
            return 0,pc_temp
    if(l[0]=='bne'):
        if(l[1]!=l[2]):
            return 1,hex(int(pc_temp,16)-4+l[3])
        else:
            return 0,pc_temp
    if(l[0]=='bge'):
        if(l[1]>=l[2]):
            return 1,hex(int(pc_temp,16)+l[3]-4)
        else:
            return 0,pc_temp
    if(l[0]=='blt'):
        if(l[1]<l[2]):
            return 1,hex(int(pc_temp,16)-4+l[3])
        else:
            return 0,pc_temp   

def I_type(l,pc_temp):  #l[0] is operation , l[1] is rs1 and l[2] is immediate
    if l[0]=='addi':
        return l[1]+l[2],pc_temp
    if l[0]=='ori':
        return l[1]|l[2],pc_temp
    if l[0]=='andi':
        return l[1]&l[2],pc_temp
    if l[0]=='lb' or l[0]=='lh' or l[0]=='ld' or l[0]=='lw':
        return l[1]+l[2],pc_temp
    if l[0]=='jalr':
        print(l[1]+l[2])
        return int(pc_temp,16),hex(l[1]+l[2])


def UJ_type(l,pc_temp):
    #we have to change the value of pc final to pc_immediate and also we have to store the value of next thing in register
    #we have to store the value of pc_temp also
    return int(pc_temp,16),hex(int(pc_temp,16)+l[1]-4)
    #we don't have to do anything in uj_type instruction in execution step

def U_type(l,pc_temp):
    #in case of auipc just add the value of pc temp in it
    if(l[0]=='auipc'):
        return int(pc_temp,16)+l[1]-4,pc_temp
    #in case of lui we don't have to do anything.
    return l[1],pc_temp



def execute(d,reg,pc_temp):
    #print("HEllo mam",d)
    #print(reg)
    if 'rs1' in d:
        rs1=int(reg[int(d['rs1'],2)],16)
    if 'rs2' in d:
        rs2=int(reg[int(d['rs2'],2)],16)
    if 'imm' in d:
        imm=int(d['imm'],2)
    if(d['type']=='R'):
        l=[d['opr'],rs1,rs2]
        return R_type(l,pc_temp)
    elif(d['type']=='S'):
        l=[d['opr'],rs1,imm]
        return S_type(l,pc_temp)
    elif d['type']=='I':
        l=[d['opr'],rs1,imm]
        return I_type(l,pc_temp)
    elif d['type']=='SB':
        l=[d['opr'],rs1,rs2,imm]
        return SB_type(l,pc_temp)
    elif d['type']=='U':
        l=[d['opr'],imm]
        return U_type(l,pc_temp)
    elif d['type']=='UJ':
        l=[d['opr'],imm]
        return UJ_type(l,pc_temp)
    else:
        print("Invalid Instruction type!")
        return 0,0






