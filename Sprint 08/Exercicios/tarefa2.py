import boto3
import json
from urllib.request import urlopen, Request
from datetime import datetime
from dateutil import tz

# Configurações AWS
AWS_REGION = 'us-east-1'
AWS_ACCESS_KEY_ID = 'AKIATNF37AF7PL2GRKHP'
AWS_SECRET_ACCESS_KEY = '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'

#chave de API do TMDb
api_key = 'e32e0ce30c0a4728663eeada48d1c2cf'

# Função para fazer chamadas à API do TMDb
def trazerPaginasDaAPI(page):
    url = f'https://api.themoviedb.org/3/discover/movie?api_key={api_key}&include_adult=false&include_video=false&language=en-US&page={page}&primary_release_date.gte=2013-01-01&primary_release_date.lte=2023-12-31&sort_by=primary_release_date.asc&with_genres=27&with_original_language=pt'
    request = Request(url)
    response = urlopen(request)
    
    if response.getcode() == 200:
        return json.loads(response.read().decode('utf-8'))
    return None

# Função para enviar dados para o S3
def enviarPros3(data, bucket_name, file_key):
    s3 = boto3.client('s3', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    s3.put_object(Body=json.dumps(data), Bucket=bucket_name, Key=file_key)
    print(f"Dados enviados para o S3: {file_key}")

# Função para calcular o tamanho de um objeto em bytes
#def get_size(obj):
   #return sys.getsizeof(obj)

# Iteração pelas páginas para obter os dados
def paginasASeremEnviadas(page, intervalo):
    movies_data = []
    while page <= intervalo:  #iterando pelas primeiras 25 páginas
        data = trazerPaginasDaAPI(page)
        if data:
            movies_data.extend(data['results'])
        page += 1

        # Imprimir os resultados de cada página
        print(f"Resultados da página {page - 1}:\n")
        print(data)  # Imprime os dados da página
        print(len(data['results'])) #saber o numero de filmes por pagina
        print('\n')

    #dividindo em lotes de 100 registros cada, assim o batched_data terá uma lista de listas contendo 100 filmes no total
    batched_data = [movies_data[i:i + 100] for i in range(0, len(movies_data), 100)]
    print(batched_data)

    # Enviar cada lote para o S3
    for i, batch in enumerate(batched_data):
        
        # Estruturar o caminho do arquivo no S3 com base na data de processamento
        timezone = tz.gettz('America/Recife')
        current_time = datetime.now(timezone)
        ano = current_time.strftime('%Y')
        mes = current_time.strftime('%m')
        dia = current_time.strftime('%d')

        # Montar o path do arquivo
        file_path = f'raw/tmdb/json/{ano}/{mes}/{dia}/file_{intervalo-4}-{intervalo}.json'
        enviarPros3(batch, 'data-lake-do-felix', file_path)  # Substitua 'seu-bucket-s3' pelo nome do seu bucket
        print(f"Enviando dados para o S3: {file_path}")

    #total de registros coletados
    print(f"Total de registros coletados: {len(movies_data)}")
    print(f"Total de registros coletados: {len(batched_data)}")

#print(get_size(batched_data))

paginasASeremEnviadas(1, 5)
paginasASeremEnviadas(6, 10)
paginasASeremEnviadas(11, 15)
paginasASeremEnviadas(16, 20)
paginasASeremEnviadas(21, 25)
