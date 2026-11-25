"""Operações matemáticas da calculadora segura."""

from excecoes import OperacaoInvalida


def calcular(numero1, numero2, operacao):
    """
    Executa uma das quatro operações permitidas.
    Devolve o resultado ou lança uma exceção adequada.
    """
    if operacao == "+":
        return numero1 + numero2
    elif operacao == "-":
        return numero1 - numero2
    elif operacao == "*":
        return numero1 * numero2
    elif operacao == "/":
        if numero2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        return numero1 / numero2
    else:
        raise OperacaoInvalida(
            "Operação inválida. Escolha +, -, * ou /."
        )
