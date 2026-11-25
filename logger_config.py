"""Configuração central do sistema de logging."""

import logging
import os

# O ficheiro erros.log fica sempre na pasta do projeto,
# independentemente da pasta de onde o programa é executado.
CAMINHO_LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "erros.log")


def configurar_logger():
    """
    Cria/configura o ficheiro erros.log.
    Regista eventos informativos (INFO) e erros (ERROR).
    """
    logger = logging.getLogger("projeto_utilizadores")
    logger.setLevel(logging.INFO)

    # Evita adicionar vários handlers se a função for chamada novamente.
    if not logger.handlers:
        formato = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s",
            datefmt="%d-%m-%Y %H:%M:%S"
        )

        ficheiro = logging.FileHandler(CAMINHO_LOG, encoding="utf-8")
        ficheiro.setLevel(logging.INFO)
        ficheiro.setFormatter(formato)
        logger.addHandler(ficheiro)

    return logger
