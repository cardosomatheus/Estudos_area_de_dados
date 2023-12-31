--  INCLUS�O DE REGISTRO COM PROCEDURES NA TABELA SEGMERCADO
EXECUTE INCLUIR_SEGMERCADO(4,'Farmaceuticos');


--  INCLUS�O DE REGISTRO COM PROCEDURES NA TABELA PRODUTO_EXERCICIO
EXECUTE INCLUINDO_PRODUTO('33854','Frescor da montanha-Aroma Laranja-1 litro','Mate');
EXECUTE INCLUINDO_PRODUTO('33855','Frescor da montanha-Aroma Laranja-1 litro','Mate');;
EXECUTE INCLUINDO_PRODUTO('89254','Frescor da montanha-Aroma Uva-1 litro','�guas');


--  INCLUS�O DE REGISTRO COM PROCEDURES NA TABELA CLIENTE
EXECUTE INCLUIR_CLIENTE(1,'SUPERMECADO CAMPEAO','1234567890',1,90000);
EXECUTE INCLUIR_CLIENTE(2,'SUPERMECADO DO VALE','1220101010',1,90000);
EXECUTE INCLUIR_CLIENTE(3,'SUPERMECADO DE MINAS','998822110',1,30000);


--  INCLUS�O DE REGISTRO COM PROCEDURES NA TABELA PRODUTO_VENDA_EXERCICIO COM VALORES DENTRO DE VARIAVEIS
EXECUTE INCLUINDO_DADOS_VENDA(1,'41232','01/01/2022',100,10);
EXECUTE INCLUINDO_DADOS_VENDA(2,'92347','01/01/2022',200,25);


--  ALTERA��O DE REGISTRO COM PROCEDURES NA TABELA  PRODUTO_EXERCICIO
EXECUTE ALTERANDO_CATEGORIA_PRODUTO('33854', '�guas');

--  EXCLUS�O DE REGISTRO COM PROCEDURES NA TABELA PRODUTO_EXERCICIO
EXECUTE EXCLUINDO_PRODUTO('89254');
EXECUTE EXCLUINDO_PRODUTO('33855');

-- EXEMPLO DE CONSULTA COM A FUN��O RETORNA_CATEGORIA()
SELECT COD,CATEGORIA, RETORNA_CATEGORIA(COD) FROM PRODUTO_EXERCICIO WHERE COD = '41232';


-- FUN��O PARA DESCOBRIR A CATEGORIA DO CLIENTE E ARMAZENAR EM UMA VARIAVEL
VARIABLE g_FAT VARCHAR2(100);
EXECUTE :g_FAT := CATEGORIA_CLIENTE(10000);
PRINT g_FAT;
