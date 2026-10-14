from datetime import datetime
from pathlib import Path

from src.controle_acesso import verificar_acessos, usuarios


def gerar_relatorio():
    alertas = verificar_acessos(usuarios)

    pasta_relatorios = Path(__file__).resolve().parent.parent / "relatorios"
    pasta_relatorios.mkdir(parents=True, exist_ok=True)

    arquivo = pasta_relatorios / "relatorio_auditoria.txt"

    with arquivo.open("w", encoding="utf-8") as relatorio:
        relatorio.write("RELATÓRIO DE AUDITORIA ITGC\n")
        relatorio.write("=" * 40 + "\n")
        relatorio.write(
            f"Data da geração: {datetime.now():%d/%m/%Y %H:%M}\n\n"
        )

        if not alertas:
            relatorio.write("Nenhuma falha de acesso identificada.\n")

        for alerta in alertas:
            relatorio.write("CONTROLE: Gestão de acessos\n")
            relatorio.write(f"FALHA: {alerta}\n")
            relatorio.write(
                "RISCO: Acesso não autorizado a sistemas e dados.\n"
            )
            relatorio.write(
                "AÇÃO RECOMENDADA: Solicitar a desativação do acesso "
                "e confirmar a execução.\n"
            )
            relatorio.write(
                "EVIDÊNCIAS NECESSÁRIAS: Registro da solicitação, "
                "aprovação aplicável e confirmação da desativação.\n"
            )
            relatorio.write("STATUS: Pendente de verificação.\n")
            relatorio.write("-" * 40 + "\n")

    print(f"Relatório gerado em: {arquivo}")


if __name__ == "__main__":
    gerar_relatorio()