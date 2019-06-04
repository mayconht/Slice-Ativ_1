FROM ubuntu:latest
RUN apt-get update
MAINTAINER Grupo4 
# Update
RUN apk add --update python py-pip
# Install app dependencies
RUN pip install Flask
# Bundle app source
COPY server.py /home/vagrant/server/Slice-Ativ_1/server.py
EXPOSE  8000
CMD ["python3", "/home/vagrant/server/Slice-Ativ_1/server.py", "-p 8000"]
