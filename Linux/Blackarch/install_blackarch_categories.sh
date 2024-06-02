#!/bin/bash

# List of BlackArch categories to install
categories=(
  blackarch-webapp
  blackarch-fuzzer
  blackarch-scanner
  blackarch-proxy
  blackarch-windows
  blackarch-dos
  blackarch-disassembler
  blackarch-cracker
  blackarch-voip
  blackarch-exploitation
  blackarch-recon
  blackarch-spoof
  blackarch-forensic
  blackarch-crypto
  blackarch-backdoor
  blackarch-networking
  blackarch-misc
  blackarch-defensive
  blackarch-wireless
  blackarch-automation
  blackarch-sniffer
  blackarch-binary
  blackarch-packer
  blackarch-reversing
  blackarch-mobile
  blackarch-malware
  blackarch-code-audit
  blackarch-social
  blackarch-honeypot
  blackarch-hardware
  blackarch-fingerprint
  blackarch-decompiler
  blackarch-config
  blackarch-debugger
  blackarch-firmware
  blackarch-bluetooth
  blackarch-database
  blackarch-automobile
  blackarch-webap
  blackarch-nfc
  blackarch-tunnel
  blackarch-drone
  blackarch-unpacker
  blackarch-radio
  blackarch-keylogger
  blackarch-stego
  blackarch-anti-forensic
  blackarch-ids
  blackarch-gpu
)

# Install each category with the specified pacman options
for category in "${categories[@]}"; do
  sudo pacman -S --needed --disable-download-timeout --noprogressbar --overwrite '*' $category --ignore aws-extender-cli
done
