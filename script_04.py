with open('human_genes.fasta', 'r') as file:
    lines = file.readlines()

gene_dict = {}
current_gene = None

for line in lines:
    line = line.strip()
    if line.startswith('>'):
        # Gene name is the first word after '>'
        current_gene = line[1:].split()[0]
        gene_dict[current_gene] = ''
    elif current_gene is not None:
        gene_dict[current_gene] += line

print(gene_dict)

