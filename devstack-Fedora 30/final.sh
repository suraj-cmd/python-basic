#!/bin/bash
set -v
su - stack
git clone https://opendev.org/openstack/devstack
cd devstack/
git pull https://review.opendev.org/openstack/devstack refs/changes/84/678184/1
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
git show

cat >> local.conf <<EOF
[[local|localrc]]
ADMIN_PASSWORD=secret
DATABASE_PASSWORD=$ADMIN_PASSWORD
RABBIT_PASSWORD=$ADMIN_PASSWORD
SERVICE_PASSWORD=$ADMIN_PASSWORD
HOST_IP=192.168.122.21
EOL
