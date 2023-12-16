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


## Playbooks

Playbooks are used for grouping of hosts and/or groups for a task or set of tasks that are required to be run. All playbooks must return artifacts that exist to serve the purpose of having information on the play that can be used in further automations.


### Artifacts

The artificates returned are set using the `ansible.builtin.set_stats` module. Prior to setting these facts with the `stats` module they must be set as facts first using the `ansible.builtin.set_fact` module. the latter enables passing of the artifacts via cli and `stats` from within AWX / Ansible Automation Platform.

!!! tip
    When setting the artifacts, ensure `per_host=false` is set so that artifacts work within AWX / Ansible Automation Platform.

Common artifacts structure. **ALL** playbooks must set these variables.

``` yaml
# 'nfc_automation', dict. Global Variable, This is set from within the first playbook 
# ran and updated as required with the end time updated by the last playbook.
nfc_automation:
  error: 0      # Boolean, 0=no Error, 1=Error occured
  time:
    start: "{{ '%Y-%m-%dT%H:%M:%S %z' | strftime }}"    # String of date time, set at time of setting 'nfc_automation'
    end: 0                                              # String of date time, set when play finished, and updated by subsequent plays
                                                        # Determin end time of play or duration of play when used with start time, even on error.

# 'nfc_task', list. every playbook creates its own task dict to add to this list.
nfc_task: 
  - name: "glpi"
    start: "{{ '%Y-%m-%dT%H:%M:%S %z' | strftime }}"
    tags: "{{ ansible_run_tags }}"

```

The above must be set from within every playbook regardless of what else is in the playbooks.

example playbook to set artifacts and variables

``` yaml
---

#
# Playbook Template
#
# This playbook template is the base template for All of our playbooks.
#
# No Fuss Computing <https://nofusscomputing.gitlab.io/projects/ansible/ansible_playbooks/projects/ansible/>
#
# Requirements:
#   - ansible >= 2.8
#

- name: Playbook Template
  hosts: localhost
  become: false


  pre_tasks:


      # Play and task set time
    - name: Set Start Time
      ansible.builtin.set_fact:
        nfc_task_starttime: "{{ ('%Y-%m-%dT%H:%M:%S %z' | strftime) | string }}"
      no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
      when: nfc_automation is not defined
      tags:
        - always


    # Setup dictionary 'nfc_automation'
    - name: Set Automation Facts
      ansible.builtin.set_fact:
        nfc_automation: {
          "error": 0,
          "time": {
            "start": "{{ nfc_task_starttime | string }}",
            "end": 0
          }
        }
      no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
      when: nfc_automation is not defined
      tags:
        - always


    # Setup dictionary 'nfc_task'
    - name: Set Automation Facts
      ansible.builtin.set_fact:
        nfc_task: {
          "name": "{{ ansible_play_name | lower | string }}",
          "roles": "{{ ansible_play_role_names | string }}",
          "skip_tags": "{{ ansible_skip_tags | list }}",
          "start": "{{ nfc_task_starttime | string }}",
          "tags": "{{ ansible_run_tags | list }}"
        }
      no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
      tags:
        - always


    - name: Block - pre_tasks
      block:


        ########################################################################
        #
        # Your tasks here
        #
        ########################################################################


      rescue:

          # there was an error, set error object
        - name: Set error fact
          ansible.builtin.set_fact:
            nfc_automation: "{{ nfc_automation | combine({
                'error': 1
              }) }}"
          no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
          tags:
            - always


      always:


          # Check if error occured and fail task
        - name: Error Check
          ansible.builtin.assert:
            that:
              - nfc_automation.error | int == 0
            msg: Error occured, Fail the play run
          tags:
            - always


    # Don't use the 'roles' section.
  roles: []
    # if the included role(s) do not contain a rescue block, the playbook may stop
    # executing in this section (roles) with the post_tasks not running. This will
    # cause the artifacts to be incomplete. It's recommended to include your roles
    # in section(s) 'pre_tasks', 'tasks' or 'post_tasks' and from within a block with
   # rescue so that the playbook can complete and ensure that all artifacts are set.


  tasks:


    - name: Block - tasks
      block:

          # Check for error and fail play on error
        - name: Error Check
          ansible.builtin.assert:
            that:
              - nfc_automation.error | int == 0
            msg: Error eccured, follow error path to fail play


        ########################################################################
        #
        # Your tasks here
        #
        ########################################################################

      rescue:


          # there was an error, set error object
        - name: Set error fact
          ansible.builtin.set_fact:
            nfc_automation: "{{ nfc_automation | combine({
                'error': 1
              }) }}"
          no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
          tags:
            - always


      always:


          # Check if error occured and fail task
        - name: Error Check
          ansible.builtin.assert:
            that:
              - nfc_automation.error | int == 0
            msg: Error occured, Fail the play run
          tags:
            - always


  post_tasks:

    - name: Tasks post_task
      block:


          # Check for error and fail play on error
        - name: Error Check
          ansible.builtin.assert:
            that:
              - nfc_automation.error | int == 0
            msg: Error occured, follow error path to fail play
          tags:
            - always


        ########################################################################
        #
        # Your tasks here
        #
        ########################################################################


      rescue:


          # there was an error, set error object
        - name: Set error fact
          ansible.builtin.set_fact:
            nfc_automation: "{{ nfc_automation | combine({
                'error': 1
              }) }}"
          no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
          tags:
            - always


      always:


          # Task and automation end time.
        - name: Fetch End time
          ansible.builtin.set_fact:
            nfc_task_endtime: "{{ '%Y-%m-%dT%H:%M:%S %z' | strftime }}"
          no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
          tags:
            - always


          # Set task end time
        - name: Set task Facts
          ansible.builtin.set_fact:
            nfc_tasks: "{{ nfc_tasks | default([]) + [ nfc_task | combine({
                'end': nfc_task_endtime | string
              }) ] }}"
          no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
          tags:
            - always


          # Set Automation end time.
          # every playbook must set this variable so that the end time
          # is equal to the fail time or the end of a group of playbooks.
        - name: Set automation end time
          ansible.builtin.set_fact:
            nfc_automation: "{{ nfc_automation | combine({
                'time': nfc_automation.time | combine({
                  'end': nfc_task_endtime | string
                })
              }) }}"
            nfc_task_endtime: null
          no_log: "{{ nfc_pb_no_log_setup_facts | default(true) | bool }}"
          tags:
            - always


          # Set the artifacts as a fact for subsequent playbook useage
          # Note: variable 'per_host' must be 'false' so that the artifacts
          # work within AWX / Ansible Automation Platform.
        - name: Create Automation Artifact
          ansible.builtin.set_stats:
            data:
              nfc_automation: "{{ nfc_automation }}"
              nfc_tasks: "{{ nfc_tasks }}"
            per_host: false
          tags:
            - always


          # Final error check to fail the entire play run on error
        - name: Error Check
          ansible.builtin.assert:
            that:
              - nfc_automation.error | int == 0
            msg: Error occured, Fail the play run
          tags:
            - always


  vars: {}


```

The above template playbook is designed for post automation should it be required to run. `nfc_automation` is for the entire play/workflow with `nfc_tasks` being a list of `nfc_task` dictionary from each playbook. `nfc_task`  is there for you to add your own artifacts to and without any additional effort from you, will be added to the global artifacts. 


### Playbook Variables

Within any playbook that we create any variable that is set within the playbook is to be prefixed with `nfc_pb_`. Currently we have the following variables that are reserved and set as part of how we structure our playbooks.

- `nfc_automation` Details on the play/run. see artifacts above for details.

- `nfc_pb_no_log_setup_facts` Boolean value used as a feature gate on whether to log `set_fact` tasks that are for setting up the play. i.e. artifacts. setting this value to `false` will caused the tasks to be logged.

- `nfc_tasks` List of all `nfc_task` dictionaries of the play. see artifacts above for details.


## AWX / Tower / Automation Platform


### Prime host

If you use a system like AWX / Tower / Automation Platform the inventory should be designed in a way that you have a prime host. The prime host is a single host that once it exists, it's capable of rebuilding all of the infrastructure within the inventory. Using the prime host method, you only require the variable secrets (vault encrypted) of the prime host and only those pertinent to rebuilding the prime host. This should only be the backup decryption key (vault encrypted).

!!! warning Warning
    Prime Host requires that the backup decryption key be updated within the inventory whenever it changes. There is also a requirement that the vault encryption key be available and not stored on infrastructure that without or that infrastructure not existing you cant access the vault key. i.e. password manager.


## ToDo

- Explain usage of file `.inventory_root` which must exist as nfc_common _(todo: see kubernetes playbook/master)_ _may no longer be required a project structure is known along with using variable `playbook_dir`_