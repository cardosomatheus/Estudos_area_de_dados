USE VENDAS_SUCOS;



DELIMITER $$
CREATE TRIGGER TG_CALCULA_FATURAMENTO 
AFTER UPDATE ON ITENS_NOTAS FOR EACH ROW
BEGIN
	INSERT INTO TAB_FATURAMENTO (DATA_VENDA, TOTAL_VENDAS)
	SELECT  SYSDATE(),
			ROUND(SUM(PRECO), 2) 
	FROM ITENS_NOTAS;
END$$
DELIMITER ;