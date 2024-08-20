Replique este desenho asteristicos(5) mas agora inicie com asteristicos(20).
* * * * * 
* * * * 
* * * 
* * 
*


SELECT (SELECT LISTAGG('* ', '') WITHIN GROUP (ORDER BY LEVEL) AS  FROM DUAL CONNECT BY level <= RN)
   FROM (SELECT  ROWNUM AS RN
            FROM DUAL A
          CONNECT BY ROWNUM <= 20
          ORDER BY 1 DESC);