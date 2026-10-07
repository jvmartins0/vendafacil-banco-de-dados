-- Recebe JSON: [{"produto_id":1,"quantidade":2}]
CREATE OR REPLACE PROCEDURE sp_registrar_venda(p_itens JSONB) LANGUAGE plpgsql AS $$
DECLARE v_venda_id BIGINT; v_item JSONB; v_pid BIGINT; v_qtd INTEGER; v_preco NUMERIC(10,2); v_estoque INTEGER;
BEGIN
 IF p_itens IS NULL OR jsonb_typeof(p_itens)<>'array' OR jsonb_array_length(p_itens)=0 THEN RAISE EXCEPTION 'Informe ao menos um item.'; END IF;
 INSERT INTO vendas DEFAULT VALUES RETURNING id INTO v_venda_id;
 FOR v_item IN SELECT value FROM jsonb_array_elements(p_itens) LOOP
  v_pid:=(v_item->>'produto_id')::BIGINT; v_qtd:=(v_item->>'quantidade')::INTEGER;
  IF v_qtd IS NULL OR v_qtd<=0 THEN RAISE EXCEPTION 'Quantidade deve ser maior que zero.'; END IF;
  SELECT preco,estoque INTO v_preco,v_estoque FROM produtos WHERE id=v_pid AND ativo=TRUE FOR UPDATE;
  IF NOT FOUND THEN RAISE EXCEPTION 'Produto % não encontrado ou inativo.',v_pid; END IF;
  IF v_estoque<v_qtd THEN RAISE EXCEPTION 'Estoque insuficiente para produto % (disponível: %).',v_pid,v_estoque; END IF;
  INSERT INTO itens_venda(venda_id,produto_id,quantidade,preco_unitario) VALUES(v_venda_id,v_pid,v_qtd,v_preco);
  UPDATE produtos SET estoque=estoque-v_qtd WHERE id=v_pid;
 END LOOP;
END; $$;
