Gere os dois conjuntos de resultados a seguir:

Consulte uma lista alfabeticamente ordenada de todos os nomes em OCCUPATIONS , imediatamente seguidos pela primeira letra de cada profissão como um parentético (ou seja: entre parênteses). Por exemplo: AnActorName(A), ADoctorName(D), AProfessorName(P), e ASingerName(S).
Consulte o número de ocorrências de cada ocupação em OCCUPATIONS . Classifique as ocorrências em ordem crescente e envie-as no seguinte formato:

There are a total of [occupation_count] [occupation]s.
onde [occupation_count]é o número de ocorrências de uma ocupação em OCCUPATIONS e [occupation]é o nome da ocupação em letras minúsculas . Se mais de uma Occupation tiver o mesmo [occupation_count], elas devem ser ordenadas alfabeticamente.

Observação: haverá pelo menos duas entradas na tabela para cada tipo de ocupação.

SELECT A.COLUNA  FROM (SELECT   A.NAME||'('||SUBSTR(A.OCCUPATION,1,1)||')' COLUNA FROM OCCUPATIONS A ORDER BY NAME) A
 UNION ALL
SELECT B.COLUNA 
  FROM (SELECT  'There are a total of '|| COUNT(*) ||' '|| LOWER(B.OCCUPATION)||'s.' COLUNA
           FROM OCCUPATIONS B
          GROUP BY B.OCCUPATION
          HAVING COUNT(*) >1
          ORDER BY COUNT(*), B.OCCUPATION) B;