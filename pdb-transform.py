import argparse
import copy

from Bio import PDB


def parse_matrix(matrix_path):
    """
    Parses transformation matrix file
    file format: csv, first three lines are rotation vectors (x, y, and z, respectively)
        fourth line is a translation vector

    :return: transformation dict
        {
        'rotation': [
            x rotation vector (list),
            y rotation vector (list),
            z rotation vector (list)
        ],
        'translation': translation vector (list)
        }
    """
    with open(matrix_path) as a:
        matrix_lines = a.read().splitlines()

    # split up lines and convert values to floats
    matrix = map(lambda x: map(float, x.split(',')), matrix_lines)

    matrix_dict = {
        'rotation': [matrix[0], matrix[1], matrix[2]],
        'translation': matrix[3]
    }
    return matrix_dict


def parse_pdb_file(pdb_path):
    """
    :param pdb_path:
    :return: biopython's structure object
    """
    parser = PDB.PDBParser()
    strct_name = pdb_path.split('.')[0]
    structure = parser.get_structure(strct_name, pdb_path)
    return structure


def write_pdb_file(structure, output_path):
    """
    :param structure: biopython's structure object
    :param output_path:
    """
    io = PDB.PDBIO()
    io.set_structure(structure)
    io.save(output_path)
    return output_path


def apply_transformation(structure, matrix):
    """
    Transforms structure based on the transformation matrix
    :param structure: biopython's structure object
    :param matrix: transformation matrix dict
    :return: transformed structure
    """
    # Atom.transform has a side effect, without a return value, so performing a deepcopy
    # allows to return a transformed copy, instead of returning the same object.
    
    structure = copy.deepcopy(structure)
    # rotation = np.asmatrix(np.array(matrix['rotation']))
    rotation = matrix['rotation']
    # translation = np.array(matrix['translation'])
    translation = matrix['translation']

    # apply transformation to each atom
    for atom in structure.get_atoms():
        atom.transform(rotation, translation)
    
    return structure


def pdb_transform(pdb_path, matrix_path, output_path):
    """
    Applies transformation matrix to the PDB file and writes the new PDB to file
    :param pdb_path: path to the input PDB file
    :param matrix_path: path to the transformation matrix file
    :param output_path: path to the output PDB file
    """
    matrix = parse_matrix(matrix_path)
    structure = parse_pdb_file(pdb_path)

    structure = apply_transformation(structure, matrix)

    write_pdb_file(structure, output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("-pdb")
    parser.add_argument("-mat")
    parser.add_argument("-out")

    args = parser.parse_args()

    pdb_transform(args.pdb, args.mat, args.out)
