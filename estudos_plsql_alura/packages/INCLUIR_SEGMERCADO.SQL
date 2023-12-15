
CREATE OR REPLACE NONEDITIONABLE PROCEDURE incluir_segmercado
    (p_id IN segmercado.ID%TYPE,
     p_descricao IN segmercado.descricao%TYPE)
IS
 BEGIN
    INSERT INTO segmercado 
       VALUES(p_id, UPPER(p_descricao));
    COMMIT;
EXCEPTION
    WHEN dup_val_on_index THEN
        raise_application_error(-20001,'Segmento de Mercado já Cadastrado');
END;
