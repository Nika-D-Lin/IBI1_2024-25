import re
#when find the next name, append the last name and seqyence
input = open(r"C:\Users\lenovo\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
out_put = []
current_gene = None #at first, there is no name
current_sequence = []
for line in input:
    line = line.strip() #delete the blank character
    if re.search('>',line):  # New gene sequence
        if current_gene:
            out_put.append((current_gene[0], '\n'.join(current_sequence))) #use \n to make each line in different lines
        current_gene = (re.findall(r'gene:(\S+)',line)) #only use the name by ()
        current_sequence = [] #clear the list for the next name to use
    else:
        current_sequence.append(line)
        
if current_gene: #to check the final one
    out_put.append((current_gene[0], '\n'.join(current_sequence)))

input2 = open(r'C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical7\tata_genes.fa','w')
for gene_name, sequence in out_put: #use two new varieties to meet the two kinds--current_gene and current_sequence
        if re.search(r'TATA[AT]A[AT]', sequence): #use [] to search 'TATATAT' or 'TATATAA' or 'TATAAAT' or 'TATAAAA'
            input2.write(f'> {gene_name}\n{sequence}\n')