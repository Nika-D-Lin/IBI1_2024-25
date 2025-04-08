def Restriction_enzyme_cut_sites(DNA_sequences, recognised_sequence): #set the function to input DNA and recognised sequences
    for i in range(len(DNA_sequences) - len(recognised_sequence) + 1): #To make sure that every value can be circulation and there won't be error.
        if DNA_sequences[i:i + len(recognised_sequence)] == recognised_sequence:
            return i + 1 #return the location
    return ("Error: The DNA sequence doesn't contain canonical nucleotides")

DNA = input('DNA:')
Recognised_sequence = input('Recognised:')
print(Restriction_enzyme_cut_sites(DNA,Recognised_sequence))

#example:
print(Restriction_enzyme_cut_sites('ACTGCTAGATCG','GCTA'))
#the answer should be 4