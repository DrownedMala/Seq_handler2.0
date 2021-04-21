
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec24

from files_options import fasta_splitter, gbk_splitter
from seqs_options import dna_options, rna_options  # contengono trascrizione, traduzione, trascrizione inversa, gc content
from prot_options import aa_options                # contiene blast per ora
from Bio.Seq import Seq
from Bio.SeqUtils import GC
import os.path


# tolti gli aminoacidi che corrispondono a 'ACTG', queste sono le lettere che servono al programma 
# per decidere se la sequenza sia amminoacidica o nucleotidica
aa_only_letter = ("L", "M", "F", "W", "K", "Q", "E", "S", "P", "V", "I", "Y", "H", "R", "N", "D")



# input iniziale
new_str = input("Insert your sequence or the path to a file >>> ")



# se non ci sono slash probabilmente non è un percorso per un file.
if "\\" not in new_str and "/" not in new_str:
    # se abbiamo una sequenza abbastanza lunga dovrebbe essere possibile dedurne il tipo dalla sua composizione di 
    # lettere, senza considerare la possibilità che siano solo ATCG e siano amminoacidi
    # ↓
    if len(new_str) > 20:                               
        for i in new_str.upper():
            if i in aa_only_letter:
                aa_options(new_str)                  # definire una funzione per le opzioni aminoacidi
                break
            elif i == "U": 
                rna_options(new_str)
                break
        else:
            dna_options(new_str)                      # definire una funzione per le opzioni dna 
    # se la seq è corta, si chiede che tipo di sequenza sia
    # ↓
    else:   
        which_seq_type = input("Which type of seq did you input? \n[AA, RNA, DNA] >>> ")
        
        if which_seq_type.lower() == 'aa' or which_seq_type == '1':
            aa_options(new_str)
        elif which_seq_type.lower() == 'rna' or which_seq_type == '2': 
            rna_options(new_str)
        elif which_seq_type.lower() == 'dna' or which_seq_type == '3':
            dna_options(new_str)

#controlla che la stringa passata sia un percorso esistente per un file
elif "\\" in new_str or "/" in new_str:
    while os.path.exists(new_str) == False: # controlla il percorso
        new_str = input("It seems you tried to work on a file, but the path isn't correct. Check it and retry. \n>>> ")
    
    what_now = input(f"""\nYour file is \"{os.path.basename(os.path.normpath(new_str))}\"; 
                    What do you want to do now?\n
                    1) Split a multi-fasta in single fasta files\n
                    2) --- \n
                    >>> """)
    
    if what_now == "1" or what_now.lower() == "split":
        fasta_splitter(new_str)
    



