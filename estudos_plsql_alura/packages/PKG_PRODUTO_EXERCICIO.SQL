create or replace noneditionable package PKG_PRODUTO_EXERCICIO 
is

    --PROCEDUTRES
-----------------------------------------------------------------------------------------------------------------------------------
    procedure INCLUINDO_DADOS_VENDA (P_ID PRODUTO_VENDA_EXERCICIO.id%type,
                                     P_COD_PRODUTO PRODUTO_VENDA_EXERCICIO.COD_PRODUTO%type,
                                     P_DATA PRODUTO_VENDA_EXERCICIO.data%type,
                                     P_QUANTIDADE PRODUTO_VENDA_EXERCICIO.QUANTIDADE%type,
                                     P_PRECO PRODUTO_VENDA_EXERCICIO.PRECO%type);
  
-----------------------------------------------------------------------------------------------------------------------------------   
     procedure INCLUINDO_PRODUTO    (P_COD PRODUTO_EXERCICIO.COD%type,
                                     P_DESCRICAO PRODUTO_EXERCICIO.DESCRICAO%type);
                                     
-----------------------------------------------------------------------------------------------------------------------------------
     procedure INCLUINDO_PRODUTO    (P_COD PRODUTO_EXERCICIO.COD%type,
                                     P_DESCRICAO PRODUTO_EXERCICIO.DESCRICAO%type,
                                     P_CATEGORIA PRODUTO_EXERCICIO.CATEGORIA%type);
        
        
        -- FUNÇOES
-----------------------------------------------------------------------------------------------------------------------------------
    function RETORNA_CATEGORIA      (P_COD in PRODUTO_EXERCICIO.COD%type)
    return PRODUTO_EXERCICIO.CATEGORIA%type;

-----------------------------------------------------------------------------------------------------------------------------------
    function RETORNA_IMPOSTO        (P_COD_PRODUTO PRODUTO_VENDA_EXERCICIO.COD_PRODUTO%type)
    return PRODUTO_VENDA_EXERCICIO.PERCENTUAL_IMPOSTO%type;
    
-----------------------------------------------------------------------------------------------------------------------------------
    -- CONSTANTES
    C_SUCO_DE_FRUTAS number(10) := 10;
    C_AGUAS number(10):= 20;
    C_MATE number(10):= 15;

end;