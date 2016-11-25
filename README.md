# pdb-transform
Apply transformation matrix to a PDB file

# dependencies
All dependencies are listed in the requirements.txt file.
To install them run:

`pip install -r requirements.txt`

# usage:
`python pdb_transform.py -pdb pdb_path -mat trans_matrix_path -out output_pdb_path`

# input format
CSV, first three lines are rotation vectors (x, y, and z, respectively) and
the fourth line is a translation vector
