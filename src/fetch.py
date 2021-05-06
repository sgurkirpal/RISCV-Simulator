#Returns two dictionaries one with the text and other with data part
import memory

def increment_pc(pc):   #takes a hex string as input and returns a hex string with 0x4 added in it
    pc_int=int(pc,16)
    new_pc=pc_int + 0x4
    new_pc=hex(new_pc)
    new_pc=str(new_pc)
    new_pc="0x"+(10-len(new_pc))*'0'+new_pc[2:]
    return str(new_pc)

def decrement_pc(pc,index):
    pc_int=int(pc,16)
    new_pc=pc_int - index
    new_pc=hex(new_pc)
    new_pc=str(new_pc)
    new_pc="0x"+(10-len(new_pc))*'0'+new_pc[2:]
    return str(new_pc)

def fetch_file(mc_file):
    dict_text={}
    dict_data={}
    flag=0 # 0 while we add pc and 1 while adding memory
    for line in mc_file:
        words=line.split()
        if(len(words)==0):
            break
        if(words[0]=='0xffffc'):   # delimilter --> 0xffffc
            flag=1
            continue
        if flag==0:
            for i in range(4):
                pc_val=words[0]
                pc_val=int(pc_val,16)
                pc_val=hex(pc_val+i)
                pc_val='0x'+'0'*(10-len(pc_val))+pc_val[2:]
                dict_text[pc_val]="0x"+words[1][2*i+2:2*i+4]    
        else:
            if(len(words[1])==3):
                words[1]=words[1][:2]+'0'+words[1][2:]
            dict_data[words[0]]=words[1]
        
    return dict_text,dict_data

def cacheinitialization(input_list):
    #print("Enter the value for cachesize(in Bytes only)")
    cachesize=input_list[0]
    #print("Enter the value for blocksize(in Bytes only)")
    blocksize=input_list[1]
    #print("Enter number of ways for SA")
    k=input_list[2]
    memorycachedict={}
    no_of_blocks=(cachesize//blocksize)
    no_of_sets=no_of_blocks//k
    
    #memorycachedict is a dictionary which contains k elements
    # where each element is a separate list
    # syntax of list is such that l[0]=1 means it is filled
    # l[1]=tag bit
    # l[2]= cycle no. in which that tag value is changed
    # l[3:3+blocksize]=contains all the data bytes

    for i in range(no_of_sets):
        memorycachedict[i]=[]
        for j in range(k):
            memorycachedict[i].append([])
            memorycachedict[i][j].append(0)
            memorycachedict[i][j].append(-1)
            memorycachedict[i][j].append(-1)
            for _ in range(blocksize):
                memorycachedict[i][j].append(-1)
    return no_of_blocks,no_of_sets,memorycachedict,k,blocksize,cachesize


#instruction cache dict is exactly same as memory cache dict
def instruction_initialization(input_list):
    cachesize=input_list[3]
    #print("Enter the value for blocksize(in Bytes only)")
    blocksize=input_list[4]
    #print("Enter number of ways for SA")
    k=input_list[5]
    no_of_blocks=(cachesize//blocksize)
    no_of_sets=no_of_blocks//k
    InstructionCacheDict={}
    for i in range(no_of_sets):
        InstructionCacheDict[i]=[]
        for j in range(k):
            InstructionCacheDict[i].append([])
            InstructionCacheDict[i][j].append(0)
            InstructionCacheDict[i][j].append(-1)
            InstructionCacheDict[i][j].append(-1)
            for _ in range(blocksize):
                InstructionCacheDict[i][j].append(-1)
    return InstructionCacheDict,no_of_blocks,no_of_sets,k,blocksize,cachesize

def retrievingmachinecode(pc_val,instruction_dict,instruction_cache_dict,block_size,no_of_sets,clockcycle,hit,miss,output):
    machine_code='0x'
    pc_can=pc_val
    for i in range(4):
        pc_val=pc_can
        pc_val=int(pc_val,16)
        pc_val=hex(pc_val+i)
        pc_val='0x'+'0'*(10-len(pc_val))+pc_val[2:] 
        output+="INSTRUCTION_"       
        a,instruction_cache_dict,hit,miss,output=memory.doing_load_cache(pc_val,instruction_cache_dict,block_size,no_of_sets,instruction_dict,clockcycle,hit,miss,output)
        machine_code+=a[2:]
    return machine_code,hit,miss,output