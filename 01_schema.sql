-- Execute no banco vendafacil antes dos demais scripts.
CREATE TABLE IF NOT EXISTS produtos(id BIGSERIAL PRIMARY KEY,nome VARCHAR(120) NOT NULL UNIQUE,preco NUMERIC(10,2) NOT NULL CHECK(preco>=0),estoque INTEGER NOT NULL DEFAULT 0 CHECK(estoque>=0),ativo BOOLEAN NOT NULL DEFAULT TRUE);
CREATE TABLE IF NOT EXISTS vendas(id BIGSERIAL PRIMARY KEY,criada_em TIMESTAMPTZ NOT NULL DEFAULT NOW());
CREATE TABLE IF NOT EXISTS itens_venda(id BIGSERIAL PRIMARY KEY,venda_id BIGINT NOT NULL REFERENCES vendas(id) ON DELETE CASCADE,produto_id BIGINT NOT NULL REFERENCES produtos(id),quantidade INTEGER NOT NULL CHECK(quantidade>0),preco_unitario NUMERIC(10,2) NOT NULL CHECK(preco_unitario>=0));
CREATE INDEX IF NOT EXISTS idx_itens_venda_venda ON itens_venda(venda_id);
