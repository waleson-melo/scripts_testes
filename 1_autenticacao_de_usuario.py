
# Caso de Teste         | Caso Valido            | Caso Invalido
# ----------------------|------------------------|-----------------------
# Cadastro Existente    | (1) Sim                | (2) Não
# Email Valido          | (3) Sim                | (4) Não
# Campos Obrigatórios   | (5) Sim                | (6) Não

# Classe de Equivalência | Entrada       | Resultado Esperado
# -----------------------|---------------|-------------------
# Cadastro Existente     | True          | Válido
# Cadastro Existente     | False         | Inválido
# Email Valido           | "email"       | Válido
# Email Valido           | ""            | Inválido
# Campos Obrigatórios    | preenchidos   | Válido
# Campos Obrigatórios    | vazios        | Inválido

# Processo válido:
#   1, 3, 7
# Processo inválido:
#   1, 4, 8
#   2, 3, 7
#   2, 4, 8

import re


test_cases = [
    {
        "title": "Cadastro Existente - Email Válido",
        "description": "Caso de teste com usuário existente e email válido",
        "input": {
            "cadastro_existente": True,
            "email": "user@example.com"
        },
        "expected_output": "Válido"
    },
    {
        "title": "Cadastro Existente - Email Vazio",
        "description": "Caso de teste com usuário existente e email vazio",
        "input": {
            "cadastro_existente": True,
            "email": ""
        },
        "expected_output": "Inválido"
    },
    {
        "title": "Cadastro Não Existente - Email Válido",
        "description": "Caso de teste com usuário não existente e email válido",
        "input": {
            "cadastro_existente": False,
            "email": "user@example.com"
        },
        "expected_output": "Inválido"
    },
    {
        "title": "Cadastro Não Existente - Email Vazio",
        "description": "Caso de teste com usuário não existente e email vazio",
        "input": {
            "cadastro_existente": False,
            "email": ""
        },
        "expected_output": "Inválido"
    }
]


def autenticacao_usuario(cadastro_existente, email):
    if not cadastro_existente:
        return "Inválido"
    if not email:
        return "Inválido"
    if not is_valid_email(email):
        return "Inválido"
    return "Válido"

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        return False


for test_case in test_cases:
    title = test_case["title"]
    description = test_case["description"]
    input_data = test_case["input"]
    expected_output = test_case["expected_output"]

    output = autenticacao_usuario(**input_data)

    print(f"Título: {title}")
    print(f"Descrição: {description}")
    print(f"Entrada: {input_data}")
    print(f"Resultado Esperado: {expected_output}")
    print(f"Actual Output: {output}")
    print()
