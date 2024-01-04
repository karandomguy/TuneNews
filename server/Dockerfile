FROM python:3.12-slim

RUN apt-get update -y && \
    apt-get dist-upgrade -y && \
    apt-get install -y && \
    apt-get install build-essential -y \
    supervisor wget unzip

WORKDIR /Desktop/TuneNews/

COPY song_gen.py song_gen.py
COPY main.py main.py
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]