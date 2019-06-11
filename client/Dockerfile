FROM ubuntu:latest
LABEL version="1.0.0" description="Server Grupo 4" maintainer="grupo 4"
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
EXPOSE 5000
COPY . /Slice-Ativ_1/client
WORKDIR /Slice-Ativ_1/client
RUN pip install flask
ENTRYPOINT ["python"]
CMD ["client.py"]