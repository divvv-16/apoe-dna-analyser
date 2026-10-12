# APOE Gene DNA Analyser

A Python/Biopython tool that analyses the human *APOE* gene (NCBI GeneID 348), the strongest common genetic risk factor for late-onset Alzheimer's disease.

**Motivation.** The APOE ε4 allele is associated with higher Alzheimer's risk in women than in men (e.g. Farrer et al., JAMA 1997; Neu et al., JAMA Neurology 2017). I built this to work directly with the gene's sequence data rather than only reading about it. *(Check both citations before keeping them.)*

## What it does
- Loads the APOE genomic sequence from a FASTA file
- Counts nucleotides and calculates GC content
- Computes the reverse complement
- Transcribes DNA to RNA and translates RNA to protein
- Compares the translated output against the NCBI reference protein

## What I learned
Translating the full genomic sequence gives a protein far shorter than the real APOE protein. Genomic DNA contains introns, which are spliced out before translation. I confirmed this by comparing the output length to the reference protein (`protein.faa`).

## Data
Download from NCBI Gene (GeneID 348, *Homo sapiens*): the gene FASTA (`gene.fna.txt`) and protein FASTA (`protein.faa`). Place both in the same folder as the script.

## How to run
```bash
pip install biopython
python apoe_dna_analyser.py
```

## Example output
(paste your real output here)

## Next steps
- Extract the coding sequence (CDS) so translation matches the reference protein
- Call the ε2/ε3/ε4 genotype from rs429358 and rs7412
