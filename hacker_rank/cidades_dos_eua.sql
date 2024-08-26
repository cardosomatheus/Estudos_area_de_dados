Consulte todas as colunas para todas as cidades americanas na tabela CITY com populações maiores que 100000. O CountryCode para América é USA.


SELECT * 
  FROM CITY
 WHERE UPPER(COUNTRYCODE) = 'USA'
 AND POPULATION > 100000;