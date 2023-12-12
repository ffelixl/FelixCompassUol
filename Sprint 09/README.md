# Sprint 09

### Orientador(a): Isabela Braga

Na sprint 09, foram utilizados os conceitos spark e ETL para preparação dos dados extraidos na sprint08 para geração de insights na proxima sprint!

## Primeiros exercicios:

* Seção 02 - modelagem relacional e dimensional:
  * Tarefa 01 - Inicialmente fomos revisar os conceitos de modelagem relacional e o modelo entidade relacionamento em seguida fomos realizar a atividade de aplicar as 3 formas normais no Banco de Dados disponibilizado na atividade, para assim garantir que o mesmo esteja dentro dos padrões das 3 formas normais ou 3FN. Então separei a única tabela tb_locacao em 4 tabelas, locacao, carro, cliente e vendedor. Na tabela locacao criei as chaves estrangeiras para junção com as outras tabelas citadas anterior, uma chave estrangeira para a tabela carro, uma para a tabela cliente e outra para a tabela vendedor, e assim separei os atributos que fazem mais sentido estar em cada tabela, de acordo com o digrama entidade e relacionamento na pasta evidencias.

  * Tarefa 02 - Em seguida realizei a leitura sobre a modelagem dimensional e seus conceitos, para realizar a segunda atividade que seria apartir da modelagem relacional aplicando as 3FN aplicar os conceitos de modelagem dimensional para poder analisar os dados de diferentes perspectivas. Com isso criei uma tabela de fatolocacao e outras 4 tabelas de dimensões da tabela fato, as 4 tabelas de dimensões são dimCliente, dimTempo, dimVendedor e dimCarro também separei alguns atributos para cada tabela como faz mais sentido para a modelagem dimensional.
   

## Desafio parte 03 - Lab Aws:

* Seção 03 - Processos de ETL:
  * Tarefa 03 e 05 - na tarefa 03 realizei o processamento da camada trusted em que se consiste em pegar os dados descentralizados que recuperamos na sprint 08 do monitor Evandro, organiza-los para melhor visualização e eliminação de valores nulos e tratamentos de valores em branco. Com isso recuperei os arquivos json gerados na sprint citada e realizei a organização dos mesmos através do framework spark gerando um dataframe com as colunas selecionadas, também adicionei um método de obter o id do imdb que eu não havia recuperado na sprint anterior para caso eu precise na próxima sprint para conectar minha tabela com outra fonte de dados, com isso com base em cada id do tmdb é chamado o método obter_id_imdb que faz nova requisição a api do tmdb para recuperar o id do imdb para cada id presente no meu dataframe, logo apos realizei o método de contar valores nulos em cada coluna para realizar o tratamento caso houvesse, como selecionei apenas algumas colunas especificas que julguei necessárias para minha análise não houve valores nulos no meu dataframe, também verifiquei se os dados estavam com tipo correto em cada coluna e alterei algumas colunas para o tipo correto de acordo com o código "job2final.py" presente na pasta exercícios, esses últimos procedimentos de eliminação de colunas irrelevantes e alteração de tipos de dados são feitos normalmente na camada refined, porem como já havia realizado essas operações na primeira camada a trusted de forma intuitiva não precisei realizar novamente na refined, mas o certo mesmo seria a separação dos processos em seus estágios específicos, também perguntei para a monitora da sprint referente se poderia fazer desta forma. Com isso agrupei os meus filmes recuperados na sprint anterior em um dataframe só que antes estavam fracionados para assim escreve-los no meu bucket no s3 em formato parquet.
  * Tarefa 03 e 05 - Também fiz o uso de dados de oscars disponibilizado pela monitora da sprint, fazendo a leitura do arquivo que estava em formato xlsx em seguida convertendo para um dataframe do spark e realizando os mesmos procedimentos citados no item anterior de verificação de valores nulos, renomeação e alteração dos tipos de dados de algumas colunas e escrita em formato parquet no meu s3.
  * Tarefa 03 e 05 - Também utilizei os dados de atores que foram disponilizados na sprint 07 da monitora Dilmara para realizar analises com base nos meus filmes recuperados na sprint do Evandro para poder abrir meu leque de consultas e mostrar a integração de diversas fontes de dados podendo gerar diversos tipos de insights, o arquivo inicialmente estava em csv que também foi lido e refeito os procedimentos das camadas trusted e refined para melhor organização e consulta nos dados.
  * Com isso feito os devidos processamentos e tranformações nos arquivos e salvos em formato parquet criei 3  banco de dados no meu catalogo do glue e utilizei crawlers para cada DB para catalogar os dados, definir meus esquemas e formato de dados de cada tabela e assim poder visualizar os dados no athena e fazer consultas nas minhas tabelas.

 
* Tarefa 04 - na tarefa 04 foi realizado a modelagem dimensional com base nas minhas tabelas de filmes, atores e oscars. criando uma tabela fatofilmes com dimensão dim_sobre_filmes que contem informações referente de cada filme, também criei a tabela fatoOscars com a dimensão dim_status_oscars que contém informações sobre os prêmios de oscars e categorias, também criei a dimensão atores que contém informações sobre cada autor sendo uma dimensão da fato oscars.

Na subpasta evidencias estará todos os prints de respostas das atividades e a realização das mesmas!!
Na subpasta exercicios estará os scripts das atividades e outros arquivos necessários!!

* [Pasta Evidencias](https://github.com/ffelixl/FelixCompassUol/tree/main/Sprint%2009/evidencias)
* [Pasta Exercicios](https://github.com/ffelixl/FelixCompassUol/tree/main/Sprint%2009/exercicios)

### Certificados

* [Conclusão da sprint](https://github.com/ffelixl/FelixCompassUol/blob/main/Sprint%2009/Certificados/certificado%20sprint09.pdf)


