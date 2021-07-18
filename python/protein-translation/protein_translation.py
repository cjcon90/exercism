from typing import List

CODONS = {
        "AUG": "Methionine",
        "UUU": "Phenylalanine",
        "UUC": "Phenylalanine",
        "UUA": "Leucine",
        "UUG": "Leucine",
        "UCU": "Serine",
        "UCC": "Serine",
        "UCA": "Serine",
        "UCG": "Serine",
        "UAU": "Tyrosine",
        "UAC": "Tyrosine",
        "UGU": "Cysteine",
        "UGC": "Cysteine",
        "UGG": "Tryptophan",
        "UAA": None,
        "UAG": None,
        "UGA": None,
        }

def proteins(strand: str) -> List[str]:
    translation = []
    for i in range(0, len(strand), 3):
        codon = strand[i:i+3]
        protein = CODONS[codon]
        if protein:
            translation.append(protein)
        else:
            break
    return translation
