import re  # import regular expression

# read the original fasta file
yeast_gene = open("/Users/yiyi/Desktop/IBI1_2021-22/Practical8/.Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa.icloud")  # open file
all_sequence = yeast_gene.read()  # read the file
sequences = all_sequence.replace('\n', "")  # combine the lines
sequences = sequences.split('>')  # split the str into single gene

# define a function that can help to turn lists into strings
def clean(input):   
    ret = str(input)
    ret = ret.replace("['", '')
    ret = ret.replace("]", '')
    ret = ret.replace('\'', '')
    ret = ret.replace(', ', '')
    return ret


EcoRI_cut_genes = []  # create a list storing the genes that can be cut by EcoRI
for match in range(0, len(sequences)):  # select genes that contain "GAATTC" sequence
    if "GAATTC" in sequences[match]:
        EcoRI_cut_genes.append(sequences[match])

gene_name = re.findall('gene:.......', str(
    EcoRI_cut_genes))  # select gene names
# store the gene names into string form
gene_name = clean(gene_name).split('gene:')[1:]

complete_gene_sequence = re.findall('[A-T]{10,}', str(EcoRI_cut_genes))
cut_gene_length = []  # create a list that stores the length of the genes
for i in range(0, len(complete_gene_sequence)):
    cut_gene_length.append(len(complete_gene_sequence[i]))  # store gene length

cuttable_genes = []  # create a list that will store the cuttable gene information
x = len(gene_name)
for n in range(0, x):
    cuttable_genes.append(
        '>' + gene_name[n] + "  " + clean(cut_gene_length[n])+'\n'+complete_gene_sequence[n]+'\n')

 # create a new file "cut_gene.fa"
with open("cut_genes.fa", 'w') as f: 
    f.writelines(cuttable_genes)  # store the above information into the file
open_file = open("cut_genes.fa")  # open the file
cut_genes = open_file.read()  # read the file
print(cut_genes)  # print to see if the file is the format we want
