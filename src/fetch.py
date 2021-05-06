#Returns two dictionaries one with the text and other with data part

def increment_pc(pc):   #takes a hex string as input and returns a hex string with 0x4 added in it
    pc_int=int(pc,16)
    new_pc=pc_int + 0x4
    new_pc=hex(new_pc)
    return str(new_pc)

def decrement_pc(pc,index):
    pc_int=int(pc,16)
    new_pc=pc_int - index
    new_pc=hex(new_pc)
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
            dict_text[words[0]]=words[1]
        else:
            if(len(words[1])==3):
                words[1]=words[1][:2]+'0'+words[1][2:]
            dict_data[words[0]]=words[1]
        
    return dict_text,dict_data

def cacheinitialization():
    print("Enter the value for cachesize(in Bytes only)")
    cachesize=int(input())
    print("Enter the value for blocksize(in Bytes only)")
    blocksize=int(input())
    print("Enter number of ways for SA")
    k=int(input())
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
            print(memorycachedict)
            memorycachedict[i][j].append(0)
            memorycachedict[i][j].append(-1)
            memorycachedict[i][j].append(-1)
            for _ in range(blocksize):
                memorycachedict[i][j].append(-1)
    return no_of_blocks,no_of_sets,memorycachedict,k,blocksize,cachesize


#instruction cache dict is exactly same as memory cache dict
def instruction_initialization(no_of_sets,k,blocksize):
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
    return InstructionCacheDict