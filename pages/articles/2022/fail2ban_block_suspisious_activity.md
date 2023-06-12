---
title: Setting up Fail2ban to Monitor Common TCP and UDP Ports for suspicious activity
description: An explanation on how to configure fail2ban to block suspisious activity.
date: 2022-06-12
template: article.html
type: blog
author: jon
about: https://www.fail2ban.org/
tags:
  - Security
  - Firewall
  - Fail2ban

---

In this article, we'll explore how to set up an existing installation of Fail2ban to monitor common TCP and UDP ports. Fail2ban is a powerful tool that scans log files, detects suspicious activity, and automatically blocks the IP addresses of the offending hosts. By implementing Fail2ban to monitor common ports, we can enhance the security of our system and mitigate potential risks.


## Prerequisites

- An existing installation of Fail2ban

- Basic knowledge of working with the command line


## Step 1: Set up iptables Rules

1. Open the iptables configuration file in a text editor using root privileges:

   ```bash
   sudo nano /etc/iptables/log_closed_ports.v4
   ```

2. Add the following rules for each specified port to log access to that port:

   ```bash
   -A INPUT -p tcp --dport 80 -j LOG --log-prefix "[http-blocked-port-80] "
   -A INPUT -p tcp --dport 443 -j LOG --log-prefix "[https-blocked-port-443] "
   -A INPUT -p udp --dport 53 -j LOG --log-prefix "[dns-blocked-port-53] "
   -A INPUT -p tcp --dport 22 -j LOG --log-prefix "[ssh-blocked-port-22] "
   -A INPUT -p tcp --dport 3306 -j LOG --log-prefix "[mysql-blocked-port-3306] "
   -A INPUT -p tcp --dport 5432 -j LOG --log-prefix "[postgresql-blocked-port-5432] "
   ```

   Adjust the port numbers and log prefixes as needed for each port.

3. Save and exit the file (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).

4. Restart the iptables service to apply the changes:

   ```bash
   sudo service iptables restart
   ```


## Step 2: Configure Fail2ban Filters

1. Open the Fail2ban filters directory in a text editor:

   ```bash
   sudo nano /etc/fail2ban/filter.d/iptables-port.conf
   ```

2. Add the following content to the file:

   ```ini
   [Definition]
   failregex = ^.*\[.*\] .* <HOST> .*$
   ignoreregex =

   actionban = iptables-multiport[logpath="/var/log/fail2ban_blocked_port_access.log", logprefix="[%(date)s] [%(name)s] [%(ip)s] "]
   ```

3. Save and exit the file (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).


## Step 3: Configure Fail2ban Jail

1. Open the Fail2ban jail configuration file in a text editor:

   ```bash
   sudo nano /etc/fail2ban/jail.d/custom.conf
   ```

2. Add the following configuration to the file:

   ```ini
   [http-blocked-port-80]
   enabled = true
   filter = iptables-port
   logpath = /var/log/iptables.log
   maxretry = 3
   banaction = iptables-multiport

   [https-blocked-port-443]
   enabled = true
   filter = iptables-port
   logpath = /var/log/iptables.log
   maxretry = 3
   banaction = iptables-multiport

   [dns-blocked-port-53]
   enabled = true
   filter = iptables-port
   logpath = /var/log/iptables.log
   maxretry = 3
   banaction = iptables-multiport

   [ssh-blocked-port-22]
   enabled = true
   filter = iptables-port
   logpath = /var/log/iptables.log
   maxretry = 3
   banaction = iptables-multiport

   [mysql-blocked-port-3306]
   enabled = true
   filter = iptables-port
   logpath = /var/log/iptables.log
   maxretry = 3
   banaction = iptables-multiport

   [postgresql-blocked-port-5432]
   enabled = true
   filter = iptables-port
   logpath = /var/log/iptables.log
   maxretry = 3
   banaction = iptables-multiport
   ```

   Adjust the configuration as needed for each port.

3. Save and exit the file (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).


## Step 4: Restart Fail2ban Service

1. Restart the Fail2ban service to apply the configuration changes:

   ```bash
   sudo service fail2ban restart
   ```

Congratulations! You have successfully set up Fail2ban to monitor common TCP and UDP ports. Fail2ban will now log access attempts to the specified ports and automatically ban IP addresses that exceed the maximum number of allowed retries. The ban events will be logged in the `/var/log/fail2ban_blocked_port_access.log` file with the date, rule name, and IP address information.

!!! Alert
    Please note that the provided configurations are examples, and you may need to modify them based on your specific needs and environment.


## Common Ports

Within this table you will find some common ports that maybe useful to include additional rules for.

| Port | Protocol | Description                  |
|------|----------|------------------------------|
| 20   | TCP      | FTP Data                     |
| 21   | TCP      | FTP Control                  |
| 22   | TCP      | SSH                          |
| 23   | TCP      | Telnet                       |
| 25   | TCP      | SMTP                         |
| 53   | TCP/UDP  | DNS                          |
| 67   | UDP      | DHCP Server                  |
| 68   | UDP      | DHCP Client                  |
| 69   | UDP      | TFTP                         |
| 80   | TCP      | HTTP                         |
| 110  | TCP      | POP3                         |
| 115  | TCP      | SFTP                         |
| 123  | UDP      | NTP                          |
| 137  | UDP      | NetBIOS Name Service         |
| 138  | UDP      | NetBIOS Datagram Service     |
| 139  | TCP      | NetBIOS Session Service      |
| 143  | TCP      | IMAP                         |
| 161  | UDP      | SNMP                         |
| 389  | TCP/UDP  | LDAP                         |
| 443  | TCP      | HTTPS                        |
| 445  | TCP/UDP  | SMB                          |
| 465  | TCP      | SMTPS                        |
| 514  | TCP/UDP  | Syslog                       |
| 587  | TCP      | SMTP (Submission)            |
| 636  | TCP/UDP  | LDAPS                        |
| 993  | TCP      | IMAPS                        |
| 995  | TCP      | POP3S                        |
| 1433 | TCP      | MS SQL Server                |
| 1434 | UDP      | MS SQL Server (UDP)          |
| 1521 | TCP      | Oracle Database              |
| 2049 | TCP/UDP  | NFS                          |
| 3306 | TCP      | MySQL                        |
| 3389 | TCP      | Remote Desktop Protocol (RDP) |
| 5432 | TCP      | PostgreSQL                   |
| 5900 | TCP      | VNC                          |
| 5985 | TCP      | WinRM                        |
| 6379 | TCP      | Redis                        |
| 8080 | TCP      | HTTP (Alternate)             |
```
