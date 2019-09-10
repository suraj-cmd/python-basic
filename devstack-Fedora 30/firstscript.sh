#!/bin/bash
## This Script is used for the initial setting of Devstack on Fedora 30 ## 
sudo sed -i 's/enforcing/disabled/g' /etc/selinux/config /etc/selinux/config
sudo useradd stack
sudo passwd stack  # specify a password
echo "stack ALL=(root) NOPASSWD:ALL" | sudo tee -a /etc/sudoers.d/stack
sudo chmod 0440 /etc/sudoers.d/stack
su - stack
