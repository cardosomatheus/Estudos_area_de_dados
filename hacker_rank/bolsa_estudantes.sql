 Você recebe três tabelas:  Students , Friends e Packages.  

Students contém duas colunas: ID  e Name .
Friends contém duas colunas: ID e Friend_ID ( ID do ÚNICO melhor amigo).
Packages  contém duas colunas: ID e Salary (salário oferecido em $ milhares por mês).


 Escreva uma consulta para gerar os nomes dos alunos cujos melhores amigos receberam uma oferta de salário maior que a deles. Os nomes devem ser ordenados
pelo valor do salário oferecido aos melhores amigos. É garantido que nenhum aluno recebeu a mesma oferta de salário.

SELECT D.NAME 
  FROM Friends A
  JOIN Packages B ON A.ID = B.ID
  JOIN Packages C ON A.FRIEND_ID = C.ID
  JOIN Students D ON A.ID = D.ID
 WHERE C.SALARY > B.SALARY
 ORDER BY C.SALARY;