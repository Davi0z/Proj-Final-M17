"""Exceções personalizadas do projeto."""


class NomeInvalido(Exception):
    """Erro quando o nome não respeita as regras de validação."""


class EmailInvalido(Exception):
    """Erro quando o email não respeita as regras de validação."""


class OperacaoInvalida(Exception):
    """Erro quando é escolhida uma operação não suportada."""
