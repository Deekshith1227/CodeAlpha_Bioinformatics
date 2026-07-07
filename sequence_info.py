from Bio import SeqIO

record = SeqIO.read(
    "Task1_BLAST/data/EGFR_HUMAN.fasta",
    "fasta"
)

print("="*60)

print("Protein ID")
print(record.id)

print()

print("Description")
print(record.description)

print()

print("Protein Length")
print(len(record.seq))

print()

print("First 100 amino acids")
print(record.seq[:100])

print()

print("Last 100 amino acids")
print(record.seq[-100:])

print("="*60)