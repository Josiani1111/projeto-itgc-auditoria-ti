
usuarios = [
    {
        "nome": "Ana",
        "cargo": "Financeiro",
        "status_funcionario": "Ativo",
        "acesso_sistema": True
    },
    {
        "nome": "Carlos",
        "cargo": "Suporte de TI",
        "status_funcionario": "Desligado",
        "acesso_sistema": True
    },
    {
        "nome": "Maria",
        "cargo": "RH",
        "status_funcionario": "Ativo",
        "acesso_sistema": True
    }
]


def verificar_acessos(usuarios):
    alertas = []

    for usuario in usuarios:
        if (
            usuario["status_funcionario"] == "Desligado"
            and usuario["acesso_sistema"] is True
        ):
            alertas.append(
                f"ALERTA: {usuario['nome']} está desligado, "
                "mas ainda possui acesso ao sistema."
            )

    return alertas


if __name__ == "__main__":
    resultado = verificar_acessos(usuarios)

    print("RELATÓRIO DE CONTROLE DE ACESSO")
    print("-" * 40)

    if resultado:
        for alerta in resultado:
            print(alerta)
    else:
        print("Nenhum problema de acesso identificado.")
