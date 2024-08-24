 Você fez um trabalho tão bom ajudando Julia com seu último desafio de competição de codificação que ela quer que você trabalhe neste também!
 A pontuação total de um hacker é a soma de suas pontuações máximas para todos os desafios.
Escreva uma consulta para imprimir o hacker_id , o nome e a pontuação total dos hackers ordenados pela pontuação decrescente. Se mais de um hacker atingiu a mesma pontuação total,
então classifique o resultado por hacker_id crescente . 
Exclua todos os hackers com uma pontuação total de 0 no seu resultado.


Hackers: O hacker_id é o id do hacker, e o name é o nome do hacker.
SUBMISSIONS: submission_id é o id do envio, hacker_id é o id do hacker que fez o envio, challenge_id é o id do desafio ao qual o envio pertence e score é a pontuação do envio.



WITH A AS (
  -- PONTUAÇÃO MAXIMA EM CADA DESAFIO FEITO PELO HACKER 
  SELECT H.HACKER_ID,
         H.NAME,
         S.CHALLENGE_ID,
         MAX(S.SCORE) MAXPONT_POR_DESAFIO_USER
    FROM SUBMISSIONS S
    JOIN HACKERS H ON S.HACKER_ID = H.HACKER_ID
   GROUP BY H.HACKER_ID, H.NAME, S.CHALLENGE_ID 
),
B AS ( 
  -- SOMANDO AS PONTUAÇÕES MAXIMA DOS DESAFIOS POR HACKER
  SELECT A.HACKER_ID,
         A.NAME,
         SUM(A.MAXPONT_POR_DESAFIO_USER) SUMPONT_POR_DESAFIO_USER
    FROM A
   GROUP BY A.HACKER_ID, A.NAME
)
-- RETORNANDO APENAS AQUELE POSSUI UMA PONTUAÇÃO MAIOR QUE 0
SELECT B.HACKER_ID,
       B.NAME,
       B.SUMPONT_POR_DESAFIO_USER
  FROM B 
  WHERE B.SUMPONT_POR_DESAFIO_USER > 0
  ORDER BY B.SUMPONT_POR_DESAFIO_USER DESC, B.HACKER_ID;
