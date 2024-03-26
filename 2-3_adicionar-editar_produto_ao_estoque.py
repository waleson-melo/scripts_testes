
# Caso de Teste         | Caso Valido                                           |  Caso Invalido
# ----------------------|-------------------------------------------------------|-----------------------
# Acesso à Tela         | (1) Sim                                               | (2) Não
# Campos Obrigatórios   | (3) Sim                                               | (4) Não
# Nome do Produto       | (5) Caracteres alfanumericos e menos de 50 caracteres | (6) Não
# Quantidade em Estoque | (7) Número inteiro positivo maior que zero            | (8) Não


# Classe de Equivalência | Entrada       | Resultado Esperado
# -----------------------|---------------|-------------------
# Acesso à Tela          | Presente      | Válido
# Acesso à Tela          | Ausente       | Inválido
# Campos Obrigatórios    | Preenchidos   | Válido
# Campos Obrigatórios    | Vazios        | Inválido
# Nome do Produto        | Válido        | Válido
# Nome do Produto        | Inválido      | Inválido
# Quantidade em Estoque  | Válida        | Válido
# Quantidade em Estoque  | Inválida      | Inválido
# Valor Unitário         | Válido        | Válido
# Valor Unitário         | Inválido      | Inválido

# Processo válido:
#   1, 3, 5, 7
# Processo inválido:
#   1, 4, 6, 8
#   1, 3, 6, 8
#   1, 3, 6, 8
#   2, 3, 5, 7
#   2, ...

import re


test_cases = [
    {
        "title": "Acesso à Tela - Acesso à Tela Permitido",
        "description": "Caso de teste com usuário com acesso à tela",
        "input": {
            "acesso_a_tela": True,
            "campos_obrigatorios": True,
            "nome_do_produto": "Produto 1",
            "quantidade_em_estoque": 10,
        },
        "expected_output": "Válido"
    },
    {
        "title": "Campos Obrigatórios - Campos Obrigatórios não Preenchidos",
        "description": "Caso de teste com campos obrigatórios não preenchidos",
        "input": {
            "acesso_a_tela": True,
            "campos_obrigatorios": False,
            "nome_do_produto": "@Produto 1",
            "quantidade_em_estoque": 0,
        },
        "expected_output": "Inválido"
    },
    {
        "title": "Campos Obrigatórios - Campos Obrigatórios Preenchidos",
        "description": "Caso de teste com campos obrigatórios Preenchidos",
        "input": {
            "acesso_a_tela": True,
            "campos_obrigatorios": True,
            "nome_do_produto": "Produto/ 1",
            "quantidade_em_estoque": -1,
        },
        "expected_output": "Inválido"
    },
    {
        "title": "Nome do Produto - Sem acesso a tela",
        "description": "Caso de teste com nome do produto válido",
        "input": {
            "acesso_a_tela": False,
            "campos_obrigatorios": True,
            "restricoes_de_entrada": True,
            "nome_do_produto": "Prod,uto 1",
            "quantidade_em_estoque": -5,
        },
        "expected_output": "Inválido"
    },
]

def adicionar_produto_ao_estoque(acesso_a_tela, campos_obrigatorios, nome_do_produto, quantidade_em_estoque):
    if not acesso_a_tela:
        return "Inválido"
    if not campos_obrigatorios:
        return "Inválido"
    if not re.match("^[a-zA-Z0-9\s]+$", nome_do_produto):
        return "Inválido"
    if quantidade_em_estoque < 1:
        return "Inválido"
    return "Válido"

for i, caso in enumerate(test_cases, start=1):
    resultado = adicionar_produto_ao_estoque(acesso_a_tela=caso["input"]["acesso_a_tela"],
                                            campos_obrigatorios=caso["input"]["campos_obrigatorios"],
                                            nome_do_produto=caso["input"]["nome_do_produto"],
                                            quantidade_em_estoque=caso["input"]["quantidade_em_estoque"])
    if resultado == caso["expected_output"]:
        print("Caso de teste N°{}: {}, passou".format(i, caso["title"]))
    else:
        print("Caso de teste N°{}: {}, não passou".format(i, caso["title"]))
        print("Resultado esperado: {}".format(caso["expected_output"]))
        print("Resultado obtido: {}".format(resultado))
        print()
