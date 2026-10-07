# VendeFácil — Sistema de vendas
Projeto acadêmico individual para integrar Python/Flask com recursos do PostgreSQL.

## Identificação
- Integrante: **João Victor Martins**
- Disciplina: **Projeto Banco de Dados**
- Professor: **Anderson**

## Sobre
Aplicação web para consultar produtos, registrar vendas e acompanhar faturamento. A Procedure registra a venda e baixa estoque; a Function calcula seu total; a View consolida unidades e faturamento por produto.

## Tecnologias
Python 3.10+, Flask, PostgreSQL 14+, psycopg 3.

## Banco
Tabelas: produtos, vendas, itens_venda. View: vw_vendas_por_produto. Function: fn_total_venda(id). Procedure: sp_registrar_venda(jsonb).

## Integração
1. Relatório consulta a View.
2. Histórico chama a Function para calcular total por venda.
3. Formulário de venda chama a Procedure, que valida estoque e grava a venda atomicamente.

## Executar
1. Crie o banco PostgreSQL vendafacil.
2. Execute os scripts nesta ordem: database/tables/01_schema.sql, database/functions/01_fn_total_venda.sql, database/procedures/01_sp_registrar_venda.sql, database/views/01_vw_vendas_por_produto.sql, database/inserts/01_demo.sql.
3. Crie e ative um ambiente virtual: python -m venv .venv (Windows: .venv\Scripts\activate).
4. Instale: pip install -r requirements.txt.
5. Defina DATABASE_URL, por exemplo postgresql://postgres:SENHA@localhost:5432/vendafacil.
6. Execute python src/app.py e abra http://127.0.0.1:5000.

Para o vídeo, demonstre venda, estoque, histórico/Function, relatório/View e scripts SQL.
