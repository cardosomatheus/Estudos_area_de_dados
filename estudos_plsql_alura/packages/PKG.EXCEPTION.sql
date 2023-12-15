CREATE OR REPLACE NONEDITIONABLE PACKAGE pkg_exception
IS
    e_null EXCEPTION;
    PRAGMA exception_init(e_null,-1400);
    
    e_fk EXCEPTION;
    PRAGMA exception_init(e_fk,-2291);
END;