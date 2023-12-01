---
title: Ansible Projects
description: No Fuss Computings Ansible Projects
date: 2023-06-01
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible
---

This section of the website contains Ansible projects and the details of how to use said projects. Across All of our Ansible projects we standardize as much as possible.

Any playbooks and roles we create are designed with the below ansible setup in mind. Whilst there are many ways ~~to skin a cat~~ setup ansible, If you deviate from below you will be required to test to ensure that if using our playbooks/roles, that they work as intended. If you find that there is a better way of setting up Ansible, raise an issue with your proposal and we'll discuss.

- [No Fuss Computing playbooks](playbooks/index.md)

- [No Fuss Computing roles](roles/index.md)


## Inventory Setup

The Inventory should be setup under an SCM, git in this case; So that a version history is maintained. This also fosters a full audit trail as part of the complete host lifecycle. Idealy the Inventory along with directories `files` and `templates.` should be contained in it's own git repository. Using this method provides that the git history only pertain to the inventory alone, and therefore any install/configuration of a host.

!!! tip
    If you must include `playbooks` and `roles` wihin your inventory repository it's a good idea that these still be their own repositories with them added to the inventory repository as a git sub-module.

Ansible inventory directory structure.

``` bash
.
├── ansible.cfg
├── files
│   ├── all
│   │   ├── 
│   │   ├── 
│   ├── node1
│   │   ├── 
│   │   ├── 
│   ├── k3s-prod
│   │   ├── Ingress-manifest-AWX.yaml
│   │   └── deployment-manifest-test_web_server.yaml
│   ├── k3s-testing
│       └── deployment-manifest-test_web_server.yaml
|
├── .inventory_root
│
├── inventory
│   ├── development
│   │   ├── group_vars
│   │   │   ├── all.yaml
│   │   │   ├── debian.yaml
│   │   ├── hosts.yaml
│   │   └── host_vars
│   │       ├── laptop2.yaml
│   │       ├── node1.yaml
│   │       ├── node2.yaml
│   │       ├── node3.yaml
│   │       ├── node4.yaml
│   │       └── node5.yaml
│   └── production
│       ├── group_vars
│       │   ├── all
│       │   │   ├── main.yaml
│       │   │   ├── vault.yaml
│       │   │   └── versions_software.yaml
│       │   ├── awx.yaml
│       ├── hosts.yaml
│       └── host_vars
│           ├── node1.yaml
│           ├── k3s-prod
│           │   ├── backup.yaml
│           │   ├── kubernetes.yaml
│           │   ├── main.yaml
│           │   └── vault.yaml
│           ├── k3s-testing
│               ├── main.yaml
│               └── vault.yaml
├── playbooks
│   ├── all.yaml
├── README.md
└── templates
    ├── hosts
    │   └── k3s-prod
    │       └── HelmChart-manifest-NginX-ingress.yaml
    │
    └── groups
```

| name | Type | Description |
|:---|:---:|:---|
| ansible.cfg | _file_ | Ansible configuration file applicable to this inventory |
| files | _directory_ | Contain files that a host may require. Playbook task iterates over by hostname and group name. Sub-directories for hostname / group-name |
| .inventory_root | _file_  | This file is used by `nfc_common` role to determin the root directory of the inventory. |
| inventory | _directory_ | Ansible inventory. If multiple inventories exist can use sub folders. |
| playbooks | _directory_ | Should be a git submodule. _This keeps inventory and playbooks SCM related to each only._ |
| README.md | _file_  | Inventory readme with applicable info. |
| templates | _directory_ | This directory is the same as the `files` directory except contains jinja templates. |


### Inventory

Naming of host inventory files is to use the hostname portion of the FQDN only. i.e. for a host with a FQDN of `myhostname.domain.tld` it's `inventory_hostname` would be `myhostname`. This requirement is a must as many parts of our roles and playbooks depend upon this value matching the DNS system.


#### hosts file

The hosts file `host.yaml` contains all hosts and by which group they are part of.


### Playbooks


### Templates

Templates directory contains only two sub-deirectories `groups` and `hosts` under each of these folders are folders by group/host name that contain template files. Preferernece is leaning toards not using the `.j2` extension as the IDE may loose functionality by using.

Naming of template files is in format `{item-type}-{what-uses}-{friendly name that uses underscores not hyphon}.{file_extension}`

| Item Type | what uses | Notes
|:---|:---:|:---|
| config | bind | Configuration file for bind dns server |
| dnszone | bind | a bind server DNS zone |
| `{kubernetes kind}` | manifest | A kubernetes manifest |


#### Feature gates

Templates when added to the group folder should be setup with a feature gate. This eanbles simple yaml to be defined to allow the template to deploy.

example of yaml declaration that host/group would read.
``` yaml
feature_gates:
  is_prime: false
  monitoring: true
  operator_awx: true
  operator_grafana: true
  operator_prometheus: true
  postgres_cluster: true
  rook_ceph: true
```

Seting a feature gate on a template is as simple as enclosing the entire contents of the file with a jinja if statement. i.e. `{% if path.feature_gates.monitoring | default(false) | bool %}the content here{% endif %}`


## AWX / Tower / Automation Platform


### Prime host

If you use a system like AWX / Tower / Automation Platform the inventory should be designed in a way that you have a prime host. The prime host is a single host that once it exists, it's capable of rebuilding all of the infrastructure within the inventory. Using the prime host method, you only require the variable secrets (vault encrypted) of the prime host and only those pertinent to rebuilding the prime host. This should only be the backup decryption key (vault encrypted).

!!! warning Warning
    Prime Host requires that the backup decryption key be updated within the inventory whenever it changes. There is also a requirement that the vault encryption key be available and not stored on infrastructure that without or that infrastructure not existing you cant access the vault key. i.e. password manager.


## ToDo

- Explain usage of file `.inventory_root` which must exist as nfc_common _(todo: see kubernetes playbook/master)_ _may no longer be required a project structure is known along with using variable `playbook_dir`_