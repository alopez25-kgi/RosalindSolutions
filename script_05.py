with open('human_genes.fasta', 'r') as file:
    lines = file.readlines()


gene_dict = {}
current_gene = None

for line in lines:
    line = line.strip()
    if line.startswith('>'):
        current_gene = line[1:].split()[0]
        gene_dict[current_gene] = ''
    elif current_gene is not None:
        gene_dict[current_gene] += line


with open('gc_report.txt', 'w') as report:
    for gene, seq in gene_dict.items():
        seq = seq.upper()
        gc_count = seq.count('G') + seq.count('C')
        gc_percent = gc_count / len(seq) * 100 if len(seq) > 0 else 0.0
        report.write(f"{gene}\t{gc_percent:.1f}\n")
