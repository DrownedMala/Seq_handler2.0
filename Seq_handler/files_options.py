
import os, os.path
from Bio import SeqIO

# takes a multi-record fasta/gbk file
# and splits it into multiple files (1 seq/file)


def fasta_splitter(new_str):

    # creates destination folder for split files in the cwd ↓
    wd = f"{os.getcwd()}/Split_{os.path.basename(os.path.normpath(new_str))}" # assegna il nome del file originale anche alla cartella
    os.makedirs(f"{wd}")                 
    os.chdir(wd) # takes you to the directory in which files will be placed                            


    # for each new file: name of the file (descript. of org.); id e seq inside the file ↓ 
    for record in SeqIO.parse(new_str , "fasta"): 
        with open(f"{str(record.description)[33:]}.fasta", "w") as f: 
            f.write(f"{str(record.id)}\n{str(record.seq)}") 


    # security check: whether it finds or not the new folder, the script warns you ↓
    isdir = os.path.isdir(wd)  
    if isdir == True:
        print(f"\nA new folder \"Split_*\" was created as \"{os.getcwd()}\"")
    elif isdir == False:
        print("Something went wrong, folder was not created.")


def gbk_splitter(new_str):

    # crea cartella di destinazione per i file divisi nella cwd ↓
    wd = f"{os.getcwd()}/Split_{os.path.basename(os.path.normpath(new_str))}" # assegna il nome del file originale anche alla cartella
    os.makedirs(wd)                 
    os.chdir(wd) # porta alla directory in cui finiranno i nuovi file                              


    # per ogni file diviso assegna: nome del file (descrizione org.), id e sequenza all'interno del file stesso ↓ 
    for record in SeqIO.parse(new_str , "genbank"): 
        with open(f"{str(record.description)}.gbk", "w") as f: 
            f.write(f"{str(record.id)}\n{str(record.seq)}") 


    # check di sicurezza: se trova o meno la cartella appena creata, avverte ↓
    isdir = os.path.isdir(wd)  
    if isdir == True:
        print(f"\nA new folder \"Split_*\" was created as \"{os.getcwd()}\"")
    elif isdir == False:
        print("Something went wrong, folder was not created.")


# reference paths of mine to test
# /home/mala/Coding/Python/DataAnalysis/Pandas/ls_orchid.fasta    
# /home/mala/Coding/Python/DataAnalysis/Pandas/ls_orchid.gbk