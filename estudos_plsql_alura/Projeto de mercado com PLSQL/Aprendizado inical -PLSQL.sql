﻿--                   Aprendizado inicial sobre o conceito PL/SQL

SET SERVEROUTPUT ON;
DECLARE
    v_ID NUMBER(5) := 2;
BEGIN
    dbms_output.put_line(v_ID);
    v_ID :=3;
    dbms_output.put_line(v_ID);
END;



-- UM MEIO DE INSER��O DE REGISTROS COM PL/SQL
DECLARE
    V_ID NUMBER(5) := 5;
    V_DESCRICAO VARCHAR(100) := 'ESPOSTISTA';
BEGIN
    INSERT INTO SEGMERCADO VALUES(V_ID,UPPER(V_DESCRICAO));
    COMMIT;
END;

-- UM MEIO DE UPDATE EM REGISTROS COM PL/SQL
DECLARE
    V_ID NUMBER(5) := 2;
    V_DESCRICAO VARCHAR(100) := 'INDUSTRIAL';
BEGIN
    UPDATE SEGMERCADO
    SET DESCRICAO = UPPER(V_DESCRICAO)
    WHERE ID = V_ID;
    
    V_ID := 1;
    V_DESCRICAO := 'VAREJISTA';
    UPDATE SEGMERCADO
    SET DESCRICAO = UPPER(V_DESCRICAO)
    WHERE ID = V_ID;
    
    V_ID := 3;
    V_DESCRICAO := 'ATACADISTA';
    UPDATE SEGMERCADO
    SET DESCRICAO = UPPER(V_DESCRICAO)
    WHERE ID = V_ID;
    COMMIT;
END;


-- EXCLUSAO DE REGISTRO EM PL/SQL
DECLARE
    V_ID SEGMERCADO.ID%TYPE :=5;
BEGIN
    DELETE FROM SEGMERCADO 
    WHERE ID = V_ID;
    COMMIT;
END;
