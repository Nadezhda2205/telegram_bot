FROM python:3.9
WORKDIR /app
RUN apt-get update -y
RUN apt-get upgrade -y
COPY . ./src
RUN pip install --upgrade pip
RUN pip install -r src/requirements.txt
CMD python src/main.py