FROM python:2.7
LABEL version="1.0.0" description="Server Grupo 4" maintainer="grupo 4"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /Slice-Ativ_1
WORKDIR /Slice-Ativ_1
ENTRYPOINT ["python"]
CMD ["server.py"]
