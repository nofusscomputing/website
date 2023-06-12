---
title: Configuring a Permanent Whitelist in Fail2ban
description: An explanation on how to configure fail2ban to permanently allow hosts specified on a whitelist.
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

In this article, we will explore how to configure a permanent whitelist in Fail2ban. A whitelist allows specific IP addresses or DNS names to bypass any blocking rules enforced by Fail2ban. This can be useful when you want to ensure uninterrupted access for trusted hosts while still benefiting from the protection provided by Fail2ban against suspicious activity.


## Prerequisites

- An existing installation of Fail2ban on your system

- Basic knowledge of working with the command line


## Step 1: Open Fail2ban Configuration

1. Open the Fail2ban configuration file in a text editor using root privileges:

   ```bash
   sudo nano /etc/fail2ban/jail.local
   ```

2. Locate the `[DEFAULT]` section in the file.


## Step 2: Configure the Permanent Whitelist

1. Add the `ignoreip` parameter under the `[DEFAULT]` section to specify the IP addresses or DNS names to be whitelisted. You can whitelist multiple entries by separating them with a space.

   ```ini
   [DEFAULT]
   ignoreip = 192.168.1.100 example.com
   ```

   Replace `192.168.1.100` with the desired IP address or add more IP addresses as needed. You can also include DNS names like `example.com` to whitelist specific domains.

2. Save and exit the file (`Ctrl+O`, `Enter`, `Ctrl+X` in nano).


## Step 3: Restart Fail2ban Service

1. Restart the Fail2ban service to apply the configuration changes:

   ```bash
   sudo service fail2ban restart
   ```

Congratulations! You have successfully configured a permanent whitelist in Fail2ban. The IP addresses or DNS names specified in the `ignoreip` parameter will now be exempted from any blocking rules enforced by Fail2ban.

It's important to regularly review and update the whitelist to ensure it remains accurate and secure. Remember that introducing DNS names in the whitelist adds a dependency on DNS resolution, so ensure that DNS resolution is functioning properly on your system.

By configuring a permanent whitelist, you can allow trusted hosts to access your system without being affected by Fail2ban's blocking mechanisms. This helps strike a balance between security and accessibility.

Feel free to reach out if you have any questions or encounter any issues along the way. Stay secure!

!!! Note
    The provided instructions are based on the assumption that you have Fail2ban installed and have administrative privileges on your system. Modify the configuration as per your specific requirements and system configuration.
