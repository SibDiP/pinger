

# Ping IP Port
[![Python 3.12](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/downloads/release/python-312/)
[![Socket](https://img.shields.io/badge/Socket-TCP/IP-green.svg)](https://docs.python.org/3/library/socket.html)

A simple Python script to ping a list of IP addresses and ports using TCP/IP.

## Description

This script reads a list of IP addresses and ports from a file named `servers_ip.txt`, attempts to establish a TCP connection to each one, and prints the result.

## Usage

1. Create a file named `servers_ip.txt` with the following format:
```
192.168.1.1:8080
192.168.1.2:8080
192.168.1.3:8080
```
2. Run the script using Python 3.12 or later.

## Requirements

* Python 3.12 or later

## License

This code is released under the MIT License. See [LICENSE](LICENSE) for details.