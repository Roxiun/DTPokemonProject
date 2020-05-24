#!/usr/bin/env bash

apt-get update
apt-get install -y python3.7
apt-get install -y python3.7-pip
apt-get install -y apache2
apt-get install -y nginx
cd /vagrant && pip3 install -r requirements.txt