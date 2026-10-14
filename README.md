Sistema de Auditoria ITGC com Python

Sobre o projeto

Projeto prático de auditoria de TI desenvolvido em Python, com foco em ITGC (IT General Controls — Controles Gerais de TI), gestão de acessos, identificação de riscos e geração de relatórios de auditoria.

O sistema identifica funcionários desligados que ainda possuem acesso ativo aos sistemas, registra as falhas encontradas, classifica os riscos associados e apresenta ações corretivas recomendadas e o status da verificação.

Finalidade educacional: o projeto utiliza dados fictícios e simula procedimentos de auditoria de TI.

Objetivos

Simular a verificação de Controles Gerais de TI.

Identificar possíveis falhas na gestão de acessos.

Registrar riscos e recomendar ações corretivas.

Gerar relatórios de auditoria em TXT e Excel.

Validar as funcionalidades por meio de testes automatizados.

Tecnologias utilizadas

Python

pytest

openpyxl

Git e GitHub

Funcionalidades

Verificação de acessos de usuários.

Identificação de funcionários desligados com acesso ativo.

Registro de falhas de controle e riscos associados.

Recomendações de ações corretivas.

Geração de relatórios de auditoria em formato TXT.

Geração de planilhas Excel com data, controle, funcionário, falha identificada, risco, ação recomendada e status.

Testes automatizados para validar as funcionalidades do sistema.

Estrutura do projeto

projeto-itgc-auditoria-ti/
├── src/
│   ├── controle_acesso.py
│   ├── relatorio_auditoria.py
│   └── relatorio_excel.py
├── tests/
│   ├── test_controle_acesso.py
│   └── test_relatorio_auditoria.py
├── relatorios/
├── .gitignore
└── README.md

A pasta relatorios/ armazena os arquivos gerados durante a execução do sistema.

Como executar

1. Instalar as dependências

No terminal do VS Code ou no PowerShell, execute:

py -m pip install openpyxl pytest

2. Gerar o relatório TXT

py -m src.relatorio_auditoria

3. Gerar o relatório Excel

py -m src.relatorio_excel

Os relatórios serão salvos na pasta relatorios/.

4. Executar os testes automatizados

py -m pytest tests -v

Conceitos de auditoria praticados

ITGC — Controles Gerais de TI.

Gestão de acessos e desligamento de usuários.

Identificação e documentação de falhas de controle.

Avaliação de riscos e recomendações de ações corretivas.

Geração de evidências e acompanhamento de pendências.

Testes automatizados e validação de resultados.

Observação sobre segurança

O sistema simula a identificação de falhas de acesso utilizando dados fictícios. A desativação real de contas, a validação das evidências e a execução de ações corretivas dependem dos responsáveis autorizados e dos procedimentos da organização.

Autora

Josiani Oliveira

Estudante do último ano de Análise e Desenvolvimento de Sistemas.

Interesses profissionais: QA e testes de software, Python, suporte de TI e governança de TI.