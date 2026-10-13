
from pathlib import Path

from src.relatorio_auditoria import gerar_relatorio


def test_relatorio_registra_falha_e_risco():
    gerar_relatorio()

    arquivo = (
        Path(__file__).resolve().parent.parent
        / "relatorios"
        / "relatorio_auditoria.txt"
    )

    conteudo = arquivo.read_text(encoding="utf-8")

    assert "RELATORIO DE AUDITORIA ITGC" in conteudo
    assert "Carlos" in conteudo
    assert "RISCO:" in conteudo
    assert "ACAO RECOMENDADA:" in conteudo


def test_relatorio_registra_evidencias_e_status():
    gerar_relatorio()

    arquivo = (
        Path(__file__).resolve().parent.parent
        / "relatorios"
        / "relatorio_auditoria.txt"
    )

    conteudo = arquivo.read_text(encoding="utf-8")

    assert "EVIDENCIAS NECESSARIAS:" in conteudo
    assert "STATUS: Pendente de verificacao." in conteudo
