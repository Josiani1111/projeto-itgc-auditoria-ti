# Sistema de Auditoria ITGC com Python

## Sobre o projeto

Projeto prático de auditoria de TI desenvolvido em Python, com foco em ITGC (*IT General Controls*), controle de acessos, identificação de riscos e geração de relatórios de auditoria.

O sistema identifica funcionários desligados que ainda possuem acesso ao sistema e registra a falha, o risco associado, a ação recomendada e o status da verificação.

**Finalidade educacional:** o projeto utiliza dados fictícios e simula procedimentos de auditoria.

## Objetivos

- Simular a verificação de controles gerais de TI.
- Identificar possíveis falhas na gestão de acessos.
- Registrar riscos e ações corretivas recomendadas.
- Gerar relatórios em TXT e Excel.
- Validar as funcionalidades por meio de testes automatizados.

## Tecnologias utilizadas

- Python
- pytest
- openpyxl
- Git e GitHub

## Funcionalidades

- Verificação de acessos de usuários.
- Identificação de funcionários desligados com acesso ativo.
- Geração de relatório de auditoria em TXT.
- Geração de planilha Excel com data, controle, funcionário, falha, risco, ação recomendada e status.
- Testes automatizados para validar os resultados.

## Estrutura do projeto

```text
projeto-itgc-auditoria-ti/
├── src/
│   ├── controle_acesso.py
│   ├── relatorio_auditoria.py
│   └── relatorio_excel.py
├── tests/
│   ├── test_controle_acesso.py
│   └── test_relatorio_auditoria.py
├── relatorios/  # Arquivos gerados durante a execução
├── .gitignore
└── README.md
```

## Como executar

### 1. Instalar as dependências

```powershell
py -m pip install openpyxl pytest
```

### 2. Gerar o relatório TXT

```powershell
py -m src.relatorio_auditoria
```

### 3. Gerar o relatório Excel

```powershell
py -m src.relatorio_excel
```

Os relatórios serão salvos na pasta `relatorios/`.

### 4. Executar os testes

```powershell
py -m pytest tests -v
```

## Conceitos de auditoria praticados

- ITGC — Controles Gerais de TI.
- Gestão de acessos e desligamento de usuários.
- Identificação e registro de riscos.
- Recomendações de ações corretivas.
- Documentação de evidências e acompanhamento de pendências.

**Nota:** o projeto simula a identificação de falhas de acesso. A desativação real de contas e a validação das evidências devem ser realizadas e confirmadas pelos responsáveis autorizados.

## Autora

**Josiani Oliveira**

Estudante do último ano de Análise e Desenvolvimento de Sistemas.

**Interesses profissionais:** QA e testes de software, Python, suporte de TI e governança de TI.