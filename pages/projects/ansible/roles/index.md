---
title: Ansible Roles
description: No Fuss Computings Ansible Roles Projects
date: 2023-11-10
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible
---

This section of the website contains Ansible roles and the details of how to use said projects. Across All of our Ansible roles we standardize as much as possible. This document will contain the details of said standardization.


Our roles:

- Common

- Docker Management

- [Firewall](firewall/index.md)

- Git Configuration

- [Home Assistant](homeassistant/index.md)

- [Kubernetes](kubernetes/index.md)

- SSH


## Role Requirements

This section covers what by default, be part of all ansible roles we create.


=== "ansible.builtin.set_stats"

    As part of the role, setting of ansible stats with `ansible.builtin.set_stats` must be provided. This enables a single variable that can be used after the play has completed. Usage of a role that includes the usage of `ansible.builtin.set_stats` within AWX enables population of the artifacts and passing of the stats between workflows/job templates.

    
    ```yaml
    - name: Stat Values
      ansible.builtin.set_fact:
        stat_values: |
          {
            "host_{{ inventory_hostname | replace('.', '_') | replace('-', '_') }}": {
              "roles": {
                role_name: {
                  "enabled": true,
                  "installed": false,
                  "empty_list": [],
                  "empty_dict": {}
                }
              },
              playbooks: {
                "{{ inventory_hostname }}": "here"
              }
            }
          }

    - name: Create Final Stats not Per Host
      ansible.builtin.set_stats:
        data: "{{ stat_values | from_yaml }}"
        per_host: false
        aggregate: true

    - name: Clear Stat Values
      ansible.builtin.set_fact:
        stat_values: null
    ```

    - `Stat Values` is only required if the variable names require expansion. _Can be omitted if no variable expansion required for variable name._

    - `Create Final Stats not Per Host` sets the artifacts/stats.

    - `Clear Stat Values` remove the stat fact. only required if using `Stat Values`.

    !!! tip AWX Gotcha
        AWX requires that `per_host` be set to `false` when setting stats for artifacts to work. Hence the structure of the artifacts above use hostname prefixed with `host_`. This method enables programatic checking if by host due to the presence of `host_` in the dictionary name.

=== "Variable naming"

- All Role Variables to be prefixed with the role name.
