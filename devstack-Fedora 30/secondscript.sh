#!/bin/bash
set -v
sudo hostnamectl set-hostname myhost.mydomain
sudo hostnamectl set-hostname --transient myhost.mydomain
sudo sed -i "127.0.0.1 myhost.mydomain" /etc/hosts
rpm -qa | grep firewalld
sudo systemctl disable firewalld
sudo systemctl stop firewalld
sudo dnf -y remove firewalld
sudo dnf -y install iptables-services
sudo systemctl enable iptables
sudo systemctl start iptables
sudo dnf -y install git vim tmux
sudo dnf -y update
