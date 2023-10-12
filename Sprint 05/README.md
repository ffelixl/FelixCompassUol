# Sprint 05

### Orientador(a): Camila Munzlinger

Na sprint 05, foram abordados os assuntos de Principais conceitos de computação em nuvem, os principais conceitos e serviços da AWS e técnica de vendas de serviços da nuvem 

## AWS Partner: Business - Principais pontos abordados:

O primeiro curso aborda os principais conceitos de computação na nuvem como:
* Maquinas virtuais
* Conteinerização
* Utilização dos serviços sem servidor
* E também conceitos de arquitetura on-premisses que é a computação tradicional com maquinas e servidores físicos, arquitetura de computação em nuvem e o hibrido que seria a implementação desses dois modos juntos.
Os principais tipos de serviços que a nuvem oferece é O IaaS ou infraestrutura como serviço é possível a virtualização, ou seja, fornecimento de maquinas virtuais, armazenamento e rede, os usuários tem controle sobre o sistema operacional e aplicativos sem se preocupar com questões de hardware. O PaaS ou plataforma como serviço garante o oferecimento de uma plataforma completa de desenvolvimento e implantação de aplicativos como um sistema operacional especifico, banco de dados, servidor web etc. E o SaaS, software como serviço, garante apenas o software em especifico e o usuário final irá apenas utilizá-lo, sem se preocupar com criação, manutenção ou atualização do mesmo.
* O conceito de ruptura de aplicativos, ou seja, de um aplicativo monolítico e robusto para microserviços também é abordado no curso.
* Valor comercial - O valor comercial é entender o que impulsiona a adoção da nuvem, por que isso é importante para os clientes e os resultados tangíveis que as empresas podem alcançar.
* Cloud framework - estrutura conceitual destinada a criar um caso de negócio abrangente para a adoção da nuvem e ajuda a articular o valor da adoção da nuvem. Ele faz isso medindo e rastreando o progresso dos clientes que migraram para a AWS em relação a quatro pilares principais de valor:
  * Economia de custo
  * Produtividade da equipe
  * Resiliência operacional
  * Agilidade empresarial

* É realizado o comparativo dos valores desses 4 pilares antes e após a migração para a nuvem para se obter uma estimativa de quanto em questão de melhoras a empresa conseguiu/conseguirá.
* Objeções para migração para a nuvem também é abordado, é importante para adquirir conhecimentos para lidar com as possíveis objeções dos clientes. lá está contido as principais objeções como: 
  * Custo
  * Segurança e privacidade
  * Visibilidade ou perda de controle
  * Infraestrutura on-premisses já existente
  * Habilidades inexistentes
  * Atrelamento a somente um fornecedor
  * Sustentabilidade ambiental
* Venda conjunta – trata-se da parceria entre a aws e os aws partners que trabalham em conjunto para assim criar a solução para cada cliente. AWS marketplace é um catalogo digital que ajuda os clientes buscarem soluções para o que ele procura com base no desenvolvimento de aws partners.



## Cloud Quest – Cloud Pratictioner:

Esta parte consiste-se em um jogo que busca aprofundar os conhecimentos acerca dos principais conceitos e serviços da AWS, além de familiarizar-se com ambiente da nuvem e da AWS. O jogo foi um divisor de águas em que podemos quebrar toda a parte conceitual e aprender sobre os principais serviços de uma forma divertida e prática.
Lista das atividades e dos principais conceitos abordados:
01. EC2 – como criar e subir um servidor na nuvem.
02.	Availability zones - Aprendemos como criar instâncias de servidores em determinadas zonas de disponibilidade.
03.	Alteração e criação de EC2 de diferentes tipos - aprendemos como criar ou mudar um servidor para um tipo de servidor diferente com mais ou menos poder computacional de acordo com nossas demandas.
04.	Conceitos de VPC – virtual private cloud ou rede intranet e extranet, aprendemos como configurar apenas uma rede intranet isolada de outra, aprendemos também como configurar para uma aplicação se comunicar com outra através de um tipo de conexão TCP por exemplo através de uma porta especifica, na atividade em especifico foi conectado um servidor web que está em uma sub-rede pública para se comunicar com a internet através do protocolo http pela porta 80 e também conectar esse servidor web em outra intranet privada de um banco de dados que se comunica através do protocolo TCP pela porta 3306. Tudo isso através dos grupos de segurança, permitindo ou negando acessos.
05.	Conceitos de VCP peering – Para conectar instancias de servidores e poder compartilhar trafego entre os mesmos através de endereços ipv4 ou ipv6
06.	Conceitos de bancos e seus tipos de instancias – Aprendemos como criar determinados tipos de bancos de dados e com determinado poder computacional para a instancia do mesmo. Além de criar também replicas do mesmo em regiões diferentes e que estão sincronizados.
07.	Conceitos de sistema de arquivos compartilhado através do amazon EFS – Aprendemos como criar instancias que através de um sistema de arquivos podem compartilhar dados/arquivos.
08.	Conceitos do banco de dados dynamoDB – aprendemos conceitos do banco de dados não relacional dynamoDB em que podemos adicionar ou excluir dados de forma rápida e pratica.
09.	Conceitos de AutoScalingGroup – aprendemos como escalar nossa aplicação através do auto scaling group, podendo aumentar ou diminuir o numero de servidores da nossa aplicação de acordo com a demanda ou horário conforme especificado pela gente na hora de criarmos nosso grupo de auto scaling. Além de criarmos a rede para atribuirmos ela para cada instancia que será criada dinamicamente.
10.	Conceitos de aws pricing calculator – aprendemos como estimar nossos gastos através do serviço aws pricing calculator especificando quantas e quais tipos de instancias serão utilizadas e por quanto tempo, para realizar um balanço de quais serão nossos gastos diariamente, semanalmente, mensalmente e anualmente.
11.	Conceitos de IAM ou identity and access management – aprendemos como criar grupos de acesso e quais serão suas permissões e quais serviços da aws estarão disponíveis para cada grupo, além de criar usuários e senhas para cada usuário do grupo.
12.	Conceitos de ELB ou elastic load balance – aprendemos como criar instancias em zonas diferentes, configurar suas redes e através do ELB configurar para o trafego da aplicação ser direcionado para ambas as instancias diferentes, evitando assim sobrecarga de servidores. Além de usar também o auto scaling group para criar instâncias automaticamente de acordo com nossa demanda ou horário, para fazer com nossa aplicação torne-se também altamente disponível.

O jogo serviu para nos nortear sobre os principais serviços da aws, alguns conceitos de rede tiveram que ser relembrados para facilitar o aprendizado, mas tudo se encaminhou perfeitamente para uma melhor aprendizagem e melhor aproveitamento da sprint.
Na pasta evidencias estarão todos os prints de implementações e respostas.


## AWS Partner - Aspectos econômicos da Cloud:

O curso Trata-se de uma abordagem mais aprofundada sobre os conceitos de valor comercial e sobre o cloud value framework e os seus 5 pilares de grande importância.
* A redução de custos é realizada evitando as infraestruturas on-premises com grandes gastos fixos e reduzindo a variável de gastos contínuos usando as economias de escala das ofertas da AWS.
* A produtividade da equipe é medida em resultados maiores pela equipe do mesmo tamanho porque muito do trabalho tático anterior não é mais necessário.
* A resiliência operacional é conquistada com maior disponibilidade e segurança e menor tempo de inatividade.
* A agilidade empresarial consiste nos novos produtos, nas novas expansões de geolocalização ou de mais recursos dos produtos existentes que os clientes podem fornecer.
* A sustentabilidade é a redução do impacto ambiental das operações de TI.


## AWS Partner - Accreditation (Technical):

O curso aborda de uma forma pratica a conversa entre Maria que seria uma revendedora de serviços a partir dos parceiros da aws e um cliente que está querendo migrar seus serviços para a nuvem. No curso é abordado novamente conceitos arquitetura on-premisses e arquiteturas na nuvem. Além dos principais benefícios de utilização de computação na nuvem como agilidade, elasticidade, economia de custo e implantação global de uma aplicação em questão de minutos. Também é abordado novamente os conceitos de região da aws e zonas de disponibilidade. 
* Também é apresentado os principais serviços computacionais da aws como: 
  * EC2 – serviço computacional de fácil redimensionamento ou servidores que podem ser criados de acordo com suas especificações computacionais e sistemas operacionais de sua escolha. 
  * EC2 AutoEscaling – que serve para criar ou diminuir o número de instancias EC2 de acordo com gatilhos.
  * ELB ou Elastic load balancing - que distribui automaticamente o trafego de entrada dos aplicativos em diversos destinos.
  * Amazon container service ou ECS – é um serviço de gerenciamento de contêineres de alta capacidade se dimensionamento e performance que aceita contêineres do Docker e permite que clientes executem facilmente aplicativos em um cluster gerenciado.
  * Aws lambda – Serviço computacional que executa código sem a necessidade de provisionar ou gerenciar servidores.
* Também é abordado os principais serviços de armazenamento da aws como:
  * amazon elastic block store - funciona com um disco rígido para instancias EC2 podendo formatar, particionar e instalar SOs neles, armazenamento persistente a nível de bloco.
  * Amazon S3 simple storage service – é o armazenamento da internet para armazenar e recuperar dados de qualquer lugar da web.
  * Aws storage gateway - fornece integração entre um ambiente on-premisses e o armazenamento aws para transferência de dados para dentro e para fora da nuvem aws.
  * Amazon Elastic file system ou EFS – serviço de armazenamento de arquivos que aumenta ou diminui conforme sai ou entra arquivos usado para instancias do EC2.
* Os serviços de bancos de dados como:
  * amazon rds ou relational database service - que oferece o gerenciamento de um serviço abordando os principais bancos de dados relacionais como aurora, PostgreSQL, mySQL, MariaDB entre outros.
  * Amazon dynamoDB – que é um banco de dados não relacional de fácil gerenciamento.
  * Amazon elastiCache – serviço que permite criar e dimensionar um cache na nuvem para recuperação rápida de dados que melhora o tempo de servidores web por exemplo.
* Também se aborda os principais serviços de rede da aws como:
  * Amazon virtual cloud private ou VPC – que cria uma rede virtual na nuvem com recursos avançados como grupo de segurança que controla o acesso as instancias e listas de controle de acesso a rede (NACL) que controla o acesso as sub-redes.
  * Amazon route 53 – serviço de DNS altamente dimensionável que direciona os usuários finais para aplicativos da internet convertendo nomes legíveis em endereços IPs.
No curso também se aborda como lidar com as objeções do cliente de Maria, além de fases que devem ser seguidas para compreender os problemas do cliente e apresentar uma solução condizente com os problemas do cliente e apresentar uma POC (prova de conceito) em que o cliente analisará a solução em seu ambiente testando a mesma. Também está presente conceitos de benefícios e recursos da rede de parceiros da aws o aws partner network. Tudo isso para um planejamento da migração para a nuvem eficaz e de acordo com as demandas dos clientes. 


Na subpasta evidencias estará todos os prints de teste no ambiente da aws e respostas das atividades do jogo.

* [Pasta Evidencias](https://github.com/ffelixl/FelixCompassUol/tree/main/Sprint%2005/evidencias)

### Certificados

* ![Conclusão do curso 01](https://github.com/ffelixl/FelixCompassUol/blob/main/Sprint%2005/certificados/certificado1.pdf)
* [Conclusão do curso 02]()
* [Conclusão do curso 03]()
* [Conclusão do curso 04]()
* [Conclusão do curso 05]()