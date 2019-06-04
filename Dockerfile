FROM ubuntu:latest
RUN apt-get update
MAINTAINER Grupo4 
COPY server.py /home/vagrant/server/Slice-Ativ_1/server.py
EXPOSE  8000
CMD ["python3", "/home/vagrant/server/Slice-Ativ_1/server.py", "-p 8000"]
