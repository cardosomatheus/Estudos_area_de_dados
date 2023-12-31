/* 
    AP�S A INSER��O, DELETE, OU UPDATE DO REGISTRO NA TABELA ITENS NOTAS, A TRIGGER DELETA TODOS OS REGISTRO EM TAB_FATURAMENTO
    E FAZ UM JOIN SELECIONANDO E AGRUPANDO O FATURAMENTO POR DIA. COM ISSO ESSE DIOS VALORES ENCONTRADOS POR LINHA
    S�O MODIFICADADOS EM TAB_FATURAMENTO ATRAV�S DO INSERT DE MANEIRA AUTOMATICA ATRAV�S DO GATILHO(TRIGGER)
*/

-- CRIA OU MODIFIQUE A TRIGGER
CREATE OR REPLACE TRIGGER TG_TAB_FATURAMENTO
AFTER INSERT OR DELETE OR UPDATE ON ITENS_NOTAS
BEGIN
    --  DELETA TODOS OS  REGISTROS DA TABELA
    DELETE FROM TAB_FATURAMENTO;
    --  INSERE TODOS OS REGISTROS RETORNADOS DA CONSULTA 
    INSERT INTO TAB_FATURAMENTO
    -- SELECIONA O FATURAMENTO AGRUPADO POR DIA. O TOTAL DE DATURAMENTOS NO DIA
    SELECT
        N.DATA_VENDA,
        SUM(TN.PRECO*TN.QUANTIDADE)  AS FATURAMENTO
    FROM NOTAS N
    INNER JOIN ITENS_NOTAS TN
        ON TN.NUMERO = N.NUMERO
    GROUP BY N.DATA_VENDA;
END;


-- TABELA TAB_FATURAMENTO
CREATE TABLE TAB_FATURAMENTO(
    DATA_VENDA DATE NULL,
    FATURAMENTO FLOAT
);

-- INSERT EM NOTAS
INSERT INTO NOTAS (NUMERO,DATA_VENDA,CPF,MATRICULA,IMPOSTO)
VALUES ('007',TO_DATE('2019-01-03','YYYY-MM-DD'),'1471156710','235',0.2);
-- INSERT EM ITENS_NOTAS
INSERT INTO ITENS_NOTAS (NUMERO,CODIGO,QUANTIDADE,PRECO)
VALUES ('007','1040107',15,10);

-- UPDATE QUANTIDADE EM ITENS_NOTAS
UPDATE ITENS_NOTAS
SET QUANTIDADE = 500
WHERE NUMERO = '007';

SELECT * FROM TAB_FATURAMENTO;

