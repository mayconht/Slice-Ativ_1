FROM ubuntu
LABEL version="1.0.0" description="Server Grupo 4" maintainer="grupo 4"
RUN cd / && mkdir Server && chmod 777 -R Server/
COPY ./vagrant/server.py /Server/
VOLUME /Server/
EXPOSE 5000
ENV POST=http://localhost:5000//POST_INFO
ENV GET=http://localhost:5000//GET_INFO
WORKDIR /Server
ENTRYPOINT ["/Server"]
CMD ["python3", "Server.py"]
