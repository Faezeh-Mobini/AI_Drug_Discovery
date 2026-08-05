from rdkit import Chem
from rdkit.Chem import Descriptors

# Progesterone SMILES
smiles = "CC(=O)[C@]1(CC[C@H]2[C@@H]3CCC4=CC(=O)CC[C@]4(C)[C@H]3CC[C@]12C)C"

mol = Chem.MolFromSmiles(smiles)

print("Molecule loaded successfully!")

print("Molecular Weight:", round(Descriptors.MolWt(mol), 2))
print("LogP:", round(Descriptors.MolLogP(mol), 2))
print("TPSA:", round(Descriptors.TPSA(mol), 2))