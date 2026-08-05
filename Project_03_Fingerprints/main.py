from rdkit import Chem
from rdkit.Chem import rdFingerprintGenerator
from rdkit.DataStructs import TanimotoSimilarity
import pandas as pd
import matplotlib.pyplot as plt


# -------------------------------
# Molecules
# -------------------------------

# -------------------------------
# Load Molecules from CSV
# -------------------------------

molecules_df = pd.read_csv("molecules.csv")

print(molecules_df)


# -------------------------------
# Morgan Fingerprint Generator
# -------------------------------

generator = rdFingerprintGenerator.GetMorganGenerator(radius=2)


# -------------------------------
# Generate Fingerprints
# -------------------------------

fingerprints = {}














for _, row in molecules_df.iterrows():

    name = row["Name"]
    smiles = row["SMILES"]

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        print(f"Invalid SMILES: {name}")
        continue

    print(f"Valid SMILES: {name}")

    fp = generator.GetFingerprint(mol)

    fingerprints[name] = fp


# -------------------------------
# Create Similarity Matrix
# -------------------------------

similarity_matrix = {}

for name_1, fp_1 in fingerprints.items():

    similarity_matrix[name_1] = {}

    for name_2, fp_2 in fingerprints.items():

        similarity = TanimotoSimilarity(fp_1, fp_2)

        similarity_matrix[name_1][name_2] = similarity


# -------------------------------
# Convert to DataFrame
# -------------------------------

similarity_df = pd.DataFrame(similarity_matrix)

similarity_df = similarity_df.round(3)


# -------------------------------
# Display Results
# -------------------------------

print("=" * 60)

print("Molecular Similarity Matrix")

print("=" * 60)

print(similarity_df)

import matplotlib.pyplot as plt
# -------------------------------
# Visualization: Heatmap
# -------------------------------

plt.figure(figsize=(8, 6))

plt.imshow(
    similarity_df,
    cmap="viridis",
    vmin=0,
    vmax=1
)

# Add numerical values
for i in range(len(similarity_df.index)):
    for j in range(len(similarity_df.columns)):

        value = similarity_df.iloc[i, j]

        plt.text(
            j,
            i,
            f"{value:.3f}",
            ha="center",
            va="center",
            color="white"
        )

plt.colorbar(label="Tanimoto Similarity")

plt.xticks(
    range(len(similarity_df.columns)),
    similarity_df.columns,
    rotation=45
)

plt.yticks(
    range(len(similarity_df.index)),
    similarity_df.index
)

plt.title("Molecular Similarity Matrix")

plt.tight_layout()

plt.show()