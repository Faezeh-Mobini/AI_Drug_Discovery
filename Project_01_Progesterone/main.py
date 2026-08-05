from rdkit import Chem
from rdkit.Chem import Descriptors

# Progesterone SMILES
smiles = "CC(=O)[C@]1(CC[C@H]2[C@@H]3CCC4=CC(=O)CC[C@]4(C)[C@H]3CC[C@]12C)C"

mol = Chem.MolFromSmiles(smiles)

print("=" * 40)
print("Progesterone Analysis")
print("=" * 40)

print("Canonical SMILES:")
print(Chem.MolToSmiles(mol))

print()

print(f"Molecular Weight : {Descriptors.MolWt(mol):.2f}")
print(f"LogP             : {Descriptors.MolLogP(mol):.2f}")
print(f"TPSA             : {Descriptors.TPSA(mol):.2f}")
print(f"H-Bond Donors    : {Descriptors.NumHDonors(mol)}")
print(f"H-Bond Acceptors : {Descriptors.NumHAcceptors(mol)}")

from rdkit.Chem import Draw

img = Draw.MolToImage(mol, size=(500, 500))
img.save("progesterone.png")

print("Structure image saved as progesterone.png")