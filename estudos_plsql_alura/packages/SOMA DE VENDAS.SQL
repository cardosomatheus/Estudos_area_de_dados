CREATE OR REPLACE NONEDITIONABLE PROCEDURE soma_vendas 
(p_venda_limite IN produto_venda_exercicio.valor_total%TYPE,
 p_id_retorno OUT produto_venda_exercicio.ID%TYPE)
IS
   v_id produto_venda_exercicio.ID%TYPE := 1;
   v_valor_total produto_venda_exercicio.valor_total%TYPE;
   v_venda_total produto_venda_exercicio.valor_total%TYPE := 0;
BEGIN
  LOOP
     SELECT valor_total INTO v_valor_total FROM produto_venda_exercicio WHERE ID = v_id;
     v_venda_total := v_venda_total + v_valor_total;
     IF v_venda_total >= p_venda_limite THEN
        EXIT;
     END IF;
     v_id := v_id + 1;
  END LOOP;
  p_id_retorno := v_id;
END;
