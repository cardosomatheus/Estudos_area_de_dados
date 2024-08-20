Gire a coluna Occupation em OCCUPATIONS para que cada Name seja classificado alfabeticamente e exibido abaixo de sua Occupation correspondente . Os cabeçalhos da coluna de saída devem ser Doctor , Professor , Singer e Actor , respectivamente.
Nota: Imprima NULL quando não houver mais nomes correspondentes a uma ocupação.


A tabela OCUPAÇÕES é descrita da seguinte forma:
Ocupação conterá apenas um dos seguintes valores: Doutor , Professor , Cantor ou Ator .
Entrada de amostra

Saída de amostra:
Jenny    Ashley     Meera  Jane
Samantha Christeen  Priya  Julia
NULL     Ketty      NULL   Maria
Explicação

A primeira coluna é uma lista alfabeticamente ordenada de nomes de Doutores.
A segunda coluna é uma lista alfabeticamente ordenada de nomes de Professores.
A terceira coluna é uma lista alfabeticamente ordenada de nomes de Cantores.
A quarta coluna é uma lista alfabeticamente ordenada de nomes de Atores.
Os dados de células vazias para colunas com menos do que o número máximo de nomes por ocupação (neste caso, as colunas Professor e Ator) são preenchidas com valores NULL .

SELECT MAX(CASE WHEN OCCUPATION = 'Doctor' THEN NAME END) AS Doctor,
       MAX(CASE WHEN OCCUPATION = 'Professor' THEN NAME END) AS Professor,
       MAX(CASE WHEN OCCUPATION = 'Singer' THEN NAME END) AS Singer,
       MAX(CASE WHEN OCCUPATION = 'Actor' THEN NAME END) AS Actor
    FROM(SELECT ROW_NUMBER() OVER(PARTITION BY OCCUPATION ORDER BY NAME) RN,
                A.*
            FROM OCCUPATIONS A)
  GROUP BY RN
  ORDER BY RN;