# Download de Taxas Bacen

Script em python que têm como funcionalidade principal o download das taxas de câmbio bacen.

# Como Utilizar

## Preparação

- Clone ou faça o download dos arquivos desse repositório;
- Instale os requerimentos do projeto utilizando um terminal na pasta em que o projeto está salvo e executa o seguinte comando`pip install -r requirements.txt`
- Salve os arquivos do projeto na mesma pasta;

## Execução

- Execute o arquivo main.py que vai iniciar o script e solicitar algumas informações
  - Dia que você quer buscar as taxas de câmbio
  - Moeda que o usuário deseja buscar as novas informações;
  - Formato e periodicidade das informações
- Após informar essas informações o script vai criar uma pasta com as informações baixadas em excel e vai perguntar ao usuário se mais alguma busca deve ser realizada.

### Caso a solicitação seja feita em uma data na qual não há taxas disponíveis , o script vai retornar um erro e vai solicitar ao usuário uma nova data para execução.
