Você recebe uma tabela, BST , contendo duas colunas: N  e P,  onde N representa o valor de um nó na Árvore Binária e P é o pai de N.

Escreva uma consulta para encontrar o tipo de nó de Binary Tree ordenado pelo valor do nó. Produza um dos seguintes para cada nó:

Raiz : Se o nó for nó raiz.
Folha : Se o nó for um nó folha.
Interno : Se o nó não for raiz nem folha.
Entrada de amostra



Saída de amostra:

1 Leaf
2 Inner
3 Leaf
5 Root
6 Leaf
8 Inner
9 Leaf


SELECT A.N,
       CASE
        WHEN A.P IS NULL THEN 'Root'
        WHEN A.N IN (SELECT B.P FROM BST B) THEN 'Inner'
        ELSE 'Leaf'
       END 
  FROM BST A
  ORDER BY A.N;