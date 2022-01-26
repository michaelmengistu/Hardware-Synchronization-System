#!/bin/bash
sudo sysctl -w net.ipv4.conf.all.arp_filter=0
sudo sysctl -w net.ipv4.conf.all.rp_filter=0
sudo sysctl -w net.ipv4.conf.default.arp_filter=0
sudo sysctl -w net.ipv4.conf.default.rp_filter=0
sudo sysctl -w net.ipv4.conf.enp0s3.arp_filter=0
sudo sysctl -w net.ipv4.conf.enp0s3.rp_filter=0
sudo sysctl -w net.ipv4.conf.enx00e04c360fcb.arp_filter=0
sudo sysctl -w net.ipv4.conf.enx00e04c360fcb.rp_filter=0
sudo sysctl -w net.ipv4.conf.lo.arp_filter=0
sudo sysctl -w net.ipv4.conf.lo.rp_filter=0


