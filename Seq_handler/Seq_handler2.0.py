
# http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec24

from files_options import fasta_splitter, gbk_splitter
from seqs_options import dna_options, rna_options  # contains gc content, transcription, translation and back-transcription
from prot_options import aa_options                # contains blast for now
from Bio.Seq import Seq
from Bio.SeqUtils import GC
import os.path


# aa letters, minus 'ATCG': this tuple allows the code to decide if a sequence is aminoacidic or not
aa_only_letter = ("L", "M", "F", "W", "K", "Q", "E", "S", "P", "V", "I", "Y", "H", "R", "N", "D")



# starting input 
new_str = input("Insert your sequence or the path to a file >>> ")



# if there are no slashes it's not a path.
if "\\" not in new_str and "/" not in new_str:
    # if we have a seq long enough, it should be possible to infere its type by its letters composition 
    # ↓
    if len(new_str) > 20:                               
        for i in new_str.upper():
            if i in aa_only_letter:
                aa_options(new_str)                  
                break
            elif i == "U": 
                rna_options(new_str)
                break
        else:
            dna_options(new_str)                      
    # if it's a short seq, it asks for its type
    # ↓
    else:   
        which_seq_type = input("Which type of seq did you input? \n[AA, RNA, DNA] >>> ")
        
        if which_seq_type.lower() == 'aa' or which_seq_type == '1':
            aa_options(new_str)
        elif which_seq_type.lower() == 'rna' or which_seq_type == '2': 
            rna_options(new_str)
        elif which_seq_type.lower() == 'dna' or which_seq_type == '3':
            dna_options(new_str)

# check if the string is actually an existing path
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
