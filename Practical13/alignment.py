import re

def comparasion(seq1, seq2):
    same_sequence = 0
    for	i in range(len(seq1)):	
        if seq1[i] == seq2[i]:				
            same_sequence += 1
    return f"{same_sequence/len(seq1)*100}%"

def sequence(seq):
    with open(seq) as f1:
        lines = f1.readlines()
        sequence = []
        for line in lines:
            if not re.search(r">",line):
                sequence.append(line.strip()) #use strip() to delete the space
    return ''.join(sequence) #to put each line together in one line

seq1 = r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical13\human_sod2.fasta"
seq2 = r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical13\mouse_sod2.fasta"
seq3 = r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical13\random.fasta"

seq1 = sequence(seq1)
seq2 = sequence(seq2)
seq3 = sequence(seq3)

with open(r"C:\Users\lenovo\OneDrive - International Campus, Zhejiang University\桌面\Github\IBI1_2024-25\Practical13\BLOSUM62.txt") as f4:
    lines = f4.readlines()
    sequence = []
    for line in lines:
        if not re.search(r'#',line):
            sequence.append(line)
matrix = sequence

def BLOSUM62_calculate(seq1, seq2):
    pairs = []
    for	i in range(len(seq1)):	
        pairs.append(seq1[i]+seq2[i])

    score = 0
    for pair in pairs:
        for i in range(len(matrix[0])): #use two for circle to read the matrix
            for j in range(len(matrix)):
                if pair[0] == matrix[0][i] and pair[1] == matrix[j][0]:
                    score += int(matrix[j][i])
    return score

group = [("human and mouse", seq1, seq2), ("human and random", seq1, seq3), ("mouse and random", seq2, seq3)]

for label, seq1, seq2 in group: #use the three eletment groups to fit the three varieties
    print(f"As for {label}: the identity is {comparasion(seq1, seq2)}, and the BLOSUM62 is {BLOSUM62_calculate(seq1, seq2)}")