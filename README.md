Sistema de Auditoria ITGC com Python



Sobre o projeto



Projeto prático de auditoria de TI desenvolvido em Python, com foco em ITGC (IT General Controls), controle de acessos, identificação de riscos e geração de relatórios de auditoria.



O sistema identifica funcionários desligados que ainda possuem acesso ao sistema e registra a falha, o risco associado, a ação recomendada e o status da verificação.



Este projeto possui finalidade educacional e utiliza dados fictícios.



Objetivos



Simular a verificação de controles gerais de TI.



Identificar possíveis falhas na gestão de acessos.



Registrar riscos e ações corretivas recomendadas.



Gerar relatórios em TXT e Excel.



Validar as funcionalidades por meio de testes automatizados.



Tecnologias utilizadas



Python



pytest



openpyxl



Git e GitHub



Funcionalidades



Verificação de acessos de usuários.



Identificação de funcionários desligados com acesso ativo.



Geração de relatório de auditoria em TXT.



Geração de planilha Excel com data, controle, funcionário, falha, risco, ação recomendada e status.



Testes automatizados para validar os resultados.



Estrutura do projeto



projeto-itgc-auditoria-ti/

├── dados/

├── relatorios/

│   ├── relatorio\_auditoria.txt

│   └── relatorio\_auditoria.xlsx

├── src/

│   ├── controle\_acesso.py

│   ├── relatorio\_auditoria.py

│   └── relatorio\_excel.py

├── tests/

│   ├── test\_controle\_acesso.py

│   └── test\_relatorio\_auditoria.py

└── README.md



Como executar



1\. Instalar as dependências



py -m pip install openpyxl pytest



2\. Gerar o relatório TXT



py -m src.relatorio\_auditoria



3\. Gerar o relatório Excel



py -m src.relatorio\_excel



Os relatórios serão salvos na pasta relatorios/.



4\. Executar os testes



py -m pytest tests -v



Conceitos de auditoria praticados



ITGC — Controles Gerais de TI.



Gestão de acessos e desligamento de usuários.



Identificação e registro de riscos.



Recomendações de ações corretivas.



Documentação de evidências e acompanhamento de pendências.



O projeto demonstra uma simulação de controle de acessos. A desativação real de uma conta e a validação das evidências devem ser realizadas e confirmadas pelos responsáveis autorizados.



Autora



Josiani Oliveira



Estudante do último ano de Análise e Desenvolvimento de Sistemas.



Interesses profissionais: QA e testes de software, Python, suporte de TI e governança de TI.

