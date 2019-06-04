# -*- mode: ruby -*-
# vi: set ft=ruby :
#Esse codigo vai criar as duas vms com configuracao basica do vagrant

Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: "Tamo butano pra fude!!!"

  config.vm.define "Master" do |vm1|
    vm1.vm.box = "ubuntu/bionic64"
    vm1.vm.hostname = "Master"
    vm1.vm.network "private_network", ip: "192.168.2.100"
  end

  config.vm.define "Worker" do |vm2|
    vm2.vm.box = "ubuntu/bionic64"
    vm2.vm.hostname = "Worker"
    vm2.vm.network "private_network", ip: "192.168.2.101"
  end
end