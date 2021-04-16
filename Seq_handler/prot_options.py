from Bio.Seq import Seq
from Bio.Blast import NCBIWWW, NCBIXML


def prot_options(new_seq):
    # maybe a blast?
    prot_seq = Seq(new_seq.upper())
    
    blasted = NCBIWWW.qblast("blastp", "nr", prot_seq)
    blast_records = NCBIXML.parse(blasted)

    threshold = 1e-50
    for record in blast_records:
        if record.alignments:
            print(f"\nQuery: {record.query[:100]}\n")
            for align in record.alignments:
                for hsp in align.hsps:
                    if hsp.expect < threshold:
                        print(">")
                        print(f"match: {align.title[:100]}")
                        print(f"score: {hsp.score}")
                        print(">\n")


new_seq = input("sequenza: ")
prot_options(new_seq)
