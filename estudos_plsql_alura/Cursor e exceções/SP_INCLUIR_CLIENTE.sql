create or replace PROCEDURE INCLUIR_CLIENTE
(P_ID IN CLIENTE.ID%TYPE,
 P_RAZAO IN CLIENTE.RAZAO_SOCIAL%TYPE,
 P_CNPJ IN CLIENTE.CNPJ%TYPE,
 P_SEGMERCADO IN CLIENTE.SEGMERCADO_ID%TYPE,
 P_FATURAMENTO IN CLIENTE.FATURAMENTO_PREVISTO%TYPE)
IS
    v_CATEGORIA CLIENTE.CATEGORIA%TYPE;
    V_CPNJ CLIENTE.CNPJ%TYPE;
BEGIN
    FORMATANDO_CNPJ(P_CNPJ,V_CPNJ);
    v_CATEGORIA := CATEGORIA_CLIENTE(P_FATURAMENTO);
    
    INSERT INTO CLIENTE 
    VALUES(P_ID,P_RAZAO,V_CPNJ,P_SEGMERCADO,SYSDATE,P_FATURAMENTO,V_CATEGORIA);
    COMMIT;
END;


SELECT * FROM CLIENTE;
EXECUTE INCLUIR_CLIENTE(4,'SUPERMECADO REI DA COLINA','9876543210',1,50000);