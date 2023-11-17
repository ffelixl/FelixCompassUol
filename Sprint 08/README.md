# Sprint 08

### Orientador(a): Evandro Rosa

Na sprint 08, demos inicio a parte do desafio final, em que precisamos recuperar dados da api do TMDB ou the movie database e mandar os arquivos json diretamente para nosso data-lake no s3!

## Passa a passo para se chegar no resultado esperado:

* Inicialmente precisamos criar uma conta no site do TMDB que hospeda informações sobre filmes e séries basicamente, para podermos fazer o uso da api e recuperarmos informações sobre os mesmos!

* Logo em seguida fui para a tarefa 1, vimos um exemplo de código de como recuperar dados da api e como utilizar nossas credenciais para poder se utilizar os dados ali presente, o código da tarefa 1 em que se tinha que fazer uma consulta simples junto a api, utilizando nossas credenciais para acesso a mesma está na pasta exercicios!

* Primeiramente foi decidido o filtros que ia utilizar na tarefa 2 para recuperar os filmes, com isso decidi buscar os filmes do genero terror que possui id do genero 27 e que tem linguagem original portuguesa(pt) de 01 de janeiro de 2013 até 31 de dezembro de 2023, ordenados de forma crescente.

* Em seguida fui para realização a tarefa 2 que é um pouco mais robusta. Inicialmente comecei desenvolvendo a partir do código da atividade 1 que já tinha como base e as modificações que deveria utilizar na url lá na api para recuperar as informações de meu interesse. importando as bibliotecas necessárias, utilizando minhas credenciais de acesso a minha conta da aws, em seguida adicionando também minha credencial de acesso a api do tmdb, também foi criado a função trazerPaginasDaApi que basicamente recebe como parametro uma página contendo uma lista de 20 filmes especificados e filtrados de acordo com a url fornecida na função. Em seguida foi criado a função paginasAseremEnviadas que basicamente recebe como parametro a pagina e o intervalo para junção das páginas, que no caso é de 5 em 5 paginas, garantindo assim que cada lote tenha 100 filmes, ou seja 5 x 20 de cada pagina = 100, garantindo o que a tarefa pede de armazenar 100 filmes em cada arquivo json, também contém um for que será responsável por utilizar das bibliotecas datetime e dateutil com a função tz para recuperar a data atual baseado no horário do brasil, como especificado em parámetro no código, assim é processado a data de cada envio de lote para nomeação dos diretorios baseado na data de processamento como pede a questão. Em seguida foi criado a função de enviarPros3 que basicamente recebe como parametro o lote de 100 filmes, o nome do bucket no s3 na conta da aws e o caminho em que o lote de filmes será escrito, dentro da função é instanciado um objeto boto3 da biblioteca boto3 em que chamará a função putobject com os parametros recebidos para enviar os lotes para o s3. Assim a função paginasAseremEnviadas é chamada 5 vezes passando a primeira página e o intervalo para agrupamento e envio de cada lote, conforme está presente no código, garantindo assim 5 lotes de 100 filmes, ou seja 500 filmes no total.

* Depois fui para o meu s3 criar o meu bucket que iria receber os dados.

* Em seguida foi criado a politica (politicaingestordedados) que seria anexada a minha lambda com as permissões miininas ou seja apenas de escrita no s3.

* Em seguida criei a minha lambda, não foi necessário criar layer pois todas as bibliotecas eram nativas do python e suportadas pela aws, embora tenha sido criado um arquivo zip com as bibliotecas necessárias juntamente com o monitor Evandro porém não foi possivel adicionar a layer devido incompatibilidade de versões do python e do sistema do wsl, então ficou sem nenhuma layer mesmo. em seguida adicionada a politica criada na minha lambda.

* Logo em seguida subi o código que tinha feito localmente inicialmente para testes locais na função lambda e com isso demonstrado os resultados conforme o video na pasta de exercicios.

* [Pasta Evidencias](https://github.com/ffelixl/FelixCompassUol/tree/main/Sprint%2008/Evidencias)
* [Pasta Exercicios](https://github.com/ffelixl/FelixCompassUol/tree/main/Sprint%2008/Exercicios)



