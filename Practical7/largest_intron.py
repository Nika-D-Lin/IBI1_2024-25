import re

seq = 'ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA'
a = re.findall(r'GT\S+AG',seq) #search the intron that is from GT to AG
print(len(a[0])) #a is a list. If print(a), it will count the element in this list and out put 1. So, use a[0] to chooce the target one.