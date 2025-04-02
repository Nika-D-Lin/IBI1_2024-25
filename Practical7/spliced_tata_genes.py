import re

input0 = open(r"C:\Users\lenovo\Downloads\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r')
out_put = []
current_gene = None
current_sequence = []
for line in input0:
    line = line.strip()
    if re.search('>',line):  # New gene sequence
        if current_gene:
            out_put.append((current_gene[0], ''.join(current_sequence)))
        current_gene = (re.findall(r'gene:(\S+)',line))
        current_sequence = []
    else:
        current_sequence.append(line)
        
if current_gene: #to check the final one
    out_put.append((current_gene[0], ''.join(current_sequence)))

spliced_gene = input("chooce one:GTAG, GCAG, ATAC ")
input2 = open(fr'C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical7\{spliced_gene}_spliced_genes.fa','w')
for gene_name, sequence in out_put:
        if re.search(r'TATA[AT]A[AT]', sequence):
            if re.search(fr'{spliced_gene}', sequence):
                number = len(re.findall(r'TATA[AT]A[AT]', sequence))
                input2.write(f'> {gene_name}\n{sequence}\n{number}\n')