
# Programma che prende un file fasta con più record
# e lo divide un record/file

from Bio import SeqIO


#def Parse_and_write():
num = 0

for record in SeqIO.parse("/home/mala/Progr_learning/Python/Biopython/ls_orchid.fasta", "fasta"): 
    num += 1
    with open(f"file{num}.fasta", "w") as f:
        f.write(f"{str(record.id)}\n{str(record.seq)}")

# funziona!