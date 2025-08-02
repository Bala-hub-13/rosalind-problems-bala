Seq = "/home/bm/Downloads/rosalind_gc.txt"

with open(Seq, 'r') as DNA_Seq:
    lines = DNA_Seq.readlines()
    for line in lines[:5]:
        print(line.strip())