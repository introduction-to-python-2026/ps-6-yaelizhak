def create_codon_dict(path):
    row = rows[0]
    codon_to_amino_acid = {}
    for row in rows:
        cell = row.strip().split('\t')
        codon= cell[0]
        acid = cell[2]
        codon_to_amino_acid [codon] = acid
    
    return codon_to_amino_acid



