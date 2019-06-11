Jaime Leite
Maycon Douglas
William Soares


Acessando o servidor da faculdade:
    com o git instalado no windows e/ou linux. (recomendo usar Ubuntu for windows)

    git clone https://github.com/dcomp-leris/slice-enablers.git
    cd slice-enablers
    cd arquivos
    chmod 400 cloud_ufscar_rsa.dms
    ssh -i cloud_ufscar_rsa.dms ubuntu@200.136.252.136
    sh acessar.sh 4

    ***Não se esqueça de usar SUDO para os comandos***

Instalando o Vagrant no computador Pessoal/Faculdade:
    Linux:
        sudo apt update
        sudo apt -y install virtualbox
        sudo apt -y install vagrant
    Windows:
        Download https://www.vagrantup.com/downloads.html
        Download https://www.virtualbox.org/wiki/Downloads
        Instalar usando UI.

Criar o Vagrant File, que vai proporcionar todas as configs.
        Vide vagrant file nesta mesma pasta
        
Copiando os arquivos para o servidor (ja executado no servidor da ufscar na raiz do grupo 4)
    git clone https://github.com/mayconht/Slice-Ativ_1.git
    cd Slice-Ativ_1

Verificando se o Vagrant reconhece as VM's
    vagrant status
    **Ele deverá exibir a vm Worker e a VM Master (case sensitive)**
    vagrant up
    **As maquinas irão subir e fazer os downloads necessários**

Conectando nas maquinas Vagrant (recomendo trabalhar com 1 por vez)
    **Janela 1**
        vagrant ssh Master
    **Janela 2**
        vagrant ssh Worker

Executando as configuraçoes nas VM'se
    **Janela 1 e 2**
        sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common; curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -; sudo apt-key fingerprint 0EBFCD88; sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"; sudo apt update; sudo apt -y install docker-ce docker-ce-cli containerd.io; sudo systemctl start docker; sudo systemctl enable docker;
    **Janela 1 - Master**
        sudo docker swarm init --advertise-addr 192.168.2.100:2377
        (Salve o resultado, vai ser necessario na Worker)
        exit
    **Janela 2 - Worker**
        sudo docker swarm join --token <Adicionado Token gerado no Master>
        (voce deverá ver a mensagem This node Joined a swarm as a worker)

Subindo aplicativo no docker na Master
    **Janela 1  - Master**
        git clone https://github.com/mayconht/Slice-Ativ_1.git
        sudo apt install docker
        cd Slice-Ativ_1
        sudo docker build -t server:latest .
        (vc deverá ver a mensagem: Successfully built)
        docker images
        docker ps
        sudo docker run -d -p 5000:5000 server:latest

testando localmente o server
    curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"reqtime": "this is our second test","contname": "ServerCont","contid": "1545730073", "imgid": "1545730073","cpu": "20%","memory": "6%"}'  http://localhost:5000/POST_INFO
    curl http://localhost:5000/GET_INFO

