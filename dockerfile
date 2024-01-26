#Dockerfile utilizado para subir o jenkins e instalar o docker com suas dependências
FROM jenkins/jenkins:lts
USER root
RUN apt-get update && \
    apt-get install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common && \
    curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y 

# Create a new group named dockergroup
RUN groupadd dockergroup

# Add the jenkins user to the dockergroup
RUN usermod -aG dockergroup jenkins

# Add the dockergroup to the Docker group
# RUN usermod -aG docker dockergroup

#USER jenkins
