
import os, os.path
from Bio import SeqIO

# Programma che prende un file fasta con più record
# e lo divide un record/file


def fasta_splitter(new_str):

    # crea cartella di destinazione per i file divisi nella cwd ↓
    wd = f"{os.getcwd()}/Split_{os.path.basename(os.path.normpath(new_str))}" # assegna il nome del file originale anche alla cartella
    os.makedirs(f"{wd}")                 
    os.chdir(wd) # porta alla directory in cui finiranno i nuovi file                              


    # per ogni file diviso assegna: nome del file (descrizione org.), id e sequenza all'interno del file stesso ↓ 
    for record in SeqIO.parse(new_str , "fasta"): 
        with open(f"{str(record.description)[33:]}.fasta", "w") as f: 
            f.write(f"{str(record.id)}\n{str(record.seq)}") 


    # check di sicurezza: se trova o meno la cartella appena creata, avverte ↓
    isdir = os.path.isdir(wd)  
    if isdir == True:
        print(f"\nA new folder \"Split_*\" was created as \"{os.getcwd()}\"")
    else:
        print("Something went wrong, folder was not created.")


# /home/mala/Progr_learning/Python/DataAnalysis/Pandas/ls_orchid.fasta    