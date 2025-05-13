import re

def comparasion(seq1, seq2):
    same_sequence = 0
    for	i in range(len(seq1)):	
        if seq1[i] == seq2[i]:				
            same_sequence += 1
    return f"{same_sequence/len(seq1)*100}%"

with open(r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical13\human_sod2.fasta") as f1:
    lines = f1.readlines()
    sequence = []
    for line in lines:
        if not re.search(r">",line):
            sequence.append(line)
seq1 = ''.join(sequence)

with open(r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical13\mouse_sod2.fasta") as f2:
    lines = f2.readlines()
    sequence = []
    for line in lines:
        if not re.search(r">",line):
            sequence.append(line)
seq2 = ''.join(sequence)

with open(r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical13\random.fasta") as f3:
    lines = f3.readlines()
    sequence = []
    for line in lines:
        if not re.search(r">",line):
            sequence.append(line)
seq3 = ''.join(sequence)

with open(r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical13\BLOSUM62.txt") as f4:
    lines = f4.readlines()
    sequence = []
    for line in lines:
        if not re.search(r'#',line):
            sequence.append(line.strip())
matrix = sequence

def BLOSUM62_calculate(seq1, seq2):
    diffenrent = []
    for	i in range(len(seq1)):	
        if seq1[i] != seq2[i]:
            diffenrent.append(seq1+seq2)

    score = 0
    for pair in diffenrent:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if pair[0] == matrix[0][i] and pair[1] == matrix[j][0]:
                    score += int(matrix[j][i])
    return score

group = [("human and mouse", seq1, seq2), ("human and random", seq1, seq3), ("mouse and random", seq2, seq3)]

for label, seq1, seq2 in group:
    print(f"As for {label}: the identity is {comparasion(seq1, seq2)}, and the BLOSUM62 is {BLOSUM62_calculate(seq1, seq2)}")