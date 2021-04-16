import time
from Bio.Seq import Seq
from Bio.Blast import NCBIWWW, NCBIXML

start = time.time()


new_seq = input("Input your seq: ")
prot_seq = Seq(new_seq.upper())

# insulin:
# malwmrllpllallalwgpdpaaafvnqhlcgshlvealylvcgergffytpktrreaedlqvgqvelgggpgagslqplalegslqkrgiveqcctsicslyqlenycn

#  per NCBIWWW.qblast() sono necessari 3 parametri: 
# - il tipo di blast da effettuare: https://blast.ncbi.nlm.nih.gov/Blast.cgi
# - il database contro cui cercare: ftp://ftp.ncbi.nlm.nih.gov/pub/factsheets/HowTo_BLASTGuide.pdf
# - la sequenza sottoposta alla ricerca.

results = NCBIWWW.qblast("blastp", "nr", prot_seq)
blast_records = NCBIXML.parse(results)

E_VALUE_THRESH = 1e-20
for record in blast_records:
    if record.alignments: 
        print(f"\nQuery: {record.query[:100]}\n") 
        for align in record.alignments[0:10]: 
            for hsp in align.hsps: 
                if hsp.expect < E_VALUE_THRESH: 
                    print(">")
                    print(f"match: {align.title[:100]}")
                    print(f"score: {hsp.score}")
                    print(">\n")

print(f"\nRan in: {time.time() - start}")