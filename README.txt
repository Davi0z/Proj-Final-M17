PROJETO - GESTÃO DE UTILIZADORES + CALCULADORA SEGURA
Módulo 17_OP2 - Python

1. FICHEIROS
- main.py: menu e fluxo principal da aplicação.
- validacoes.py: validação do nome e do email.
- excecoes.py: exceções personalizadas.
- calculadora.py: operações matemáticas.
- logger_config.py: configuração do logging.
- erros.log: é criado automaticamente quando a aplicação é executada.

2. COMO EXECUTAR
1) Extraia todos os ficheiros para a mesma pasta.
2) Abra essa pasta no Visual Studio Code, IDLE ou terminal.
3) Execute:
   python main.py

3. COMO FUNCIONA
- O registo é obrigatório antes de aceder à calculadora.
- O nome deve ter pelo menos 3 caracteres e não pode conter dígitos.
- O email deve conter '@' e '.' e não pode ter espaços.
- A calculadora permite soma (+), subtração (-), multiplicação (*) e divisão (/).
- O programa trata valores não numéricos, divisão por zero e operações inválidas.
- Os eventos e erros são guardados automaticamente em erros.log (na pasta do projeto).
- Ctrl+C / Ctrl+D terminam a aplicação em segurança, mesmo antes do registo.

4. TESTES SUGERIDOS
- Nome: Ana -> válido.
- Nome: A1a -> inválido.
- Nome: Al -> inválido.
- Email: ana@email.com -> válido.
- Email: anaemail.com -> inválido.
- Cálculo: 10 / 2 -> resultado 5.
- Cálculo: 10 / 0 -> mensagem de erro, sem terminar o programa.
- Cálculo com texto em vez de número -> mensagem de erro.
- Operação % -> operação inválida.
- Número 'nan' ou 'inf' -> mensagem de erro.
- Email com espaços -> inválido.

Nota: erros.log é criado na pasta do projeto quando executar main.py.
