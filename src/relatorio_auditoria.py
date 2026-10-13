
from datetime import datetime
from pathlib import Path

from src.controle_acesso import verificar_acessos, usuarios


def gerar_relatorio():
    alertas = verificar_acessos(usuarios)

    pasta_relatorios = Path(__file__).resolve().parent.parent / "relatorios"
    pasta_relatorios.mkdir(parents=True, exist_ok=True)

    arquivo = pasta_relatorios / "relatorio_auditoria.txt"

    with arquivo.open("w", encoding="utf-8") as relatorio:
        relatorio.write("RELATORIO DE AUDITORIA ITGC\n")
        relatorio.write("=" * 40 + "\n")
        relatorio.write(
            f"Data da geracao: {datetime.now():%d/%m/%Y %H:%M}\n\n"
        )

        if not alertas:
            relatorio.write("Nenhuma falha de acesso identificada.\n")

        for alerta in alertas:
            relatorio.write("CONTROLE: Gestao de acessos\n")
            relatorio.write(f"FALHA: {alerta}\n")
            relatorio.write(
                "RISCO: Acesso nao autorizado a sistemas e dados.\n"
            )
            relatorio.write(
                "ACAO RECOMENDADA: Solicitar a desativacao do acesso "
                "e confirmar a execucao.\n"
            )
            relatorio.write(
                "EVIDENCIAS NECESSARIAS: Registro da solicitacao, "
                "aprovacao aplicavel e confirmacao da desativacao.\n"
            )
            relatorio.write("STATUS: Pendente de verificacao.\n")
            relatorio.write("-" * 40 + "\n")

    print(f"Relatorio gerado em: {arquivo}")


if __name__ == "__main__":
    gerar_relatorio()
