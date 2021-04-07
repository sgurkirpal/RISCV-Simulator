def to_hex(n): # gives string output
    num=hex(n)
    return num


def twos(string):
    x=string
    l=len(x)
    for i in range(32-len(x)):
        x='1'+x
    y=int(x,2)
    y=~y
    z=y+4294967297    
    z=bin(z)
    z='-'+z
    return z

    
def decode(instrc):
    x=int(instrc,16)    
    bin_x="{:032b}".format(x)       
    d={}
    opcode=bin_x[25:32]
    if(opcode=='0110011'):   # R-type instruction 
        d['type']="R"
        rd=bin_x[32-12:32-7]
        d['rd']=rd
        d['rs1']=bin_x[32-20:32-15]
        d['rs2']=bin_x[32-25:32-20]
        func3=bin_x[32-15:32-12]
        func7=bin_x[32-32:32-25]        
        if(func3=='000'and func7=='0000000'):
            d['opr']='add'
        elif(func3=='000' and func7=='0100000'):
            d['opr']='sub'
        elif(func3=='001'and func7=='0000000'):
            d['opr']='sll'
        elif(func3=='101'and func7=='0000000'):
            d['opr']='srl'
        elif(func3=='101'and func7=='0100000'):
            d['opr']='sra'
        elif(func3=='010'and func7=='0000000'):
            d['opr']='sra'
        elif(func3=='100'and func7=='0000000'):
            d['opr']='xor'
        elif(func3=='111'and func7=='0000000'):
            d['opr']='and'
        elif(func3=='110'and func7=='0000000'):
            d['opr']='or'
        elif(func3=='000'and func7=='0000001'):
            d['opr']='mul'
        elif(func3=='100'and func7=='0000001'):
            d['opr']='div'
            
    if(bin_x[25:32]=='0010011'):   # I type instruction 1st half
        d['type']="I"
        rd=bin_x[32-12:32-7]
        d['rd']=rd
        d['rs1']=bin_x[32-20:32-15]
        d['imm']=bin_x[32-32:32-20]
        func3=bin_x[32-15:32-12]
        if(bin_x[0]=='1'):                           # to check for sign extension
            d['imm']=twos(d['imm'])
            
        if(func3=='000'):
            d['opr']='addi'
        elif(func3=='111'):
            d['opr']='andi'
        elif(func3=='110'):
            d['opr']='ori'
    
    if(bin_x[25:32]=='0000011'):   # I type instruction 1st loads 
        d['type']="I"
        rd=bin_x[32-12:32-7]
        d['rd']=rd
        d['rs1']=bin_x[32-20:32-15]
        d['imm']=bin_x[32-32:32-20]
        func3=bin_x[32-15:32-12]
        if(bin_x[0]=='1'):                           # to check for sign extension
            d['imm']=twos(d['imm'])
        if(func3=='000'):
            d['opr']='lb'
        elif(func3=='001'):
            d['opr']='lh'
        elif(func3=='010'):
            d['opr']='lw'
        elif(func3=='011'):
            d['opr']='ld'
            
    if(bin_x[25:32]=='1100111'):   # I type instruction jalr
        d['type']="I"
        rd=bin_x[32-12:32-7]
        d['rd']=rd
        d['rs1']=bin_x[32-20:32-15]
        d['imm']=bin_x[32-32:32-20]
        func3=bin_x[32-15:32-12]
        if(bin_x[0]=='1'):                           # to check for sign extension
            d['imm']=twos(d['imm'])
        if(func3=='000'):
            d['opr']='jalr'
    
    if(bin_x[25:32]=='0100011'):   # s type instructions
        d['type']="S"       
       
        d['rs1']=bin_x[32-20:32-15]
        d['rs2']=bin_x[32-25:32-20]
        func3=bin_x[32-15:32-12]
        d['imm']=bin_x[32-32:32-25]+bin_x[32-12:32-7]
        if(d['imm'][0]=='1'):                           # to check for sign extension
            d['imm']=twos(d['imm'])
        if(func3=='000'):
            d['opr']='sb'
        elif(func3=='001'):
            d['opr']='sh'
        elif(func3=='010'):
            d['opr']='sw'
        elif(func3=='011'):
            d['opr']='sd'
            
    if(bin_x[25:32]=='1100011'):   # sb type instructions
        d['type']="SB"       
       
        d['rs1']=bin_x[32-20:32-15]
        d['rs2']=bin_x[32-25:32-20]
        func3=bin_x[32-15:32-12]
        d['imm']=bin_x[32-32]+bin_x[32-8]+bin_x[32-31:32-25]+bin_x[32-12:32-8]+'0'
        if(d['imm'][0]=='1'):                           # to check for sign extension
            d['imm']=twos(d['imm'])
        if(func3=='000'):
            d['opr']='beq'
        elif(func3=='001'):
            d['opr']='bne'
        elif(func3=='101'):
            d['opr']='bge'
        elif(func3=='100'):
            d['opr']='blt'
            
    if(bin_x[25:32]=='0010111'or bin_x[25:32]=='0110111'):   # U type instructions
        d['type']="U"       
       
        rd=bin_x[32-12:32-7]
        d['rd']=rd
        
        string=bin_x[32-32:32-12]
        for i in range(32-len(string)):
            string=string+'0'
        d['imm']=string
        if(d['imm'][0]=='1'):                           # to check for sign extension
            d['imm']=twos(d['imm'])
        if(opcode=='0010111'):
            d['opr']='auipc'
        else:
            d['opr']='lui'
    if(bin_x[25:32]=='1101111'):   # UJ type instructions
        d['type']="UJ"       
       
        rd=bin_x[32-12:32-7]
        d['rd']=rd
        
        string=bin_x[0]+bin_x[32-20:32-12]+bin_x[32-21]+bin_x[32-31:32-21]
        for i in range(32-len(string)):
            string=string+'0'
        d['imm']=string
        if(d['imm'][0]=='1'):                           # to check for sign extension
            d['imm']=twos(d['imm'])
       
        d['opr']='jal'
        
            
            
            
     
        
        
            
            
        
        
        
        
        
    return d
        
    
    
    
    
    
        
    
    
    
    
    