
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec24

from seqs_options import dna_options, rna_options  # contengono trascrizione, traduzione, trascrizione inversa, gc content
from prot_options import aa_options                # contiene blast per ora
from Bio.Seq import Seq
from Bio.SeqUtils import GC



# input iniziale
new_seq = input("Insert your sequence: ")

# tolti gli aminoacidi che corrispondono a 'ACTG'
aa_only_letter = ("L", "M", "F", "W", "K", "Q", "E", "S", "P", "V", "I", "Y", "H", "R", "N", "D") 


# se abbiamo una sequenza abbastanza lunga dovrebbe essere possibile dedurne il tipo dalla sua composizione di 
# lettere, senza considerare la possibilità che siano solo ATCG e siano amminoacidi
# ↓
if len(new_seq) > 20:                               
    for i in new_seq.upper():
        if i in aa_only_letter:
           aa_options(new_seq)                  # definire una funzione per le opzioni aminoacidi
           break
        elif i == "U": 
            rna_options(new_seq)
            break
    else:
        dna_options(new_seq)                      # definire una funzione per le opzioni dna 
 
# se la seq è corta, si chiede che tipo di sequenza sia
# ↓
else:   
    which_seq_type = input("Which type of seq did you input? \n[AA, RNA, DNA]--> ")
    
    if which_seq_type.lower() == 'aa' or which_seq_type == '1':
        aa_options(new_seq)
    elif which_seq_type.lower() == 'rna' or which_seq_type == '2': 
        rna_options(new_seq)
    elif which_seq_type.lower() == 'dna' or which_seq_type == '3':
        dna_options(new_seq)
