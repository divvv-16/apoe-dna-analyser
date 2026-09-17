from pathlib import Path

from Bio import SeqIO

sequence_file = Path(__file__).with_name("gene.fna.txt")
record = next(SeqIO.parse(sequence_file, "fasta"))
dna_seq = str(record.seq)

print("Sequence ID:", record.id)
print("Length:", len(dna_seq))

def count_nucleotides(seq):
    counts={
        "A": seq.count("A"),
        "T": seq.count("T"),
        "C": seq.count("C"),
        "G": seq.count("G")
    }
    return counts

nucleotide_counts=count_nucleotides(dna_seq)
print("Nucleotide Counts:", nucleotide_counts)

def gc_content(seq):
    g = seq.count("G")
    c = seq.count("C")
    total = len(seq)
    percentage = (g+c) / total * 100
    return round(percentage, 2)

print("GC content:", gc_content(dna_seq), "%")

def reverse_complement(seq):
    complement_map={"A": "T", "T": "A", "C": "G", "G": "C", "N": "N"}
    complemented = ""
    for base in seq:
        complemented = complemented + complement_map.get(base, "N")
    return complemented[::-1]

print("Reverse complement (first 60):", reverse_complement(dna_seq)[:60])

def transcribe(seq):
    return seq.replace("T", "U")

rna_seq = transcribe(dna_seq)
print("RNA (first 60):", rna_seq[:60])

CODON_TABLE = {
    "UUU": "F", "UUC": "F", "UUA": "L", "UUG": "L",
    "CUU": "L", "CUC": "L", "CUA": "L", "CUG": "L",
    "AUU": "I", "AUC": "I", "AUA": "I", "AUG": "M",
    "GUU": "V", "GUC": "V", "GUA": "V", "GUG": "V",
    "UCU": "S", "UCC": "S", "UCA": "S", "UCG": "S",
    "CCU": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    "ACU": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    "GCU": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    "UAU": "Y", "UAC": "Y", "UAA": "*", "UAG": "*",
    "CAU": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    "AAU": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    "GAU": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    "UGU": "C", "UGC": "C", "UGA": "*", "UGG": "W",
    "CGU": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    "AGU": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    "GGU": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}   

def translate(rna):
    protein = ""
    for i in range(0, len(rna) - 2, 3):
        codon = rna[i:i + 3]
        amino_acid = CODON_TABLE.get(codon, "X")
        if amino_acid == "*":
            break 
        protein = protein + amino_acid
    return protein

protein_seq = translate(rna_seq)
print("Protein (first 60):", protein_seq[:60])
print("Protein length:", len(protein_seq))

test_sequence_file = Path(__file__).with_name("test_sequence.fna")
record = next(SeqIO.parse(test_sequence_file, "fasta"))
