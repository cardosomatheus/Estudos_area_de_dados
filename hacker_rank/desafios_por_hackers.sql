 Julia pediu que seus alunos criassem alguns desafios de codificação. Escreva uma consulta para imprimir o hacker_id , o nome e o número total de desafios criados por cada aluno.
lassifique seus resultados pelo número total de desafios em ordem decrescente. Se mais de um aluno criou o mesmo número de desafios, classifique o resultado por hacker_id . 
Se mais de um aluno criou o mesmo número de desafios e a contagem for menor que o número máximo de desafios criados, exclua esses alunos do resultado.


Hackers: O hacker_id é o id do hacker, e o name é o nome do hacker.

Challenges: O challenge_id é o id do desafio, e o hacker_id é o id do aluno que criou o desafio.


WITH A AS (
    -- A quantidade de desafios por hackers
    SELECT H.hacker_id, h.name, COUNT(D.challenge_id)  contador_desafios
      FROM Challenges D
      JOIN HACKERS H ON D.hacker_id = H.hacker_id
     GROUP BY H.hacker_id, H.name
),
B AS (
    -- valor de desafios
    SELECT MAX(A.contador_desafios) max_contador_desafios FROM A
),
C AS (
    -- informa os desafios que possui uma contagem de desafios menores do que o valor maximo e se repetem mais de uma vez para diferentes hackes.
    SELECT A.contador_desafios, COUNT(*) 
      FROM A,B
     WHERE A.contador_desafios < B.max_contador_desafios
     GROUP BY A.contador_desafios
     HAVING COUNT(*) > 1
)
SELECT * 
    FROM A
 WHERE A.contador_desafios NOT IN (SELECT C.contador_desafios FROM C)
 ORDER BY A.contador_desafios DESC, A.HACKER_ID;