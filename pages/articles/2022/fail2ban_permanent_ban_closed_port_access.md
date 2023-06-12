---
title: Managing Permanent Bans in Fail2ban
description: An explanation on how to configure fail2ban to permanently ban closed ports access as suspisious activity.
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

In this article, we'll continue from where we left off in the article "[Setting up Fail2ban to Monitor Common TCP and UDP Ports for suspicious activity](fail2ban_block_suspisious_activity.md)" and explore how to manage permanent bans in Fail2ban on Debian/Ubuntu. We'll specifically focus on checking the closed port log file, `/var/log/fail2ban_blocked_port_access.log`, and adding hosts to a permanent ban list if they are found three times. This additional step will further enhance the security of your system by permanently blocking repeat offenders.

When an attacker targets a system, they often perform port scanning to identify open ports that can be exploited. Accessing a closed port, on the other hand, is considered suspicious and indicative of potentially malicious activity. Fail2ban helps detect and respond to such behavior by monitoring the system's log files, including the closed port log. By examining this log, we can identify hosts that repeatedly attempt to access closed ports, indicating a persistent threat.

In this article, we'll cover the steps to check the closed port log, create a permanent ban list, and configure Fail2ban to add IP addresses to the ban list when they are found three times in the log. By doing so, we can effectively protect our system from attackers who repeatedly attempt to access closed ports.


## Prerequisites

- An existing installation of Fail2ban on Debian/Ubuntu

- Basic knowledge of working with the command line


## Step 1: Checking the Closed Port Log

1. Open the closed port log file, `/var/log/fail2ban_blocked_port_access.log`, using a text editor:

   ```bash
   sudo nano /var/log/fail2ban_blocked_port_access.log
   ```

2. Inside the log file, you will see entries in the following format:

   ```
   [2023-06-12] [http-blocked-port-80] [192.168.0.1] Host banned permanently.
   ```

3. Each entry consists of the date, rule name, IP address, and the indication of a permanent ban.


## Step 2: Creating the Permanent Ban List

1. Open the Fail2ban jail local configuration file in a text editor:

   ```bash
   sudo nano /etc/fail2ban/jail.local
   ```

2. Scroll to the end of the file and add the following section to create a permanent ban list:

   ```ini
   [permanent-bans]
   enabled = true
   filter = permanent-bans
   logpath = /var/log/fail2ban_blocked_port_access.log
   maxretry = 1
   bantime = -1
   action = iptables-allports
   ```

   Adjust the `filter` parameter and `logpath` as per your system configuration.

3. Save and exit the file (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).


## Step 3: Creating the Filter for Permanent Bans

1. Open the Fail2ban filter file for permanent bans in a text editor:

   ```bash
   sudo nano /etc/fail2ban/filter.d/permanent-bans.conf
   ```

2. Add the following content to the file:

   ```ini
   [Definition]
   failregex = ^\[\d{4}-\d{2}-\d{2}\] \[.*\] \[(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\].*Host banned permanently\.$
   ignoreregex =
   ```

3. Save and exit the file (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).


## Step 4: Restarting Fail2ban Service

1. Restart the Fail2ban service to apply the configuration changes:

   ```bash
   sudo service fail2ban restart
   ```

2. Fail2ban will now read the closed port log file and permanently ban any IP address that appears three times in the log.

Congratulations! You have successfully set up permanent bans in Fail2ban on Debian/Ubuntu. By monitoring the closed port log and adding repeat offenders to a permanent ban list, you have added an extra layer of security to your system.

!!! Tip
    Please note that while permanent bans provide increased protection, they should be used judiciously. Review the closed port log entries carefully before applying permanent bans to avoid unintended consequences. It's recommended to test and fine-tune the configuration in a controlled environment before applying it to production systems.

If you have any questions or encounter any issues, feel free to reach out. Stay secure!

## Common Network Ports

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

Feel free to reach out if you have any questions or encounter any issues along the way. Stay secure!

!!! Note
   Please note that the provided configurations and port table are examples, and you may need to modify them based on your specific needs and environment.