# #!usr/bin/python3

from Bio.Seq import Seq
from Bio.SeqUtils import GC

# le opzioni che si hanno per agire su sequenze di DNA
def dna_options(new_seq):
    dna_seq = Seq(new_seq).upper()
    what_next = ""
    ok_input = ("1", "2", "3")
    while what_next == "" or what_next not in ok_input:
        what_next = input("""What are you willing to do now?      
                            You can:\n
                            1) Transcribe it\n
                            2) Translate it\n
                            3) Get its GC content\n
                            >>> """)  

        if what_next == '1':
            coding_or_template = input("\nIs it a coding strand? (y/n) >>> ")

            if coding_or_template.lower() == 'y':
                print(f"\nCodingSeq Transcribed (as 5'→3'): {dna_seq.transcribe()}\n")
            elif coding_or_template.lower() == 'n':
                print(f"\nTemplateSeq Transcribed (as 5'→3'): {dna_seq.reverse_complement().transcribe()}\n")

        elif what_next == '2':
            which_org = input("\nIs it 1)human or 2)mitochondrial dna? (1/2) >>> ")   # dna mitocondriale o umano?
            if which_org == '1':                                                      # è necessario per sapere quale 
                cds = input("\nIs it a CDS? (y/n) >>> ")                              # tabella di conversione usare
                if cds.lower() == 'y':  
                    print(f"Translated: {dna_seq.translate(to_stop=True)}\n")
                elif cds.lower() == 'n':
                    print(f"Translated: {dna_seq.translate(to_stop=False)} \n(Any * is a stop codon)")
            elif which_org == '2':
                cds = input("Is it a CDS? (y/n) >>> ")                              # se CDS si ferma al primo 
                if cds.lower() == 'y':                                              # codone di stop
                    print(f"Translated: {dna_seq.translate(table=2, to_stop=True)}\n")
                elif cds.lower() == 'n':
                    print(f"Translated: {dna_seq.translate(table=2, to_stop=False)} \n(Any * is a stop codon)")

        elif what_next == '3':
            print(f"GC content is: {GC(dna_seq)}\n")

        else:
            print("Please, choose between 1, 2 or 3!\n\n")
            continue

# le opzioni che si hanno per agire su sequenze di mRNA
# def rna_options(new_seq):

# le opzioni che si hanno per agire su sequenze di AA
# def prot_options(new_seq):


# input iniziale
new_seq = input("Insert your sequence: ")

# tolti gli aminoacidi che corrispondono a 'ACTG'
aa_only_letter = ("L", "M", "F", "W", "K", "Q", "E", "S", "P", "V", "I", "Y", "H", "R", "N", "D") 


# se abbiamo una sequenza abbastanza lunga dovrebbe essere possibile dedurne il tipo dalla sua composizione di 
# lettere, senza considerare la possibilità che siano solo ATCG e siano aminoacidi
# ↓
if len(new_seq) > 15:                               
    for i in new_seq.upper():     # scansiona la sequenza passata per cercare lettere che non siano 'A','C','T','G'
        if i in aa_only_letter:   # se in 16 caratteri ci sono solo quelle 4 lettere, difficilmente sono AA
           print("prot_options(new_seq)")                  # definire una funzione per le opzioni aminoacidi
           break
        elif i == "U":            # se c'è un uracile, sarà una seq di RNA
            print("rna_options(new_seq)")           # definire una funzione per le opzioni rna
            break
    else:
        dna_options(new_seq)       # apre le opzioni da eseguire su sequenze di DNA                
 
# se la seq è corta, si chiede che tipo di sequenza sia
# ↓
else:   
    which_seq_type = input("Which type of seq did you input? \n[AA, RNA, DNA]--> ")
    
    if which_seq_type.lower() == 'aa' or which_seq_type == '1':
        print("prot_options(new_seq)")
    elif which_seq_type.lower() == 'rna' or which_seq_type == '2': 
        print("rna_options(new_seq)")
    elif which_seq_type.lower() == 'dna' or which_seq_type == '3':
        dna_options(new_seq)     # apre le opzioni da eseguire su sequenze di DNA
