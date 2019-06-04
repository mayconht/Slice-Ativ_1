Copiar os Vagrantfile com as configuraoes necessarias

** Vagrant status
 - ele vai reconhecer as configs dos arquivos.

** Vagrant up
 - Vai subir as maquinas.

** vagrant ssh {VM Name}
 - Vai acessar a VM.

** Executar as configuracoes do Docker (uma unica vez) - Master

sudo apt -y install apt-transport-https ca-certificates curl gnupg-agent software-properties-common;
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -;
sudo apt-key fingerprint 0EBFCD88;
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable";
sudo apt update;
sudo apt -y install docker-ce docker-ce-cli containerd.io;
sudo systemctl start docker;
sudo systemctl enable docker;


** MASTER
sudo docker swarm init --advertise-addr 192.168.2.100:2377

Este é o worker 
docker swarm join --token SWMTKN-1-4wow9anl8wnij4910g7rmbuwx2toaeynvi76etwacdxo6qa0pt-5gej1p8uhqhewbciw6zsd69x6 192.168.2.100:2377



