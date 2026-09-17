# APOE Gene DNA Analyzer

A beginner bioinformatics project analyzing the APOE gene — the strongest known genetic risk factor for Alzheimer's disease. Research has shown that the APOE ε4 allele confers greater Alzheimer's risk in women than in men, an effect that received comparatively little attention for years due to a historical tendency in medical research to treat male physiology as the default. This project is a first step torward engaging directly with genetic data on sex-specific neurological risk, rather than relying solely on existing literature.

## What it does
-Loads the APOE gene sequence (NCBI GeneID: 348)
-Calculates nucleotide composition and GC content 
Computes the reverse complement
-Transcribes DNA to RNA
-Translates RNA to protein

##What I learned
Translating the full genomic sequence produces a protein much shorter than the real APOE protein, because genomic DNA includes introns that are normally spliced out before translation. This became clear once i compared the output length to protein.faa, the true protein sequence

## Data source 
NCBI Gene, GeneID 348 (APOE), Homo sapiens 

## How to run 
pip install biopython 
python apoe_dna_analyser.py
