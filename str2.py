import streamlit as st
from rdkit import Chem
from rdkit.Chem import EnumerateStereoisomers, Draw
from PIL import Image

# Streamlit page configuration
st.set_page_config(page_title="Molecule Stereoisomer Viewer")

# Title
st.title("Molecule Stereoisomer Viewer")

# User input for SMILES string
user_smiles = st.text_input("Enter a SMILES string:", 'CC(C(N)C(O)=O)C')

# Convert SMILES to molecule
molecule = Chem.MolFromSmiles(user_smiles)

# Check if the molecule is valid
if molecule:
    # Display the original molecule
    st.subheader("Original Molecule")
    orig_mol_image = Draw.MolToImage(molecule)
    st.image(orig_mol_image, use_column_width=True)

    # Options for stereo enumeration
    options = EnumerateStereoisomers.StereoEnumerationOptions(unique=True, tryEmbedding=True)

    # Generate stereoisomers
    isomers = tuple(EnumerateStereoisomers.EnumerateStereoisomers(molecule, options=options))

    # Display isomers
    st.subheader("Stereoisomers")
    for idx, isomer in enumerate(isomers):
        st.text(f"Stereoisomer {idx+1}: {Chem.MolToSmiles(isomer, isomericSmiles=True)}")
        isomer_image = Draw.MolToImage(isomer)
        st.image(isomer_image, use_column_width=True)
else:
    st.error("Invalid SMILES string. Please enter a valid SMILES.")
