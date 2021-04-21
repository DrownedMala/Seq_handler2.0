from Bio.Seq import Seq
from Bio.Blast import NCBIWWW, NCBIXML

# prende in input la sequenza data nel main ed esegue un blast, 
# restituisce titolo del risultato e score

def aa_options(new_str):        
    
    what_to_do = input("""What are you willing to do now?\n
                       You can:\n
                       1) run a blast on the sequence you entered.\n
                       2) --- \n
                       >>> """)

    if what_to_do == "1" or what_to_do.lower() == "blast":
        print("A blast is being run by now, wait for the results!")
        prot_seq = Seq(new_str.upper())
        
        
        blasted = NCBIWWW.qblast("blastp", "nr", prot_seq)
        blast_records = NCBIXML.parse(blasted)


        threshold = 1e-40
        for record in blast_records:
            if record.alignments:
                print(f"\nQuery: {record.query[:100]}\n")
                for align in record.alignments:
                    for hsp in align.hsps:
                        if hsp.expect < threshold:
                            print(f"match: {align.title[:100]}")
                            print(f"E-value: {hsp.expect}")
                            print("")


# MKWVTFISLLFLFSSAYSRGVFRRDAHKSEVAHRFKDLGEENFKALVLIAFAQYLQQCPFEDHVKLVNEV
# TEFAKTCVADESAENCDKSLHTLFGDKLCTVATLRETYGEMADCCAKQEPERNECFLQHKDDNPNLPRLV
# RPEVDVMCTAFHDNEETFLKKYLYEIARRHPYFYAPELLFFAKRYKAAFTECCQAADKAACLLPKLDELR
# DEGKASSAKQRLKCASLQKFGERAFKAWAVARLSQRFPKAEFAEVSKLVTDLTKVHTECCHGDLLECADD
# RADLAKYICENQDSISSKLKECCEKPLLEKSHCIAEVENDEMPADLPSLAADFVESKDVCKNYAEAKDVF
# LGMFLYEYARRHPDYSVVLLLRLAKTYETTLEKCCAAADPHECYAKVFDEFKPLVEEPQNLIKQNCELFE
# QLGEYKFQNALLVRYTKKVPQVSTPTLVEVSRNLGKVGSKCCKHPEAKRMPCAEDYLSVVLNQLCVLHEK
# TPVSDRVTKCCTESLVNRRPCFSALEVDETYVPKEFNAETFTFHADICTLSEKERQIKKQTALVELVKHK
# PKATKEQLKAVMDDFAAFVEKCCKADDKETCFAEEGKKLVAASQAALGL