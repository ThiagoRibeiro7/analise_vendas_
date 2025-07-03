import pandas as pd

funcionarios_df = pd.read_csv('CadastroFuncionarios.csv', sep=';', decimal=',')
clientes_df = pd.read_csv('CadastroClientes.csv', sep=';', decimal=',')
servicos_df = pd.read_excel('BaseServiçosPrestados.xlsx')

#retirando as colunas Estado Civil e Cargo da tabela de funcionarios
funcionarios_df = funcionarios_df.drop(['Estado Civil', 'Cargo'], axis=1)

display(funcionarios_df)
display(clientes_df)
display(servicos_df)

#Folha Salarial
funcionarios_df['Salario Total'] = funcionarios_df['Salario Base'] + funcionarios_df['Impostos'] + funcionarios_df['Beneficios'] + funcionarios_df['VT'] + funcionarios_df['VR']
print('Total da Folha Salarial Mensal é de R${:,}'.format(funcionarios_df['Salario Total'].sum()))

#Faturamento da Empresa
faturamentos_df = servicos_df[['ID Cliente', 'Tempo Total de Contrato (Meses)']].merge(clientes_df[['ID Cliente' ,'Valor Contrato Mensal']], on='ID Cliente')
faturamentos_df['Faturamento Total'] = faturamentos_df['Tempo Total de Contrato (Meses)'] * faturamentos_df['Valor Contrato Mensal']
print('Faturamento Total: R${:,}'.format(sum(faturamentos_df['Faturamento Total'])))

# % dos Funcionarios Fecharam Contrato
qtde_funcionario_fecharamcontrato = len(servicos_df['ID Funcionário'].unique())
qtde_funcionario_total = len(funcionarios_df['ID Funcionário'])
print('Percentual Funcionários Fecharam Contrato: {:.2%}'.format(qtde_funcionario_fecharamcontrato / qtde_funcionario_total))

#Quantidade de Contratos por Área
contratos_area_df = servicos_df[['ID Funcionário']].merge(funcionarios_df[['ID Funcionário', 'Area']], on='ID Funcionário')
contratos_area_qtde = contratos_area_df['Area'].value_counts()
print(contratos_area_qtde)
contratos_area_qtde.plot(kind='bar')

#Funcionários por Área
funcionarios_area = funcionarios_df['Area'].value_counts()
print(funcionarios_area)
funcionarios_area.plot(kind='bar')

#Ticket Médio  Mensal
ticket_medio = clientes_df['Valor Contrato Mensal'].mean()
print('Ticket Médio Mensal: R${:,.2f}'.format(ticket_medio))