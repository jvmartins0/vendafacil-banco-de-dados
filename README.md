# VendeFácil — Sistema de vendas
Projeto acadêmico individual para integrar Python/Flask com PostgreSQL.

## Identificação
- Integrante: **João Victor Martins**
- Disciplina: **Projeto Banco de Dados**
- Professor: **Anderson**

## Sobre
Aplicação web para consultar produtos, registrar vendas e acompanhar faturamento. A Procedure registra a venda e baixa estoque; a Function calcula o total da venda; a View consolida unidades e faturamento por produto.

## Tecnologias
Python 3.10+, Flask, PostgreSQL 14+, psycopg 3.

## Recursos de banco
- Tabelas `produtos`, `vendas` e `itens_venda`: definidas em `01_schema.sql`.
- Function `fn_total_venda(id)`: `01_fn_total_venda.sql`; chamada na tela de histórico.
- Procedure `sp_registrar_venda(jsonb)`: `01_sp_registrar_venda.sql`; chamada ao confirmar uma venda.
- View `vw_vendas_por_produto`: `01_vw_vendas_por_produto.sql`; usada no relatório.
- `01_demo.sql`: insere produtos de exemplo.

Os arquivos ficam na raiz deste repositório para facilitar a visualização no GitHub. O pacote ZIP da entrega mantém a estrutura de pastas do projeto.

## Como executar
1. Crie o banco PostgreSQL `vendafacil`.
2. No Query Tool do pgAdmin, execute nesta ordem: `01_schema.sql`, `01_fn_total_venda.sql`, `01_sp_registrar_venda.sql`, `01_vw_vendas_por_produto.sql` e `01_demo.sql`.
3. Na pasta do projeto, crie e ative o ambiente virtual: `python -m venv .venv` e, no Windows, `.venv\Scripts\Activate.ps1`.
4. Instale as dependências: `pip install -r requirements.txt`.
5. Configure `DATABASE_URL`, por exemplo `postgresql://postgres:SENHA@localhost:5432/vendafacil`.
6. Inicie com `python app.py` e abra http://127.0.0.1:5000.

O roteiro de demonstração está em `roteiro_video.md`; o checklist final, em `checklist_entrega.md`.
