# Project Title

Cockpit installtions on locally

## Getting Started

These instructions will get you cockpit up and running on your local machine for development and testing purposes

### Prerequisites

The cockpit uses docker containers to run the required services - telegraf, grafana, influxdb and mariadb. 
So docker must be installed and running on the development box before proceeding. Make sure the user is also added to the docker group to avoid the following permissions error

### Docker-Installing steps
```
sudo dnf config-manager --add-repo https://download.docker.com/linux/fedora/docker-ce.repo
```
```
sudo dnf install docker-ce
```
```
sudo systemctl enable docker.service
```
```
sudo systemctl start docker.service
```
### Docker-compose installtation
```
sudo dnf install docker-compose
```
### Add user To Docker-group
```
sudo groupadd docker
```
```
sudo usermod -aG docker $USER
```

### Cockpit-script
```
git clone https://github.com/rdo-infra/ci-config/ci-scripts/infra-setup/roles/rrcockpit/files/development_script.sh
```
