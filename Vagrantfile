# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

groups = {
  "masterservers" => ['master'],
  "crafternodes" => ['crafter'],
}

inventory = {
  "master" => {:ip => "192.168.33.15", :cpus => 2, :mem => 4096},
  "crafter" => {:ip => "192.168.33.16", :cpus => 1, :mem => 1024},
}

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  inventory.each_with_index do |(hostname, info), index|
    config.vm.define hostname do |cfg|

      cfg.vm.provider :virtualbox do |vb, override|
        override.vm.box = "ubuntu/trusty64"
        override.vm.network :private_network, ip: "#{info[:ip]}"
        override.vm.hostname = hostname
        vb.name = 'raycrafter-' + hostname
        vb.customize ["modifyvm", :id, "--memory", info[:mem], "--cpus", info[:cpus]]
      end

      # provision nodes with ansible
      if index == inventory.size - 1
        cfg.vm.provision :ansible do |ansible|
          ansible.groups = groups
          ansible.verbose = "v"
          ansible.playbook = "vagrant.yml"
          ansible.limit = 'all'# "#{info[:ip]}" # Ansible hosts are identified by ip
          ansible.ask_vault_pass = true
        end
      end
    end
  end
end
