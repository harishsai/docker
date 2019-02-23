# docker
Read me files for docker
Docker - Installation
-----------------------
1. Update Repo
---------------
sudo apt-get update

2. Install packages
--------------------
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common

3. Get GPG Key
---------------
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

4. Add the Repo for Ubuntu
---------------------------

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
   
5. Update repository
---------------------

sudo apt-get update

6. Install the packages
------------------------

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose

7. Post Tasks 
--------------
sudo usermod -aG docker $USER
sudo systemctl enable docker
