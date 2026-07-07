from Bio import SeqIO
from Bio.SeqUtils import molecular_weight

record = SeqIO.read("Task1_BLAST/data/EGFR_HUMAN.fasta", "fasta")
sequence = str(record.seq)

length = len(sequence)

mw = molecular_weight(sequence, seq_type="protein")

aa_list = [
    "A","R","N","D","C","Q","E","G","H","I",
    "L","K","M","F","P","S","T","W","Y","V"
]

print("="*60)
print("EGFR Protein Statistics")
print("="*60)

print(f"Protein ID       : {record.id}")
print(f"Protein Length   : {length} amino acids")
print(f"Molecular Weight : {mw:.2f} Da")

print("\nAmino Acid Composition")
print("-"*60)

for aa in aa_list:
    count = sequence.count(aa)
    percent = (count / length) * 100
    print(f"{aa:2} : {count:4} ({percent:5.2f}%)")

print("="*60)