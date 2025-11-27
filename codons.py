def create_codon_dict(path):
    codon_to_amino_acid = {}
    with open(path, 'r') as f:
    for row in f:
        cell = row.strip().split('\t')
        if len(cells) < 3:
                continue
        codon= cell[0]
        acid = cell[2]
        codon_to_amino_acid [codon] = acid
    
    return codon_to_amino_acid



