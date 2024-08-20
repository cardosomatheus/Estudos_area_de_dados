Harry Potter e seus amigos estão na casa de Olivaras com Rony, finalmente substituindo a velha varinha quebrada de Charlie.
Hermione decide que a melhor maneira de escolher é determinando o número mínimo de galeões de ouro necessários para comprar cada varinha não maligna de alto poder e idade. 

Escreva uma consulta para imprimir o id , age , coins_needed e power das varinhas nas quais Ron está interessado,
 classificadas em ordem decrescente de power . Se mais de uma varinha tiver o mesmo poder, classifique o resultado em ordem decrescente de age .

Formato de entrada

As tabelas a seguir contêm dados sobre as varinhas no inventário de Olivaras:

Varinhas: O id é o id da varinha, o code é o código da varinha, coins_needed é o número total de galeões de ouro necessários para comprar a varinha e o power denota a qualidade da varinha (quanto maior o poder, melhor a varinha é).


SELECT A.ID, A.AGE, A.COINS_NEEDED, A.PW
    FROM (SELECT A.ID,
                B.AGE,
                ROW_NUMBER() OVER(PARTITION BY A.POWER, B.AGE ORDER BY COINS_NEEDED) RN,
                A.COINS_NEEDED,
                A.POWER PW
            FROM WANDS A
            JOIN WANDS_PROPERTY B ON A.CODE = B.CODE
        WHERE B.IS_EVIL = 0) A
  WHERE A.RN = 1
  ORDER BY A.PW DESC, A.AGE DESC;