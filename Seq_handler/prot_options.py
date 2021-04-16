from Bio.Seq import Seq
from Bio.Blast import NCBIWWW


def prot_options(new_seq):
    # maybe a blast?
    prot_seq = Seq(new_seq.upper())

