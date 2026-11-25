"""Aplicação: Gestão de Utilizadores + Calculadora Segura."""

import math

from calculadora import calcular
from excecoes import NomeInvalido, EmailInvalido, OperacaoInvalida
from logger_config import configurar_logger
from validacoes import validar_nome, validar_email


logger = configurar_logger()


def ler_numero(mensagem):
    """Lê um número real. Lança ValueError se o valor não for numérico."""
    valor = float(input(mensagem))

    # float() aceita 'nan' e 'inf', que não são números utilizáveis aqui.
    if not math.isfinite(valor):
        raise ValueError(f"valor não finito: {valor}")

    return valor


def registar_utilizador():
    """Pede e valida o nome e o email do utilizador."""
    print("\n--- REGISTO DE UTILIZADOR ---")

    try:
        nome = validar_nome(input("Introduza o seu nome: "))
        email = validar_email(input("Introduza o seu email: "))

        utilizador = {"nome": nome, "email": email}
        logger.info("Utilizador registado com sucesso: %s (%s)", nome, email)
        print("\nRegisto efetuado com sucesso!")
        return utilizador

    except NomeInvalido as erro:
        logger.error("Erro no registo - nome inválido: %s", erro)
        print(f"\nNão foi possível efetuar o registo: {erro}")

    except EmailInvalido as erro:
        logger.error("Erro no registo - email inválido: %s", erro)
        print(f"\nNão foi possível efetuar o registo: {erro}")

    except ValueError as erro:
        logger.error("Erro ao receber dados do registo: %s", erro)
        print("\nOcorreu um erro na introdução dos dados.")

    # EOFError e KeyboardInterrupt não são apanhados aqui de propósito:
    # sobem até ao menu(), que termina a aplicação em segurança.
    return None


def fazer_calculo():
    """Pede os valores e a operação, tratando os erros possíveis."""
    print("\n--- CALCULADORA SEGURA ---")
    print("Operações disponíveis: +  -  *  /")

    try:
        numero1 = ler_numero("Introduza o primeiro número: ")
        numero2 = ler_numero("Introduza o segundo número: ")
        operacao = input("Escolha a operação (+, -, *, /): ").strip()

        resultado = calcular(numero1, numero2, operacao)

        print(f"\nResultado: {numero1:g} {operacao} {numero2:g} = {resultado:g}")
        logger.info(
            "Operação realizada: %g %s %g = %g",
            numero1, operacao, numero2, resultado
        )

    except ValueError as erro:
        logger.error("Input numérico inválido na calculadora: %s", erro)
        print("\nErro: deve introduzir valores numéricos válidos.")

    except ZeroDivisionError as erro:
        logger.error("Tentativa de divisão por zero: %s", erro)
        print("\nErro: não é possível dividir um número por zero.")

    except OperacaoInvalida as erro:
        logger.error("Operação inválida: %s", erro)
        print(f"\nErro: {erro}")

    except (EOFError, KeyboardInterrupt):
        logger.error("Introdução de dados interrompida na calculadora.")
        print("\nOperação cancelada.")


def mostrar_utilizador(utilizador):
    """Mostra os dados do utilizador atualmente registado."""
    print("\n--- UTILIZADOR ATUAL ---")
    print(f"Nome: {utilizador['nome']}")
    print(f"Email: {utilizador['email']}")


def menu():
    """Controla o fluxo principal da aplicação."""
    utilizador = None

    print("=" * 45)
    print(" GESTÃO DE UTILIZADORES + CALCULADORA SEGURA")
    print("=" * 45)

    # O utilizador tem de se registar antes de poder usar a calculadora.
    try:
        while utilizador is None:
            utilizador = registar_utilizador()
            if utilizador is None:
                print("Tente novamente. O registo é obrigatório.")
    except (EOFError, KeyboardInterrupt):
        logger.info("Aplicação terminada antes de concluir o registo.")
        print("\nAplicação terminada.")
        return

    logger.info("Aplicação iniciada para o utilizador %s", utilizador["nome"])

    while True:
        print("\n========== MENU PRINCIPAL ==========")
        print("1 - Registar Utilizador")
        print("2 - Fazer Cálculo")
        print("3 - Ver Utilizador Atual")
        print("0 - Sair")
        print("====================================")

        try:
            opcao = input("Escolha uma opção: ").strip()

            if opcao == "1":
                novo_utilizador = registar_utilizador()
                if novo_utilizador is not None:
                    utilizador = novo_utilizador
                    logger.info(
                        "Utilizador atual alterado para %s", utilizador["nome"]
                    )

            elif opcao == "2":
                fazer_calculo()

            elif opcao == "3":
                mostrar_utilizador(utilizador)

            elif opcao == "0":
                logger.info(
                    "Aplicação terminada pelo utilizador %s", utilizador["nome"]
                )
                print("\nObrigado por utilizar a aplicação. Até breve!")
                break

            else:
                raise ValueError("A opção escolhida não existe.")

        except ValueError as erro:
            logger.error("Opção de menu inválida: %s", erro)
            print("\nOpção inválida. Escolha 1, 2, 3 ou 0.")

        except (EOFError, KeyboardInterrupt):
            logger.info("Aplicação terminada pelo teclado.")
            print("\nAplicação terminada.")
            break


if __name__ == "__main__":
    menu()
