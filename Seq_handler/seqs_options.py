
from Bio.Seq import Seq
from Bio.SeqUtils import GC

# Raccoglie le opzioni disponibili per la gestione di sequenze di DNA ed RNA.
 
def dna_options(new_seq):
    dna_seq = Seq(new_seq).upper()
    what_next = ""
    ok_input = ("1", "2", "3")
    while what_next == "" or what_next not in ok_input:
        what_next = input("""What are you willing to do now?      
                            You can:\n
                            1) Transcribe \n
                            2) Translate \n
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

def rna_options(new_seq):
    rna_seq = Seq(new_seq).upper()
    what_next = ""
    ok_input = ("1", "2", "3")
    while what_next == "" or what_next not in ok_input:
        what_next = input("""What are you willing to do now?      
                            You can:\n
                            1) Translate \n
                            2) Retro-transcribe \n
                            3) Get its GC content\n
                            >>> """)

        if what_next == "1":
            which_org = input("\nIs it 1)human or 2)mitochondrial dna? (1/2) >>> ")   # dna mitocondriale o umano?
            if which_org == '1':                                                      # è necessario per sapere quale 
                cds = input("\nIs it a CDS? (y/n) >>> ")                              # tabella di conversione usare
                if cds.lower() == 'y':  
                    print(f"Translated: {rna_seq.translate(to_stop=True)}\n")
                elif cds.lower() == 'n':
                    print(f"Translated: {rna_seq.translate(to_stop=False)} \n(Any * is a stop codon)")
            elif which_org == '2':
                cds = input("Is it a CDS? (y/n) >>> ")                              # se CDS si ferma al primo 
                if cds.lower() == 'y':                                              # codone di stop
                    print(f"Translated: {rna_seq.translate(table=2, to_stop=True)}\n")
                elif cds.lower() == 'n':
                    print(f"Translated: {rna_seq.translate(table=2, to_stop=False)} \n(Any * is a stop codon)")
        elif what_next == "2":
            print(f"Back-transcribed: {rna_seq.back_transcribe()} \n")
        elif what_next == "3":
            print(f"GC content is: {GC(rna_seq)} \n")
        else:
            print("Please, choose between 1, 2 or 3!\n\n")
            continue
