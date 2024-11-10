# Projeto de Coleta de Dados Meteorológicos

Este projeto é uma aplicação em Python que realiza web scraping de dados meteorológicos para cinco cidades específicas e salva as informações em um arquivo Excel. A coleta é automatizada para ocorrer a cada 30 minutos, e os dados capturados incluem:

- Temperatura Atual
- Temperatura Mínima e Máxima
- Cidade onde os dados foram coletados
- Horário da coleta
- Condições Climáticas (ex.: ensolarado, nublado, etc.)
- Data da Coleta (adicionada automaticamente fora do processo de scraping)

Esses dados são salvos e atualizados continuamente para permitir a análise do histórico meteorológico das cidades selecionadas.

## Funcionalidades

- **Coleta Meteorológica para Múltiplas Cidades**: Utiliza a biblioteca **BeautifulSoup** para realizar o scraping de dados meteorológicos do site https://weather.com/ para cinco cidades previamente definidas.
- **Coleta Automática a Cada 30 Minutos**: Utiliza a biblioteca **Schedule** para realizar coletas automáticas em intervalos regulares de 30 minutos.
- **Exportação para Excel**: Utiliza a biblioteca **Pandas** para salvar e atualizar os dados em um arquivo .xlsx, permitindo o armazenamento estruturado para fácil consulta e análise.

## Funcionalidade Futura

- **Pesquisa Dinâmica por Cidade**: Com a implementação do **Selenium**, a aplicação poderá pesquisar e coletar dados de qualquer cidade que o usuário definir.
