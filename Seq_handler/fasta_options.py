
# Programma che prende un file fasta con più record
# e lo divide un record/file
import os, os.path
from Bio import SeqIO



#def Parse_and_write(path):
# controlla l'esistenza del file in input, da splittare in seguito ↓
isFile = False 
path = input("Insert you FASTA file's path: ") 
isFile = os.path.isfile(path) # se non è un file, entra il ciclo per richiedere il path, altrimenti prosegue
while isFile == False: # controlla che il file esista, prima di creare una cartella per lasciarla vuota
    path = input("There is an error in the FASTA file's path, try again: ") # dovrebbe prelevare il file dal percorso datogli
    isFile = os.path.isfile(path)



# crea cartella di destinazione per i file divisi nella cwd ↓
wd = f"{os.getcwd()}/{os.path.basename(os.path.normpath(path))}_Split" # assegna il nome del file originale anche alla cartella
os.makedirs(f"{wd}")                 
os.chdir(wd) # porta alla directory in cui finiranno i nuovi file                              



# per ogni file diviso assegna: nome del file (descrizione org.), id e sequenza all'interno del file stesso ↓ 
for record in SeqIO.parse(path , "fasta"): 
    with open(f"{str(record.description)[33:]}.fasta", "w") as f: 
       f.write(f"{str(record.id)}\n{str(record.seq)}") 



# check di sicurezza: se trova o meno la cartella appena creata, avverte ↓
isdir = os.path.isdir(wd)  
if isdir == True:
    print(f"\nA new folder \"_Split\" was created as \"{os.getcwd()}\"")
else:
    print("Something went wrong, folder was not created.")


# /home/mala/Progr_learning/Python/DataAnalysis/Pandas/ls_orchid.fasta    