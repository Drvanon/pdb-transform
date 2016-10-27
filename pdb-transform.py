import argparse

from Bio import PDB


def parse_matrix(matrix_path):
    """
    Parses transformation matrix file
    file format: csv, first three lines are translation vectors (x, y, and z, respectively)
        fourth line is a rotation vector

    :return: transformation dict
        {
        'translation': {
            'x': x translation vector (list),
            'y': y translation vector (list),
            'z': z translation vector (list)
        },
        'rotation': rotation vector (list)
        }
    """
    pass


def parse_pdb_file(pdb_path):
    """
    :param pdb_path:
    :return: biopython's structure object
    """
    pass


def write_pdb_file(structure, output_path):
    """
    :param structure: biopython's structure object
    :param output_path:
    """
    pass


def apply_transformation(structure, matrix):
    """
    Transforms structure based on the transformation matrix
    :param structure: biopython's structure object
    :param matrix: transformation matrix dict
    :return: transformed structure
    """
    pass


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
