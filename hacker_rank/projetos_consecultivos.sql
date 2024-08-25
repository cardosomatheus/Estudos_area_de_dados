 Você recebeu uma tabela Projects , contendo três colunas: Task_ID , Start_Date e End_Date . É garantido que a diferença entre End_Date e Start_Date seja igual a 1 dia para cada linha na tabela.
 Se o End_Date das tarefas for consecutivo, então elas são parte do mesmo projeto. Samantha está interessada em encontrar o número total de projetos diferentes concluídos.
 
 Escreva uma consulta para gerar as datas de início e término de projetos listados pelo número de dias que levou para concluir o projeto em ordem crescente. Se houver mais
de um projeto com o mesmo número de dias de conclusão, ordene pela data de início do projeto.

Explicação

O exemplo descreve os quatro projetos a seguir:

Projeto 1 : As tarefas 1 , 2 e 3 são concluídas em dias consecutivos, então elas são parte do projeto. Assim, a data de início do projeto é 2015-10-01 e a data de término é 2015-10-04 , então levou 3 dias para concluir o projeto.
Projeto 2 : As tarefas 4  e  5  são concluídas em dias consecutivos, então elas são parte do projeto. Assim, a data de início do projeto é  2015-10-13  e a data de término é  2015-10-15 , então levou  2 dias  para concluir o projeto.
Projeto 3 : Somente a tarefa 6  faz parte do projeto. Assim, a data de início do projeto é  2015-10-28  e a data de término é  2015-10-29 , então levou  1 dia  para concluir o projeto.
Projeto 4 : Somente a tarefa  7  faz parte do projeto. Assim, a data de início do projeto é  2015-10-30  e a data de término é  2015-10-31 , então levou  1 dia  para concluir o projeto.



WITH T AS (
    -- valida se a data_final existe como inicial, isso signifca que ela é uma continuação do projeto.
    SELECT CASE WHEN A.START_DATE IN (SELECT B.END_DATE FROM PROJECTS B) THEN NULL  ELSE A.START_DATE END AS VALIDA_CONTINUACAO,
           A.*
        FROM PROJECTS A
      ORDER BY A.START_DATE
),
  U AS (
        -- Para os campos nulos, ou seja que possui continuacação, eles receberão o valor anterior preenchido, ou seja o valor inicial daquele projeto
    SELECT LAST_VALUE(VALIDA_CONTINUACAO IGNORE NULLS) OVER(ORDER BY T.START_DATE) DATA_INICIAL,
            T.*
        FROM T
),
  V AS (
        -- uso o row_num para que  a data inicial do projeto e data final esteja na primeira posição. 
    SELECT ROW_NUMBER() OVER(PARTITION BY U.DATA_INICIAL ORDER BY U.END_DATE DESC) RN,
           (U.END_DATE - U.DATA_INICIAL) DIFERENCA_DIAS,
            U.*
        FROM U
)

SELECT V.DATA_INICIAL, V.END_DATE
    FROM V 
  WHERE V.RN = 1
  ORDER BY V.DIFERENCA_DIAS, V.START_DATE;
