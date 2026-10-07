# Roteiro para o vídeo — VendeFácil

**Duração sugerida:** 4 a 6 minutos  
**Antes de gravar:** deixe o PostgreSQL e a aplicação funcionando, abra o sistema no navegador e prepare os scripts SQL no pgAdmin. O vídeo deve mostrar a tela, a ação e o resultado no banco/aplicação.

## 1. Apresentação — 30 segundos

**Na tela:** mostre a página inicial do VendeFácil.

**Fale:**

“Olá, meu nome é João Victor Martins e este é o VendeFácil, um sistema de vendas desenvolvido para o trabalho da disciplina Projeto Banco de Dados, do professor Anderson. O sistema permite consultar produtos e estoques, registrar vendas e acompanhar o faturamento por produto. O objetivo deste projeto é demonstrar a integração da aplicação com recursos do PostgreSQL: uma View, uma Function e uma Procedure.”

## 2. Produtos e registro de uma venda — 1 minuto

**Na tela:** mostre a tabela de produtos e o estoque. Escolha quantidades pequenas para uma venda de demonstração. Clique em “Confirmar venda”.

**Fale:**

“Na página inicial, a aplicação consulta a tabela de produtos e apresenta o preço e o estoque disponível. Vou registrar uma venda com estes itens. Ao confirmar, a aplicação envia os produtos e as quantidades para o banco de dados, chamando a Procedure `sp_registrar_venda`.”

**Na tela:** após o retorno, mostre a mensagem de sucesso e atualize a página se necessário para mostrar o estoque reduzido.

**Fale:**

“A venda foi registrada e o estoque foi atualizado. A Procedure verifica se recebeu itens, valida as quantidades, confere se os produtos estão ativos e se há estoque suficiente, grava a venda e seus itens e reduz o estoque. Se alguma validação falhar, o banco gera um erro e a transação não deve deixar uma venda incompleta.”

## 3. Procedure — 45 segundos

**Na tela:** abra `database/procedures/01_sp_registrar_venda.sql` e mostre também a chamada em `src/app.py`, na rota `/vender`.

**Fale:**

“A Procedure recebe um parâmetro JSONB com uma lista de produtos e quantidades. Ela trabalha com as tabelas `vendas`, `itens_venda` e `produtos`. Escolhi uma Procedure porque registrar uma venda envolve várias operações coordenadas: criar o cabeçalho da venda, incluir os itens e atualizar o estoque. Na aplicação, a chamada é feita com `CALL sp_registrar_venda`, enviando os itens informados no formulário.”

## 4. Histórico e Function — 45 segundos

**Na tela:** abra “Histórico” no sistema. Em seguida, mostre `database/functions/01_fn_total_venda.sql` e a consulta da rota `/vendas` no código.

**Fale:**

“No Histórico, cada venda aparece com data e valor total. Esse valor é calculado no banco pela Function `fn_total_venda`. Ela recebe o identificador da venda e retorna a soma de quantidade multiplicada pelo preço unitário registrado em cada item. O cálculo usa a tabela `itens_venda`, preservando o preço praticado no momento da venda. A rota `/vendas` chama essa Function na consulta que alimenta a tela.”

## 5. Relatório e View — 45 segundos

**Na tela:** abra “Relatório” no sistema e depois mostre `database/views/01_vw_vendas_por_produto.sql` e a consulta da rota `/relatorio`.

**Fale:**

“O Relatório apresenta, para cada produto, as unidades vendidas e o faturamento acumulado. Esses dados vêm da View `vw_vendas_por_produto`, que relaciona produtos e itens de venda e consolida os valores. A View facilita a consulta desses indicadores sem repetir a agregação na aplicação. A rota `/relatorio` consulta a View e apresenta o resultado nesta tela.”

## 6. Banco de dados e encerramento — 45 segundos

**Na tela:** mostre brevemente as pastas `database/tables`, `functions`, `procedures`, `views` e `inserts`, depois volte à tela do sistema.

**Fale:**

“O projeto inclui scripts para criar as tabelas, a Function, a Procedure, a View e inserir dados de demonstração. Assim, outra pessoa pode recriar o banco seguindo a ordem apresentada no README. Neste sistema, a View alimenta o relatório, a Function calcula o total no histórico e a Procedure registra a venda e atualiza o estoque. Obrigado.”

## Checklist rápido antes de enviar

- [ ] O nome, disciplina e professor aparecem corretamente no README.
- [ ] O vídeo mostra o sistema e a venda sendo registrada.
- [ ] O vídeo mostra o estoque antes e depois da venda.
- [ ] A Function, a Procedure e a View são mostradas no SQL e ligadas às telas correspondentes.
- [ ] O link do vídeo funciona para o professor.
- [ ] O repositório GitHub está acessível ao professor.
