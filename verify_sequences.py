from Bio import SeqIO
import os

folder = "Task2_MSA/sequences"

print("="*70)
print("EGFR Sequence Verification")
print("="*70)

for file in sorted(os.listdir(folder)):
    if file.endswith(".fasta"):
        record = SeqIO.read(os.path.join(folder, file), "fasta")

        print(f"\nFile      : {file}")
        print(f"Species   : {record.description}")
        print(f"Length    : {len(record.seq)} aa")
        print(f"First 10  : {record.seq[:10]}")
        print(f"Last 10   : {record.seq[-10:]}")

print("\nVerification Complete")