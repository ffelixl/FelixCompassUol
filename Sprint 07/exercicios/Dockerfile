FROM python:3.8

RUN apt-get update && apt-get install -y \
    python3-pip \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /data
RUN pip install --upgrade pip

WORKDIR /app

COPY ingestorDeDados.py /app/ingestorDeDados.py
COPY movies.csv /data/movies.csv
COPY series.csv /data/series.csv

RUN pip install boto3 pandas

CMD ["python", "/app/ingestorDeDados.py"]

