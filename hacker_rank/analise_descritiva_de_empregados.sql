A corporação conglomerada de Amber acaba de adquirir algumas novas empresas. Cada uma das empresas segue esta hierarquia:
     FOUNDER => LEAD_MANAGER => SENIOR_LEAD_MANAGER => MANAGER => EMPLOYEE.

Escreva uma consulta para imprimir o company_code , nome do fundador , número total de gerentes líderes , número total de gerentes seniores , número total de gerentes e número total de funcionários . Ordene sua saída por company_code ascendente .

Observação:

As tabelas podem conter registros duplicados.
O company_code é string, então a classificação não deve ser numérica . Por exemplo, se os company_codes forem C_1 , C_2 e C_10 , então os company_codes ascendentes serão C_1 , C_10 e C_2 .
Formato de entrada

As tabelas a seguir contêm dados da empresa:

Empresa: O company_code é o código da empresa e founder é o fundador da empresa.

Lead_Manager: O lead_manager_code é o código do gerente líder, e o company_code é o código da empresa em que trabalha.

Senior_Manager: O senior_manager_code é o código do gerente sênior, o lead_manager_code é o código do gerente principal e o company_code é o código da empresa em que trabalha.

Gerente: O manager_code é o código do gerente, o senior_manager_code é o código do seu gerente sênior, o lead_manager_code é o código do seu gerente principal e o company_code é o código da empresa em que trabalha.

Funcionário: O employee_code é o código do funcionário, o manager_code é o código do seu gerente, o senior_manager_code é o código do seu gerente sênior, o lead_manager_code é o código do seu gerente principal e o company_code é o código da empresa em que trabalha.

Entrada de amostra

Tabela Empresa : Tabela  Lead_Manager : Tabela  Senior_Manager : Tabela  Gerente : Tabela  Funcionário :

Saída de amostra:

C1 Monika 1 2 1 2
C2 Samantha 1 1 2 2
Explicação

Na empresa C1 , o único gerente líder é LM1 . Há dois gerentes seniores, SM1 e SM2 , sob LM1 . Há um gerente, M1 , sob o gerente sênior SM1 . Há dois funcionários, E1 e E2 , sob o gerente M1 .

Na empresa C2 , o único gerente líder é LM2 . Há um gerente sênior, SM3 , sob LM2 . Há dois gerentes, M2 e M3 , sob o gerente sênior SM3 . Há um funcionário, E3 , sob o gerente M2 , e outro funcionário, E4 , sob o gerente M3 .


SELECT A.COMPANY_CODE,
       B.FOUNDER,
       A.QTD_LEAD_MANAGER,
       A.QTD_SENIOR_MANAGER,
       A.QTD_MANAGER,
       A.QTD_EMPLOYEE
    FROM (SELECT DISTINCT(A.COMPANY_CODE) COMPANY_CODE ,
                 COUNT(DISTINCT A.LEAD_MANAGER_CODE) QTD_LEAD_MANAGER,
                 COUNT(DISTINCT A.SENIOR_MANAGER_CODE) QTD_SENIOR_MANAGER,
                 COUNT(DISTINCT A.MANAGER_CODE) QTD_MANAGER,       
                 COUNT(DISTINCT A.EMPLOYEE_CODE) QTD_EMPLOYEE
              FROM Employee A
            GROUP BY A.COMPANY_CODE) A
    JOIN COMPANY B ON A.COMPANY_CODE = B.COMPANY_CODE;