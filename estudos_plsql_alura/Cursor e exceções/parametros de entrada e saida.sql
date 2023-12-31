/*
CRIAMOS A PROCEDURE COM O OBJETEVIVO DE RECEBER DOIS PARAMMETROS, UM DE ENTRADA(IN)E OUTRO DE SAIDA(OUT).
O PARAMETRO DE SAIDA RETORNA O VALOR DA VARIAVEL FINAL, OU SEJA, COM ALTERA합ES CONFORME A EXECU플.
*/
CREATE OR REPLACE PROCEDURE FORMATANDO_CNPJ
(P_CNPJ IN CLIENTE.CNPJ%TYPE,
 P_CNPJ_SAIDA OUT CLIENTE.CNPJ%TYPE)
 IS
 BEGIN
    P_CNPJ_SAIDA := SUBSTR(P_CNPJ,1,3)|| '/'||SUBSTR(P_CNPJ,4,2)||'-'||SUBSTR(P_CNPJ,6);
 END;



-- MODELO DE EXI플O MOSTRANDO O RESULTAND DA ULTILIZA플O DA PROCEDURE 
SET SERVEROUTPUT ON
DECLARE
    V_CNPJ_CLIENTE CLIENTE.CNPJ%TYPE;
BEGIN
    V_CNPJ_CLIENTE := '123456789';
    
    DBMS_OUTPUT.PUT_LINE(V_CNPJ_CLIENTE);
    --  SEM A PROCEDURE
    FORMATANDO_CNPJ(V_CNPJ_CLIENTE);
    -- COM A PROCEDURE
    DBMS_OUTPUT.PUT_LINE(V_CNPJ_CLIENTE);
END;
--------------------------------------------------------------------------------------------------------------------------------
INSERT INTO PRODUTO_VENDA_EXERCICIO
VALUES (3, '41232',TO_DATE('01/02/2022','DD/MM/YYYY'), 250, 20, 0, 0);
INSERT INTO PRODUTO_VENDA_EXERCICIO
VALUES (4, '32223',TO_DATE('03/02/2022','DD/MM/YYYY'), 200, 16, 0, 0);
INSERT INTO PRODUTO_VENDA_EXERCICIO
VALUES (5, '92347',TO_DATE('05/02/2022','DD/MM/YYYY'), 200, 16, 0, 0);
INSERT INTO PRODUTO_VENDA_EXERCICIO
VALUES (6, '41232',TO_DATE('02/03/2022','DD/MM/YYYY'), 210, 19, 0, 0);
INSERT INTO PRODUTO_VENDA_EXERCICIO
VALUES (7, '33854',TO_DATE('05/03/2022','DD/MM/YYYY'), 180, 21, 0, 0);
INSERT INTO PRODUTO_VENDA_EXERCICIO
VALUES (8, '92347',TO_DATE('09/03/2022','DD/MM/YYYY'), 170, 20, 0, 0);
INSERT INTO PRODUTO_VENDA_EXERCICIO
VALUES (10, '92347',TO_DATE('09/04/2022','DD/MM/YYYY'), 120, 20, 0, 0);
INSERT INTO PRODUTO_VENDA_EXERCICIO
VALUES (11, '33854',TO_DATE('09/04/2022','DD/MM/YYYY'), 200, 20, 0, 0);



/*  OBJETIVO E FAZER COM QUE O CAMPO VALOR TOTAL RECEBA A MULTIPLCA플O ENTRE PRECO * QUANTIDADE(PRE�O CORRETO) 
E ATUALIZE O VALOR DO IMPOSTO.
*/

-- PROCEDURE SEM PARAMETRO QUE FAZ A ATUALIZA플O DO VALOR_TOTAL E O PERCENTUAL_IMPOSTO
CREATE OR REPLACE PROCEDURE ATUALIZAR_VALOR_TOTAL_IMPOSTO 
IS
    -- VARIAVEIS LOCAIS
   v_ID PRODUTO_VENDA_EXERCICIO.ID%TYPE := 1;
   v_NUMERO_VENDA INTEGER;
   v_COD_PRODUTO PRODUTO_VENDA_EXERCICIO.COD_PRODUTO%TYPE;
   v_VALOR PRODUTO_VENDA_EXERCICIO.VALOR_TOTAL%TYPE;
   v_QUANTIDADE PRODUTO_VENDA_EXERCICIO.QUANTIDADE%TYPE;
   v_PRECO PRODUTO_VENDA_EXERCICIO.PRECO%TYPE;
   v_PERCENTUAL PRODUTO_VENDA_EXERCICIO.PERCENTUAL_IMPOSTO%TYPE;
BEGIN
    -- SELE플O DO TOTAL DE REGISTROS E ATRBUIDO A VARIAVEL v_NUMERO_VENDA
   SELECT COUNT(*) INTO v_NUMERO_VENDA FROM PRODUTO_VENDA_EXERCICIO;
   LOOP
       -- SELE플O DO  COD_PRODUTO, QUANTIDADE, PRECO ATRV�S COM ID  E ENCONTRANDO O VALOR CORRETOR DO VALOR_IMPOSTO
      SELECT COD_PRODUTO, QUANTIDADE, PRECO INTO v_COD_PRODUTO, v_QUANTIDADE, v_PRECO 
      FROM PRODUTO_VENDA_EXERCICIO WHERE ID = v_ID;
      v_VALOR := v_QUANTIDADE * v_PRECO;
      
      -- ATRAV�S DO COD_PRODUTO, RETORNA O IMPOSTO CORRETO
      v_PERCENTUAL := RETORNA_IMPOSTO(v_COD_PRODUTO);
      -- ATUALIZA플O DO VALOR_COMPRA E PERCENTUAL_IMPOSTO
      UPDATE PRODUTO_VENDA_EXERCICIO 
      SET VALOR_TOTAL = v_VALOR, PERCENTUAL_IMPOSTO = v_PERCENTUAL 
      WHERE ID = v_ID;
      
      v_ID := v_ID + 1;
   EXIT WHEN v_ID > v_NUMERO_VENDA;
   END LOOP;
END;


EXECUTE ATUALIZAR_VALOR_TOTAL_IMPOSTO;
SELECT * FROM PRODUTO_VENDA_EXERCICIO;

--------------------------------------------------------------------------------------------------------------------------------
