
from src.controle_acesso import verificar_acessos


def test_identifica_usuario_desligado_com_acesso():
    usuarios = [
        {
            "nome": "Carlos",
            "cargo": "Suporte de TI",
            "status_funcionario": "Desligado",
            "acesso_sistema": True
        }
    ]

    alertas = verificar_acessos(usuarios)

    assert len(alertas) == 1
    assert "Carlos" in alertas[0]


def test_nao_alerta_usuario_ativo():
    usuarios = [
        {
            "nome": "Ana",
            "cargo": "Financeiro",
            "status_funcionario": "Ativo",
            "acesso_sistema": True
        }
    ]

    alertas = verificar_acessos(usuarios)

    assert alertas == []


def test_nao_alerta_usuario_desligado_sem_acesso():
    usuarios = [
        {
            "nome": "Maria",
            "cargo": "RH",
            "status_funcionario": "Desligado",
            "acesso_sistema": False
        }
    ]

    alertas = verificar_acessos(usuarios)

    assert alertas == []
