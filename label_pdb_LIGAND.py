import requests
import pandas as pd
import numpy as np


#functions to download a biological assembly, save it, and modify it and save it

#download 1st biological assembly based on pdb code
def get_pdb1_data(pdb_code):
    url = f'https://files.rcsb.org/view/{pdb_code}.pdb1'
    response = requests.get(url, allow_redirects=True)
    return(response)

#save 1st biological assembly without changes create a txt file for save_LIGAND_modified_pdb1(pdb_code, ligand_code)
def save_unmodified_pdb1(pdb_code):
    pdb_data = get_pdb1_data(pdb_code)

    file_pdb = open(f'{pdb_code}.pdb', 'wb')
    print('pdb file open')
    file_pdb.write(pdb_data.content)
    file_pdb.close()
    print('pdb file closed')

    file_text = open(f'{pdb_code}.txt', 'wb')
    print('text file opened')
    file_text.write(pdb_data.content)
    file_text.close()
    print('text file closed')

#save 1st biological assembly with HETATM changed to LIGAND
#assume you already have the txt file saved by save_unmodified_pdb1(pdb_code)

def save_LIGAND_modified_pdb1(pdb_code, ligand_code):
    pdb_data = open(f'{pdb_code}.txt', 'r')
    new_file = open(f'{pdb_code}_LIGAND.pdb', 'w')
    for line in pdb_data:
        if 'HETATM' and ligand_code in line:
            new_line = line.replace('HETATM', 'LIGAND')
            new_file.write(new_line)
        else:
            new_file.write(line)
    new_file.close()
    pdb_data.close()

#load pdb_refined as a DataFrame.  Change path to match path on your machine.
path = '/home/johann/space_traders/pdb_refined_091824.csv'
df_pdb_refined = pd.read_csv(path)

#make two lists: one with pdb codes and one with ligand codes
pdb_codes = df_pdb_refined['PDB code'].to_list()
ligand_codes = df_pdb_refined['Ligand Name'].to_list()

#primary loop.  Output files will be saved in same folder as program.
def main():
    for pdb_code, ligand_code in zip(pdb_codes, ligand_codes):
        save_unmodified_pdb1(pdb_code)
        save_LIGAND_modified_pdb1(pdb_code, ligand_code)

main()

