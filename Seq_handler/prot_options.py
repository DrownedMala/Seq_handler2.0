from Bio.Seq import Seq
from Bio.Blast import NCBIWWW

new_seq = "abc"

def prot_options(new_seq):
    # maybe a blast?
    print(f"I'm {new_seq}")
    #prot_seq = Seq(new_seq.upper())

prot_options(new_seq)