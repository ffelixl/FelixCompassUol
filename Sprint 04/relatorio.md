# Sprint 04

### Orientador: Aristides Henrique

Na sprint 04, foram abordados os assuntos de Programação funcional com Python, Docker e Estatistica descritiva com python 

## Programação funcional com python - principais assuntos abordados:

High orders function, closure, funções lambda, map, filter, reduce, funções imutáveis(max, min, sum, reversed, etc), generators.

Dessa forma, vimos que a programação funcional é importante, principalmente na forma de tratamento dos dados, onde se tem um cuidado redobrado principalmente com dados sensíveis em que se tem a utilização dos mesmos em diversas partes do código, ou seja, caso tenha-se o compartilhamento do mesmo, alterações seram refletidas em outras partes do programa, podendo colapsar o restante do programga e gerar erros, com a prgramação funcional é buscado justamente evitar esses tipos de mudanças nos dados para não acontecer esses erros.

## Docker - principais assuntos abordados:

### Session 01 - Introdução
* O que é o docker
* Instalação do docker

### Session 02 - Trabalhando com containers
* Definição de container e imagem
* Comandos para iniciar, criar, nomear, parar, listar, expor portas, ver logs e remover containers

### Session 03 - Criando imagens 
* Hub do docker para pegar imagens
* Criação de imagem atráves do Docker file e comando build
* Rodando imagem em um container 
* Alteração e renomeamento de imagem criada
* Comandos para remover, copiar aquivos de containers apartir de imagens criadas
* Processamento gasto pelo container rodando
* Comandos para enviar e alterar imagens para o docker hub

### Session 04 - Volumes nos containers
* Criação, renomeação e inspeção de volumes

### Session 05 - Conectando container com networks
* O que são e tipos de networks
* Tipos de driver
* Criação, remoção e listagem de networks
* Conexão com apenas a maquina host, conexão com o mundo externo e conexão com outros containers

### Session 06 - Introdução ao YAML
* O que é, como criar e manipulação de dados no arquivo yaml

### Session 07 - Docker compose
* O que é, como criar compose
* Redes no compose 
* Build de imagens e serviços do compose

### Session 08 - Orquestração com docker Swarm
* O que é o docker swarm e principais conceitos
* Enviando services para nuvem 
* Adicionar e remover nodes no docker swarm 
* Atualizar imagens e craição de redes no swarm 

### Session 09 - Orquestração com Kubernetes
* O que é e principais conceitos do kubernetes
* Criação de pods, remoção e gerencimento de imagens nos mesmos
* Criação de services e de IP para o service
* Atualização e remoção de imagens e services

Portanto, o docker facilita a criação, implantação e gerenciamento de aplicativos usando contêineres. Contêineres permitem que um aplicativo e suas dependências sejam empacotados de forma consistente, isolada e portátil. o docker compose é uma ferramenta que permite definir e gerenciar aplicativos Docker multicontêiner em um único arquivo de configuração. Com ele, é possível especificar a configuração dos serviços, redes e volumes necessários para o aplicativo. o kubernetes é uma plataforma de orquestração de contêineres que automatiza o deployment, escalabilidade e operação de aplicativos em contêineres. Ele gerencia a distribuição de contêineres em um cluster de hosts e oferece funcionalidades avançadas, como autoescalonamento, automonitoramento e autorecuperação. São inumeras as vantagens de se utilizar o docker como: Portabilidade e consistência: Os contêineres garantem que o aplicativo e suas dependências funcionem de maneira consistente em qualquer ambiente, localmente ou em nuvem. Isolamento: Os contêineres oferecem isolamento dos recursos do sistema, evitando conflitos entre aplicativos e possibilitando a execução de múltiplas aplicações no mesmo host. Rápido tempo de inicialização: Os contêineres podem ser iniciados e parados rapidamente, o que acelera os processos de desenvolvimento, teste e implantação. Eficiência de recursos: Os contêineres compartilham o mesmo kernel do sistema operacional, economizando recursos em comparação com máquinas virtuais tradicionais. Gerenciamento simplificado: Docker e outras ferramentas relacionadas facilitam o gerenciamento de aplicativos e a integração contínua, simplificando o ciclo de vida de desenvolvimento e operações.

## Estatística Descritiva com Python:

O curso de estatística descritiva visa criar e abrir nossa mente para uma forma mais abrangente de se enxergar os dados e diversas formas de analisarmos os mesmos, tem-se como principais assuntos os conceitos de estatística, tipos de amostragem de dados, conceitos de medidas de tendencias centrais como media aritmética, mediana, moda, medidas separatrizes, dentre outras. Tem também conceitos de medidas de dispersão como amplitude, desvio médio, desvio padrão e tipos de variâncias. Está contido também no curso conceitos de medidas de assimetria. E também a principal abordagem do curso é a utilização desses conceitos para fazer o processamento de dados e elaboração de gráficos no python à partir da utilização de bibliotecas já existentes que fazem o uso destes conceitos para analisar os dados de forma automática e gerar gráficos a partir dos mesmos.

Na subpasta exercicios está o scrip de todas as atividades da sprint proposta pela udemy

* [Pasta Exercicios]()

### Certificados

* [Conclusão do curso de Python, docker e estatística]()
* [Certificado de conlusão da sprint 04]()