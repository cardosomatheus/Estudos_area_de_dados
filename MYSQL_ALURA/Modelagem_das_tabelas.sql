-- criação e expecificação de uso do database
CREATE DATABASE IF NOT EXISTS VENDAS_SUCOS DEFAULT CHARACTER SET = UTF8;
USE VENDAS_SUCOS;

-- Modelagem das tabelas e seus relacionamentos
CREATE TABLE PRODUTOS(
	CODIGO VARCHAR(10) NOT NULL,
    DESCRITOR VARCHAR(100),
    SABOR VARCHAR(50),
    TAMANHO VARCHAR(50),
    EMBALAGEM VARCHAR(50),
    PRECO_LISTA FLOAT,
    CONSTRAINT PK_PRODUTOS PRIMARY KEY(CODIGO)
);


CREATE TABLE VENDEDORES (
	MATRICULA VARCHAR(5) NOT NULL,
    NOME VARCHAR(100),
    BAIRRO VARCHAR(50),
    COMISSAO FLOAT,
    DATA_ADMISSAO DATE,
    FERIAS BIT(1),
    CONSTRAINT PK_VENDEDORES PRIMARY KEY(MATRICULA)
);

CREATE TABLE CLIENTE (
	CPF VARCHAR(11) NOT NULL,
    NOME VARCHAR(100),
    ENDERECO VARCHAR(150),
    BAIRRO VARCHAR(50),
    CIDADE VARCHAR(50),
    ESTADO VARCHAR(50),
    CEP VARCHAR(8),
    DATA_NASCIMENTO DATE,
    IDADE INT,
    SEXO VARCHAR(1),
    LIMITE_CREDITO FLOAT,
	VOLUME_COMPRA FLOAT,
    PRIMEIRA_COMPRA BIT(1),
    CONSTRAINT PK_CLIENTE PRIMARY KEY(CPF)
); 

CREATE TABLE TABELA_VENDAS (
	NUMERO VARCHAR(5) NOT NULL,
    DATA DATE,
    CPF VARCHAR(11) NOT NULL,
    MATRICULA VARCHAR(5) NOT NULL,
    IMPOSTO FLOAT,
    CONSTRAINT PK_NUMERO PRIMARY KEY (NUMERO),
    CONSTRAINT FK_VENDAS_CLIENTE FOREIGN KEY (CPF) REFERENCES CLIENTE(CPF),
    CONSTRAINT FK_VENDAS_VENDEDIRES FOREIGN KEY(MATRICULA) REFERENCES VENDEDORES(MATRICULA)
);
ALTER TABLE TABELA_VENDAS RENAME NOTAS;

CREATE TABLE ITENS_NOTAS(
	NUMERO VARCHAR(5) NOT NULL,
    CODIGO VARCHAR(10) NOT NULL,
    QUANTIDADE INT,
    PRECO FLOAT,
    CONSTRAINT PK_ITENS_NOTAS PRIMARY KEY (NUMERO, CODIGO),
    CONSTRAINT FK_ITENS_NOTAS_NOTAS FOREIGN KEY(NUMERO) REFERENCES NOTAS(NUMERO),
    CONSTRAINT FK_ITENS_NOTAS_PRODUTO FOREIGN KEY(CODIGO) REFERENCES PRODUTOS(CODIGO)
);

CREATE TABLE TAB_FATURAMENTO (
	DATA_VENDAS DATE NULL,
    TOTAL_VENDAS FLOAT);

