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
    if instance.__len__() == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        removed_file = instance.dequeue()
        sys.stdout.write(
            "Arquivo {} removido com sucesso\n".format(
                removed_file["nome_do_arquivo"]
            )
        )


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
