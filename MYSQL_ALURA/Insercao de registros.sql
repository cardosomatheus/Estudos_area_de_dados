use vendas_sucos;
---------------------------------------------------------------------------------------------------
-- INSERÇÃO INICIAL 
INSERT INTO PRODUTOS VALUES('1040107','LIGHT-350ML-Melância','Melância','350 ml', 'lata', 4.56);
INSERT INTO PRODUTOS VALUES('1040108','LIGHT-350ML-Graviola','Graviola','350 ml', 'lata', 4.00);
INSERT INTO PRODUTOS VALUES('1040109','LIGHT-350ML-Açai','Açai','350 ml', 'lata', 5.60);
INSERT INTO PRODUTOS VALUES('1040110','LIGHT-350ML-Jaca','Jaca','350 ml', 'lata', 6.00);
INSERT INTO PRODUTOS VALUES('1040111','LIGHT-350ML-Manga','Manga','350 ml', 'lata', 3.50);
INSERT INTO CLIENTE
	(CPF,NOME,ENDERECO,BAIRRO,CIDADE,ESTADO,CEP,DATA_NASCIMENTO,IDADE,SEXO,LIMITE_CREDITO,VOLUME_COMPRA,PRIMEIRA_COMPRA)
VALUES 
	('1471156710','Érica Carvalho','R. Iriquitia','Jardins','São Paulo','SP','80012212','19900901',27,'F',170000,24500,0),
	('19290992743','Fernando Cavalcante','R. Dois de Fevereiro','Água Santa','Rio de Janeiro','RJ','22000000','20000212',18,'M',100000,20000,1),
	('2600586709','César Teixeira','Rua Conde de Bonfim','Tijuca','Rio de Janeiro','RJ','22020001','20000312',18,'M',120000,22000,0);

---------------------------------------------------------------------------------------------------
-- Inserção na tabela de produtos
 INSERT INTO VENDAS_SUCOS.PRODUTOS
SELECT  CODIGO_DO_PRODUTO,
		NOME_DO_PRODUTO,
		SABOR,
		EMBALAGEM,
		TAMANHO,
		PRECO_DE_LISTA	  
	FROM sucos_vendas.tabela_de_produtos A
   WHERE NOT EXISTS(SELECT 1 
						FROM VENDAS_SUCOS.PRODUTOS B
					  WHERE B.CODIGO = A.CODIGO_DO_PRODUTO);
---------------------------------------------------------------------------------------------------                      
-- Inserção na tabela de cliente                      
INSERT INTO VENDAS_SUCOS.CLIENTE
SELECT  CPF,
		NOME,
        IFNULL(ENDERECO_1, ENDERECO_2),
        BAIRRO,
        CIDADE,
        ESTADO,
        CEP,
        DATA_DE_NASCIMENTO,
        IDADE,
        SEXO,
        LIMITE_DE_CREDITO,
        VOLUME_DE_COMPRA,
        PRIMEIRA_COMPRA
	FROM SUCOS_VENDAS.TABELA_DE_CLIENTES A 
   WHERE NOT EXISTS(SELECT 1
						FROM VENDAS_SUCOS.CLIENTE B
					   WHERE A.CPF = B.CPF);
			
---------------------------------------------------------------------------------------------------
-- Inserção na tabela de vendedores
INSERT INTO VENDAS_SUCOS.VENDEDORES
SELECT  MATRICULA,
		NOME,
        BAIRRO,
        PERCENTUAL_COMISSAO,
        DATA_ADMISSAO,
        DE_FERIAS
	FROM SUCOS_VENDAS.TABELA_DE_VENDEDORES A
   WHERE NOT EXISTS( SELECT 1
						FROM VENDAS_SUCOS.VENDEDORES B
					   WHERE A.MATRICULA = B.MATRICULA);
                       
SELECT * FROM  VENDAS_SUCOS.VENDEDORES;
---------------------------------------------------------------------------------------------------
-- Inserção na tabela de notas(notas_fiscais)
INSERT INTO VENDAS_SUCOS.NOTAS
SELECT  NUMERO,
		DATA_VENDA,
        CPF,
        MATRICULA,
        IMPOSTO
	FROM SUCOS_VENDAS.NOTAS_FISCAIS A
   WHERE NOT EXISTS(SELECT 1
						FROM VENDAS_SUCOS.NOTAS B
					   WHERE A.NUMERO = B.NUMERO);

---------------------------------------------------------------------------------------------------
-- Inserção na tabela de itens_notas
INSERT INTO VENDAS_SUCOS.ITENS_NOTAS
SELECT  NUMERO,
		CODIGO_DO_PRODUTO,
        QUANTIDADE,
        PRECO        
	FROM SUCOS_VENDAS.ITENS_NOTAS_FISCAIS A
   WHERE NOT EXISTS (SELECT 1
					FROM VENDAS_SUCOS.ITENS_NOTAS B
                   WHERE A.NUMERO = B.NUMERO);
                   
                   
SELECT * FROM VENDAS_SUCOS.ITENS_NOTAS;

COMMIT;

