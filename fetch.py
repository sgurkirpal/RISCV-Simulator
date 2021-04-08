#Returns two dictionaries one with the text and other with data part

def increment_pc(pc):   #takes a hex string as input and returns a hex string with 0x4 added in it
    pc_int=int(pc,16)
    new_pc=pc_int + 0x4
    new_pc=hex(new_pc)
    return str(new_pc)

def fetch_file(mc_file):
    dict_text={}
    dict_data={}
    flag=0 # 0 while we add pc and 1 while adding memory
    for line in mc_file:
        words=line.split()
        if(words[0]=='0xffffc'):   # delimilter --> 0xffffc
            flag=1
            continue
        if flag==0:
            dict_text[words[0]]=words[1]
        else:
            if(len(words[1]==3)):
                words[1]=words[:2]+'0'+words[2:]
            dict_data[words[0]]=words[1]
        
    return dict_text,dict_data
