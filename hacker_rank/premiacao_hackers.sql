 Escreva uma consulta para imprimir o hacker_id e o nome dos hackers que atingiram a pontuação máxima em mais de um desafio. Ordene sua saída em ordem decrescente 
 pelo número total de desafios em que o hacker obteve a pontuação máxima. Se mais de um hacker recebeu a pontuação máxima no mesmo número de desafios, 
 classifique-os por hacker_id crescente.


WITH T AS (
    SELECT C.HACKER_ID,
           COUNT(*) CONTADOR
        FROM Submissions C
        JOIN CHALLENGES D ON C.CHALLENGE_ID = D.CHALLENGE_ID 
        JOIN Difficulty E ON D.Difficulty_LEVEL = E.Difficulty_LEVEL
      WHERE C.SCORE = E.SCORE
      GROUP BY C.HACKER_ID
      HAVING COUNT(*) > 1
)
SELECT A.HACKER_ID||' '||B.NAME  
    FROM T A 
    JOIN HACKERS B ON A.HACKER_ID = B.HACKER_ID
   ORDER BY A.CONTADOR DESC, A.HACKER_ID;




