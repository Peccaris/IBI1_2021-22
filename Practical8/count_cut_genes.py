import re #import regular expression

file_opened=open("/Users/yiyi/Git/IBI1_2021-22/Practical 8/cut_genes.fa") # open the file created by myself
file_readed=file_opened.read() # read the file
sequences=file_readed.replace('\n',"") # combine the lines
sequences=sequences.split('>')[1:] # split the sequences by '>'

number_of_cuts=[] # create a list that will store the number of cuts
a = len(sequences)
for i in range(0,a):   
    num = len(re.findall("GAATTC",sequences[i])) # find the site where the cut takes place and calculate the number of cuts
    number_of_cuts.append(num) #


gene_names=re.findall('[A-Z0-9]{7}',file_readed) # extract gene names 
complete_gene_sequence=re.findall('[A-T]{10,}',file_readed) #extract the complete gene sequences 

count_cut_genes=[] # created a list that will store the required information
for n in range(0,a):
    count_cut_genes.append('>'+ gene_names[n]+ "  The number of	cuts made by EcoRI:  "+ str(number_of_cuts[n])+'\n'+complete_gene_sequence[n]+'\n') # conbine the needed information into the list 

with open("/Users/yiyi/Git/IBI1_2021-22/Practical 8/count_cut_gene.fa",'w') as f: # create a file that will store the gene name, number of cuts and DNA sequences
    f.writelines(count_cut_genes) # write contents
f_opened=open("/Users/yiyi/Git/IBI1_2021-22/Practical 8/count_cut_gene.fa") #open the file 
count_cut_gene_file=f_opened.read() # read the file 
print(count_cut_gene_file) # print what the file contents