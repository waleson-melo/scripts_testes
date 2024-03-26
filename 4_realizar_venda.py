
# Caso de Teste         | Caso Valido            | Caso Invalido
# ----------------------|------------------------|-----------------------
# Acesso à Tela         | (1) Sim                | (2) Não
# Seleção de Produtos   | (3) Sim                | (4) Não
# Adição à Lista        | (5) Sim                | (6) Não
# Seleção do Pagamento  | (7) Sim                | (8) Não
# Cancelamento da Venda | (9) Sim                | (10) Não
# Finalização da Venda  | (11) Sim               | (12) Não

# Classe de Equivalência | Entrada              | Resultado Esperado
# -----------------------|----------------------|-------------------
# Acesso à Tela          | Presente             | Válido
# Acesso à Tela          | Ausente              | Inválido
# Seleção de Produtos    | Produto válido       | Válido
# Seleção de Produtos    | Produto inválido     | Inválido
# Adição à Lista         | Adição válida        | Válido
# Adição à Lista         | Adição inválida      | Inválido
# Seleção do Pagamento   | Método válido        | Válido
# Seleção do Pagamento   | Método inválido      | Inválido
# Cancelamento da Venda  | Cancelamento válido  | Válido
# Cancelamento da Venda  | Cancelamento inválido| Inválido
# Finalização da Venda   | Finalização válida   | Válido
# Finalização da Venda   | Finalização inválida | Inválido

# Processo válido:
#   1, 3, 5, 7, 9, 11
# Processo inválido:
#   1, 4, 6, 8, 10, 12
#   1, 3, 6, 8, 10, 12
#   1, 3, 5, 8, 10, 12
#   1, 3, 5, 7, 10, 12
#   1, 3, 5, 7, 9, 12
#   1, 3, 5, 7, 9, 11
#   1, 4, 6, 8, 10, 12
#   1, 4, 6, 8, 9, 12
#   2, 4, 6, 8, 10, 12
#   2, ...

import re


test_cases = [
    {
        "title": "Acesso à Tela - Acesso à Tela Permitido",
        "description": "Caso de teste com usuário com acesso à tela",
        "input": {
            "acesso_a_tela": True,
            "selecao_de_produtos": "Produto 1",
            "adicao_a_lista": True,
            "selecao_do_pagamento": "Dinheiro",
            "cancelamento_da_venda": True,
            "finalizacao_da_venda": True
        },
        "expected_output": "Válido"
    },
    {
        "title": "Seleção de Produtos - Produto Inválido",
        "description": "Caso de teste com produto inválido",
        "input": {
            "acesso_a_tela": True,
            "selecao_de_produtos": "Produto 1",
            "adicao_a_lista": True,
            "selecao_do_pagamento": "Dinheiro",
            "cancelamento_da_venda": True,
            "finalizacao_da_venda": True
        },
        "expected_output": "Inválido"
    },
    {
        "title": "Adição à Lista - Adição Inválida",
        "description": "Caso de teste com adição inválida",
        "input": {
            "acesso_a_tela": True,
            "selecao_de_produtos": "Produto 1",
            "adicao_a_lista": False,
            "selecao_do_pagamento": "Dinheiro",
            "cancelamento_da_venda": True,
            "finalizacao_da_venda": True
        },
        "expected_output": "Inválido"
    },
    {
        "title": "Seleção do Pagamento - Método Inválido",
        "description": "Caso de teste com método de pagamento inválido",
        "input": {
            "acesso_a_tela": True,
            "selecao_de_produtos": "Produto 1",
            "adicao_a_lista": True,
            "selecao_do_pagamento": "Dinheiro",
            "cancelamento_da_venda": True,
            "finalizacao_da_venda": True
        },
        "expected_output": "Inválido"
    },
    {
        "title": "Cancelamento da Venda - Cancelamento Inválido",
        "description": "Caso de teste com cancelamento inválido",
        "input": {
            "acesso_a_tela": True,
            "selecao_de_produtos": "Produto 1",
            "adicao_a_lista": True,
            "selecao_do_pagamento": "Dinheiro",
            "cancelamento_da_venda": False,
            "finalizacao_da_venda": True
        },
        "expected_output": "Inválido"
    }
]

def realizar_venda(acesso_a_tela, selecao_de_produtos, adicao_a_lista, selecao_do_pagamento, cancelamento_da_venda, finalizacao_da_venda):
    if not acesso_a_tela:
        return "Inválido"
    if not selecao_de_produtos:
        return "Inválido"
    if not adicao_a_lista:
        return "Inválido"
    if not selecao_do_pagamento:
        return "Inválido"
    if not cancelamento_da_venda:
        return "Inválido"
    if not finalizacao_da_venda:
        return "Inválido"
    return "Válido"

for i, test_case in enumerate(test_cases):
    resultado = realizar_venda(acesso_a_tela=test_case["input"]["acesso_a_tela"],
                                selecao_de_produtos=test_case["input"]["selecao_de_produtos"],
                                adicao_a_lista=test_case["input"]["adicao_a_lista"],
                                selecao_do_pagamento=test_case["input"]["selecao_do_pagamento"],
                                cancelamento_da_venda=test_case["input"]["cancelamento_da_venda"],
                                finalizacao_da_venda=test_case["input"]["finalizacao_da_venda"])

    print(f"Test Case {i+1}: {test_case['title']} - {'Falhou' if resultado != test_case['expected_output'] else 'Passou'}")
