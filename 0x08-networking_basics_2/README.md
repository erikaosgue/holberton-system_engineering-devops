
# 0x08. Networking basics #1

### Read or watch:

* [What is localhost]()
* [What is 0.0.0.0]()
* [What is the hosts file]()
* [Netcat examples]()

### man or help:

* ifconfig
* telnet
* nc
* cut

## Learning Objectives

### General
* What is localhost/127.0.0.1
* What is 0.0.0.0
* What is /etc/hosts
* How to display your machine’s active network interfaces

## Requirements

### General
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 14.04 LTS
* All your files should end with a new line
* A README.md file, at the root of the folder of the project, is mandatory
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.3-1~ubuntu14.04.1 via apt-get) without any errors
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing

### Tasks
[0. Localhost](https://github.com/erikaosgue/holberton-system_engineering-devops/blob/master/0x08-networking_basics_2/0-localhost)

What is localhost?

1. A hostname that means this IP
2. A hostname that means this computer
3. An IP attached to a computer

[1. All IPs](https://github.com/erikaosgue/holberton-system_engineering-devops/blob/master/0x08-networking_basics_2/1-wildcard)

What is 0.0.0.0?

1. All IPv4 addresses on the local machine
2. All the IPs
3. It means null in networking

[2. Change your home IP](https://github.com/erikaosgue/holberton-system_engineering-devops/blob/master/0x08-networking_basics_2/2-change_your_home_IP)

Write a Bash script that configures an Ubuntu server with the below requirements.

Requirements:

localhost resolves to 127.0.0.2
facebook.com resolves to 8.8.8.8.
The checker is running on Docker, so make sure to read [this](https://web.archive.org/web/20171117023601/http://blog.jonathanargentiero.com/docker-sed-cannot-rename-etcsedl8ysxl-device-or-resource-busy/)

[3. Show attached IPs](https://github.com/erikaosgue/holberton-system_engineering-devops/blob/master/0x08-networking_basics_2/3-show_attached_IPs)

Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.

[4. Port listening on localhost](https://github.com/erikaosgue/holberton-system_engineering-devops/blob/master/0x08-networking_basics_2/4-port_listening_on_localhost)

Write a Bash script that listens on port 98 on localhost

Terminal 0

Starting my script.

    eosorio@ubuntu$ sudo ./4-port_listening_on_localhost

Terminal 1

Connecting to localhost on port 98 using telnet and typing some text.

    eosorio@ubuntu$ telnet localhost 98
    Trying 127.0.0.2...
    Connected to localhost.
    Escape character is '^]'.
    Hello world
    test

Terminal 0

Receiving the text on the other side.

    eosorio@ubuntu$ sudo ./4-port_listening_on_localhost
    Hello world
    test
