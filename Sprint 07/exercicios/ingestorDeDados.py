import boto3
import os
from datetime import datetime

# Configurações AWS
AWS_REGION = 'us-east-1'
AWS_ACCESS_KEY_ID = 'AKIATNF37AF7PL2GRKHP'
AWS_SECRET_ACCESS_KEY = '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'

# Nome do bucket S3 e a pasta no bucket para a camada RAW
BUCKET_NAME = 'ingestordados'
RAW_PATH = 'Raw/Local/CSV'

# Diretório local onde os arquivos CSV estão localizados dentro do container
LOCAL_DIRECTORY = '/data'

# Inicializa o cliente S3
s3 = boto3.client('s3', region_name=AWS_REGION, aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)

# Cria um diretório no S3 com base na data de processamento
current_date = datetime.now()
s3_directory = f'{RAW_PATH}/{current_date.year}/{current_date.month:02d}/{current_date.day:02d}'

# Lista dos arquivos CSV a serem carregados
files_to_upload = os.listdir(LOCAL_DIRECTORY)

# Para cada arquivo na lista, faça o upload para o S3
for file_name in files_to_upload:
    # Define o caminho no S3 para o arquivo
    s3_key = f'{s3_directory}/{file_name}'

    # Faz o upload do arquivo local para o S3
    s3.upload_file(os.path.join(LOCAL_DIRECTORY, file_name), BUCKET_NAME, s3_key)

    print(f'Arquivo {file_name} carregado com sucesso para o S3 em s3://{BUCKET_NAME}/{s3_key}')
