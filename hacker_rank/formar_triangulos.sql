Escreva uma consulta identificando o tipo de cada registro na tabela TRIANGLES usando seus três comprimentos laterais. Produza uma das seguintes instruções para cada registro na tabela:

Equilátero : É um triângulo comlados de igual comprimento.
Isósceles : É um triângulo comlados de igual comprimento.
Escaleno : É um triângulo comlados de comprimentos diferentes.
Não é um triângulo : Os valores dados de A , B e C não formam um triângulo.
Formato de entrada

A tabela TRIANGLES.

SELECT 
    CASE 
      WHEN (A +B > C) AND (C+A>B) AND (B+C>A) THEN
        CASE 
          WHEN (A <> B AND  B <> C  AND C <> A) AND (A +B > C)  THEN 'Scalene'
          WHEN (A = B AND A = C) THEN 'Equilateral'
          WHEN (A = B AND A <> C) OR (A = C AND A <> B) OR (B = C AND B <> A) THEN  'Isosceles'
        END                                  
      ELSE 'Not A Triangle'
     END
FROM TRIANGLES A;
