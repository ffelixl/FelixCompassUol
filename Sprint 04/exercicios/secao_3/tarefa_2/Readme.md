# É possível reutilizar containers? Em caso positivo, apresente o comando necessário para reiniciar um dos containers parados em seu ambiente Docker? Não sendo possível reutilizar, justifique sua resposta.

## sim, é possivel através do comando **docker ps -a** você poderá ver todos os containeres que já foram executados.
## incluindo seus <id>, com isso você porderá utilizar o comando **docker start -i <id>** com o id do container que você quiser executar.