
from pathlib import Path

from src.relatorio_auditoria import gerar_relatorio


def test_gerar_relatorio_cria_arquivo():
    gerar_relatorio()

    arquivo = (
        Path(__file__).resolve().parent.parent
        / "relatorios"
        / "relatorio_auditoria.txt"
    )

    assert arquivo.exists()


def test_gerar_relatorio_contem_informacoes_de_auditoria():
    gerar_relatorio()

    arquivo = (
        Path(__file__).resolve().parent.parent
        / "relatorios"
        / "relatorio_auditoria.txt"
    )

    conteudo = arquivo.read_text(encoding="utf-8")

    assert "RELATÓRIO DE AUDITORIA ITGC" in conteudo
    assert "Data da geração:" in conteudo
