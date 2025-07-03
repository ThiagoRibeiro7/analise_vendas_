#Analise de Dados com Pandas

Descrição do Problema: Fazer a análise dos dados a seguir fazendo os cálculos para cada uma das situações;
Temos os dados de 2019 de uma empresa de prestação de serviços. 
- CadastroFuncionarios
- CadastroClientes
- BaseServiçosPrestados

O que devo calcular:
- Valor Total da Folha Salarial -> Qual foi o gasto total com salários de funcionários pela empresa?
( Calculei o salário total de cada funcionário, salário + benefícios + impostos, depois somei todos os salários )

- Qual foi o faturamento da empresa?
Calculei o faturamento total de cada serviço e depois somei o faturamento de todos

- Qual o % de funcionários que já fechou algum contrato?

Obs: na base de serviços temos o funcionário que fechou cada serviço. Mas nem todos os funcionários que a empresa tem já fecharam algum serviço.
Na base de funcionários temos uma lista com todos os funcionários
Calculei Qtde_Funcionarios_Fecharam_Serviço / Qtde_Funcionários_Totais
Para calcular a quantidade de funcionários que fecharam algum serviço, usei a base de serviços e contei quantos funcionários tem, lembrando que cada funcionario só pode ser contratado uma única vez.
Apliquei o método .unique()

-  Calculei o total de contratos que cada área da empresa já fechou

-  Calculei o total de funcionários por área

-  Qual o ticket médio mensal (faturamento médio mensal) dos contratos?
Usei o método .mean() que calcula a média

Resultados:
Folha Salarial:
- Total da Folha Salarial Mensal é de R$2.717.493,22

Faturamento da Empresa:
- Faturamento Total: R$5.519.160

% Funcionários que Fecharam Contrato
- Percentual Funcionários Fecharam Contrato: 86.84%

Quantidade de Contratos por Área:
-
Administrativo    63
Operações         48
Comercial         44
Financeiro        42
Logística         40

Funcionários por Área:
-
Comercial         26
Administrativo    26
Operações         23
Logística         21
Financeiro        18

Ticket Médio Mensal:
- Ticket Médio Mensal: R$2.502,56
