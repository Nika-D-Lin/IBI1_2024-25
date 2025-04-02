import re

input = open(r"C:\Users\lenovo\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
out_put = []
current_gene = None
current_sequence = []
for line in input:
    line = line.strip()
    if re.search('>',line):  # New gene sequence
        if current_gene:
            out_put.append((current_gene[0], '\n'.join(current_sequence)))
        current_gene = (re.findall(r'gene:(\S+)',line))
        current_sequence = []
    else:
        current_sequence.append(line)
        
if current_gene: #to check the final one
    out_put.append((current_gene[0], '\n'.join(current_sequence)))

input2 = open(r'C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical7\tata_genes.fa','w')
for gene_name, sequence in out_put:
        if re.search(r'TATA[AT]A[AT]', sequence):
            input2.write(f'> {gene_name}\n{sequence}\n')