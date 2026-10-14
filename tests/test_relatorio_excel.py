
from pathlib import Path

from openpyxl import load_workbook

from src.relatorio_excel import gerar_relatorio_excel


def test_gerar_relatorio_excel_cria_arquivo():
    gerar_relatorio_excel()

    arquivo = (
        Path(__file__).resolve().parent.parent
        / "relatorios"
        / "relatorio_auditoria.xlsx"
    )

    assert arquivo.exists()


def test_relatorio_excel_contem_colunas_esperadas():
    gerar_relatorio_excel()

    arquivo = (
        Path(__file__).resolve().parent.parent
        / "relatorios"
        / "relatorio_auditoria.xlsx"
    )

    workbook = load_workbook(arquivo, read_only=True)

    try:
        planilha = workbook.active
        colunas = [celula.value for celula in planilha[1]]

        assert "Data da auditoria" in colunas
        assert "Controle" in colunas
        assert "Risco" in colunas
        assert "Status" in colunas
        assert len(colunas) == 7
    finally:
        workbook.close()
