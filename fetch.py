#Returns two dictionaries one with the text and other with data part

def form_dict_text(sample_file):
    dict_text={}
    for line in sample_file:
        words=line.split()
        if words[0]=='0xffffc':      #Have taken 0xffffc as delimiter for text segment
            break
        dict_text[words[0]]=words[1]
    return dict_text

def form_dict_data(sample_file):
    dict_data={}
    for line in sample_file:
        words=line.split()
        dict_data[words[0]]=words[1]
    return dict_data

def fetch_file(mc_file):
    dict_text=form_dict_text(mc_file)
    dict_data=form_dict_data(mc_file)

    return dict_text,dict_data
