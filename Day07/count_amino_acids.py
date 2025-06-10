import sys
from collections import Counter

codon_table = {
    'Phe': ['TTT', 'TTC'],
    'Leu': ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG'],
    'Ile': ['ATT', 'ATC', 'ATA'],
    'Met': ['ATG'],
    'Val': ['GTT', 'GTC', 'GTA', 'GTG'],
    'Ser': ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'],
    'Pro': ['CCT', 'CCC', 'CCA', 'CCG'],
    'Thr': ['ACT', 'ACC', 'ACA', 'ACG'],
    'Ala': ['GCT', 'GCC', 'GCA', 'GCG'],
    'Tyr': ['TAT', 'TAC'],
    'His': ['CAT', 'CAC'],
    'Gln': ['CAA', 'CAG'],
    'Asn': ['AAT', 'AAC'],
    'Lys': ['AAA', 'AAG'],
    'Asp': ['GAT', 'GAC'],
    'Glu': ['GAA', 'GAG'],
    'Cys': ['TGT', 'TGC'],
    'Trp': ['TGG'],
    'Arg': ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'],
    'Gly': ['GGT', 'GGC', 'GGA', 'GGG'],
    # Stop codons
    'STOP': ['TAA', 'TAG', 'TGA']
}

# Reverse mapping: codon → amino acid
codon_to_aa = {codon: aa for aa, codons in codon_table.items() for codon in codons}

def read_sequence(filename):
    """Read a DNA sequence from a file, handling FASTA headers if present."""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # Remove FASTA headers (lines starting with >) and join all others
    sequence = ''.join(line.strip() for line in lines if not line.startswith('>'))
    sequence = sequence.upper().replace(' ', '').replace('\n', '')
    return sequence

def translate_and_count(sequence):
    """Translate DNA sequence into amino acids and count them."""
    counts = Counter()

    for i in range(0, len(sequence) - 2, 3):
        codon = sequence[i:i+3]
        aa = codon_to_aa.get(codon)
        if aa and aa != 'STOP':
            counts[aa] += 1
    return counts

def main():
    if len(sys.argv) < 2:
        print("Usage: python count_amino_acids.py <dna_sequence_file>")
        sys.exit(1)

    seq = read_sequence(sys.argv[1])
    aa_counts = translate_and_count(seq)

    for aa in sorted(aa_counts):
        print(f"{aa} {aa_counts[aa]}")

if __name__ == "__main__":
    main()
