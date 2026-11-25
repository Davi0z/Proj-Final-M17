"""Funções de validação dos dados do utilizador."""

from excecoes import NomeInvalido, EmailInvalido


def validar_nome(nome):
    """
    Valida o nome:
    - tem pelo menos 3 caracteres;
    - não contém dígitos.
    """
    nome = nome.strip()

    if len(nome) < 3:
        raise NomeInvalido("O nome deve ter pelo menos 3 caracteres.")

    if any(caractere.isdigit() for caractere in nome):
        raise NomeInvalido("O nome não pode conter números.")

    return nome


def validar_email(email):
    """
    Valida o email de acordo com o enunciado:
    deve conter '@' e '.'.
    """
    email = email.strip()

    if "@" not in email or "." not in email:
        raise EmailInvalido("O email deve conter os caracteres '@' e '.'.")

    if " " in email:
        raise EmailInvalido("O email não pode conter espaços.")

    if email.startswith("@") or email.endswith("@"):
        raise EmailInvalido("O email não tem um formato válido.")

    if email.startswith(".") or email.endswith("."):
        raise EmailInvalido("O email não tem um formato válido.")

    if email.index("@") > email.rfind("."):
        raise EmailInvalido("O email não tem um formato válido.")

    return email
