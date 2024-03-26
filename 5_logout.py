
# Caso de Teste               | Caso Valido            | Caso Invalido
# ----------------------------|------------------------|-----------------------
# CLicar em Logout            | (1) Sim                | (2) Não
# Confirmação de Logout       | (3) Sim                | (4) Não
# Encerramento da Sessão      | (5) Sim                | (6) Não
# Limpeza de Dados            | (7) Sim                | (8) Não
# Redirecionamento pós Logout | (9) Sim                | (10) Não

# Classe de Equivalência      | Entrada             | Resultado Esperado
# ----------------------------|---------------------|-------------------
# CLicar em Logout            | Sim                 | Válido
# CLicar em Logout            | Não                 | Inválido
# Confirmação de Logout       | Confirmado          | Válido
# Confirmação de Logout       | Não confirmado      | Inválido
# Encerramento da Sessão      | Sessão encerrada    | Válido
# Encerramento da Sessão      | Sessão não encerrada| Inválido
# Limpeza de Dados            | Dados limpos        | Válido
# Limpeza de Dados            | Dados não limpos    | Inválido
# Redirecionamento pós Logout | Redirecionado       | Válido
# Redirecionamento pós Logout | Não redirecionado   | Inválido

# Processo válido:
#   1, 3, 5, 7, 9
# Processo inválido:
#   1, 4, 6, 8, 10
#   1, 3, 6, 8, 10
#   1, 3, 5, 8, 10
#   1, 3, 5, 7, 10
#   1, 3, 5, 7, 9
#   1, 4, 6, 8, 10
#   2, 4, 6, 8, 10
#   2, ...

import re


test_cases = [
    {
        "title": "CLicar em Logout - Logout Confirmado",
        "description": "Caso de teste com logout confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": True,
            "encerramento_da_sessao": True,
            "limpeza_de_dados": True,
            "redirecionamento_pos_logout": True
        },
        "expected_output": "Válido"
    },
    {
        "title": "CLicar em Logout - Logout Não Confirmado",
        "description": "Caso de teste com logout não confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": False,
            "encerramento_da_sessao": False,
            "limpeza_de_dados": False,
            "redirecionamento_pos_logout": False
        },
        "expected_output": "Inválido"
    },
    {
        "title": "CLicar em Logout - Logout Confirmado",
        "description": "Caso de teste com logout confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": True,
            "encerramento_da_sessao": True,
            "limpeza_de_dados": True,
            "redirecionamento_pos_logout": True
        },
        "expected_output": "Válido"
    },
    {
        "title": "CLicar em Logout - Logout Não Confirmado",
        "description": "Caso de teste com logout não confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": False,
            "encerramento_da_sessao": False,
            "limpeza_de_dados": False,
            "redirecionamento_pos_logout": False
        },
        "expected_output": "Inválido"
    },
    {
        "title": "CLicar em Logout - Logout Confirmado",
        "description": "Caso de teste com logout confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": True,
            "encerramento_da_sessao": True,
            "limpeza_de_dados": True,
            "redirecionamento_pos_logout": True
        },
        "expected_output": "Válido"
    },
    {
        "title": "CLicar em Logout - Logout Não Confirmado",
        "description": "Caso de teste com logout não confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": False,
            "encerramento_da_sessao": False,
            "limpeza_de_dados": False,
            "redirecionamento_pos_logout": False
        },
        "expected_output": "Inválido"
    },
    {
        "title": "CLicar em Logout - Logout Confirmado",
        "description": "Caso de teste com logout confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": True,
            "encerramento_da_sessao": True,
            "limpeza_de_dados": True,
            "redirecionamento_pos_logout": True
        },
        "expected_output": "Válido"
    },
    {
        "title": "CLicar em Logout - Logout Não Confirmado",
        "description": "Caso de teste com logout não confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": False,
            "encerramento_da_sessao": False,
            "limpeza_de_dados": False,
            "redirecionamento_pos_logout": False
        },
        "expected_output": "Inválido"
    },
    {
        "title": "CLicar em Logout - Logout Confirmado",
        "description": "Caso de teste com logout confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": True,
            "encerramento_da_sessao": True,
            "limpeza_de_dados": True,
            "redirecionamento_pos_logout": True
        },
        "expected_output": "Válido"
    },
    {
        "title": "CLicar em Logout - Logout Não Confirmado",
        "description": "Caso de teste com logout não confirmado",
        "input": {
            "clicar_em_logout": True,
            "confirmacao_de_logout": False,
            "encerramento_da_sessao": False,
            "limpeza_de_dados": False,
            "redirecionamento_pos_logout": False
        },
        "expected_output": "Inválido"
    }
]

def logout(clicar_em_logout, confirmacao_de_logout, encerramento_da_sessao, limpeza_de_dados, redirecionamento_pos_logout):
    if clicar_em_logout:
        if confirmacao_de_logout:
            if encerramento_da_sessao:
                if limpeza_de_dados:
                    if redirecionamento_pos_logout:
                        return "Válido"
                    else:
                        return "Inválido"
                else:
                    return "Inválido"
            else:
                return "Inválido"
        else:
            return "Inválido"
    else:
        return "Inválido"

for i, caso in enumerate(test_cases, start=1):
    resultado = logout(clicar_em_logout=caso["input"]["clicar_em_logout"],
                        confirmacao_de_logout=caso["input"]["confirmacao_de_logout"],
                        encerramento_da_sessao=caso["input"]["encerramento_da_sessao"],
                        limpeza_de_dados=caso["input"]["limpeza_de_dados"],
                        redirecionamento_pos_logout=caso["input"]["redirecionamento_pos_logout"])
    print(f"Teste {i}")
    print(f"Resultado: {resultado}")
    print(f"Esperado: {caso['expected_output']}")
    print()
    assert resultado == caso["expected_output"]
print("Todos os testes passaram")
