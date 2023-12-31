-- INSER��O DE PRODUTOS

INSERT INTO TB_PRODUTOS 
(PRODUTO,NOME,EMBALAGEM,TAMANHO,SABOR,PRECO_LISTA)
VALUES
('1040107','Light - 350 ml - Mel�ncia','Lata','350 ml','Mel�ncia',4.56);

INSERT INTO TB_PRODUTOS 
(PRODUTO,NOME,EMBALAGEM,TAMANHO,SABOR,PRECO_LISTA)
VALUES
('1037797','Clean - 2 Litros - Laranja','PET','2 Litros','Laranja',16.01);

INSERT INTO TB_PRODUTOS 
(PRODUTO,NOME,EMBALAGEM,TAMANHO,SABOR,PRECO_LISTA)
VALUES
('1000889','Sabor da Montanha - 700 ml - Uva','Garrafa','700 ml','Uva',6.1);

INSERT INTO TB_PRODUTOS 
(PRODUTO,NOME,EMBALAGEM,TAMANHO,SABOR,PRECO_LISTA)
VALUES
('1004327','Videira do Campo - 1,5 Litros - Mel�ncia','PET','1,5 Litros','Mel�ncia',19.1);


-- INSER��O DE VENDEDORES

INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('OO233','Joao Geraldo da Fonseca','01/01/2015',0.10);

INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('00400','Maria do Rosario','23/07/2012',0.15);

INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('00810','Marcia Almeida','14/12/2016',0.18);

INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('00414','Carlos Moreira','13/11/2015',0.14);

INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('00934','Juvenildo Martins','09/03/2010',0.20);

INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('00342','Rodrigo Almeida','18/01/2022',0.09);

INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('00729','Patricia Martins','02/01/2022',0.09);


-- INSER��O DE VENDEDORES ESTRANGEIROS COM A DATA DE NASCIMENTO DIFERENTE DA BRASILEIRA
INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('00265','Jonh Wayne',TO_DATE('03/27/2019','MM/DD/YYYY'),0.12);

INSERT INTO TB_VENDEDORES
(MATRICULA,NOME,DATA_ADMISSAO,PERCENTUAL_COMISSAO)
VALUES
('00777','Katy Peterson',TO_DATE('02/04/2020','MM/DD/YYYY'),0.10);



-- INSER��O DE CLIENTES

INSERT INTO TB_CLIENTES 
(CPF, NOME, ENDERECO1, ENDERECO2, BAIRRO, CIDADE, ESTADO, CEP, DT_NASCIMENTO, IDADE, SEXO, LIMITE_CREDITO,
VOLUME_COMPRA, PRIMEIRA_COMPRA)
VALUES
('00333434577', 'Jo�o da Silva', 'Rua Projetada n�mero 10', NULL, 'VILA ROMAN', 'TR�S RIOS', 'RJ', '22222222', 
TO_DATE('12/10/1965','DD/MM/YYYY'), 56, 'M', 100000, 2000, 0);

INSERT INTO TB_CLIENTES 
(CPF, NOME, ENDERECO1, ENDERECO2, BAIRRO, CIDADE, ESTADO, CEP, DT_NASCIMENTO, IDADE, SEXO, LIMITE_CREDITO,
VOLUME_COMPRA, PRIMEIRA_COMPRA)
VALUES
('00333434588', 'Jo�o da Silva', 'Rua Projetada n�mero 10', NULL, 'VILA ROMAN', 'TR�S RIOS', 'RJ', '22222222', 
TO_DATE('12/10/1965', 'MM/DD/YYYY'), 56, 'M', 100000, 2000, 0);


SELECT * FROM tb_vendedores;


