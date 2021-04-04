
#we are assuming that after decode function we have some information
#like whether the instruction is r type s type....
#we also have the value of immediate rs1, rs2...whatever required

reg={} #registers
for i in range(32):
    reg[i]=0x00000000
    if i==2:
        reg[i]=0x7FFFFFF0
    if i==3:
        reg[i]=0x10000000


def rshift(val, n):  #logical right shift
    return val>>n if val >= 0 else (val+0x100000000)>>n


def R_type(l):
    if l[0]=='add':
        return l[1]+l[2]
    if(l[0]=='sub'):
        return l[1]-l[2]
    if(l[0]=='or'):
        return l[1]|l[2]
    if(l[0]=='and'):
        return l[1]&l[2]
    if(l[0]=='sll'):
        return l[1]<<l[2]
    if(l[0]=='slt'):
        return (l[1]<l[2])?1:0
    if(l[0]=='sra'):
        return rshift(l[1],l[2])
    if(l[0]=='srl'):
        return l[1]>>l[2]
    if(l[0]=='xor'):
        return l[1]^l[2]
    if(l[0]=='rem'):
        return l[1]%l[2]
    if(l[0]=='div'):
        return l[1]//l[2]
    if(l[0]=='mul'):
        return l[1]*l[2]


def S_type(l):
    return l[1]+l[2]


def SB_type(l):
    if(l[0]=='beq'):
        if(l[1]==l[2]):
            return 1
        else:
            return 0
    if(l[0]=='bne'):
        if(l[1]!=l[2]):
            return 1
        else:
            return 0
    if(l[0]=='bge'):
        if(l[1]>=l[2]):
            return 1
        else:
            return 0
    if(l[0]=='blt'):
        if(l[1]<l[2]):
            return 1
        else:
            return 0    

def I_type(l):
    if l[0]=='addi':
        return l[1]+l[2]
    if l[0]=='ori':
        return l[1]|l[2]
    if l[0]=='andi':
        return l[1]&l[2]
    if l[0]=='lb' or 'lh' or 'ld' or 'lw':
        return l[1]+l[2]
    if l[0]=='jalr':
        return l[1]+l[2]


def UJ_type(l):
    #we don't have to do anything in uj_type instruction in execution step

def U_type(l):
    return l[1]<<12



def execute(l):
    if(l[0]=='R'):
        return R_type(l[1:])
    elif(l[0]=='S'):
        return S_type(l[1:])
    elif l[0]=='I':
        return I_type(l[1:])
    elif l[0]=='SB':
        return SB_type(l[1:])
    elif l[0]=='U':
        return U_type(l[1:])
    elif l[0]=='UJ':
        return UJ_type(l[1:])
    else:
        print("Invalid Instruction type!")






