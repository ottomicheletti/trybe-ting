import sys
import os


def txt_importer(path_file):
    if not os.path.isfile(path_file):
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")

    _, file_extension = os.path.splitext(path_file)

    if file_extension != ".txt":
        return sys.stderr.write("Formato inválido\n")

    with open(path_file) as txt_file:
        lines = [line.strip() for line in txt_file.readlines()]
        return lines
