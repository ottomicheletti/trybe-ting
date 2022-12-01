# from ting_file_management.queue import Queue
from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    imported_text = txt_importer(path_file)

    data = {
        "nome_do_arquivo": f"{path_file}",
        "qtd_linhas": len(imported_text),
        "linhas_do_arquivo": imported_text,
    }

    if data in instance.queue:
        return None

    instance.enqueue(data)
    sys.stdout.write(str(data))


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
