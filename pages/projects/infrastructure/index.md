---
title: Infrastructure
description: No Fuss Computings Infrastructure project using open source software
date: 2024-01-13
template: project.html
about: https://gitlab.com/nofusscomputing/projects/ansible
---

This infrastructure project exists as an example of computing infrastructure that is based on open source software. The idea is to demonstrate ways of using open source software for your computing infrastructure whether it be for the home or enterprise user. Whilst a lot of my hardware is not enterprise grade equipment, The devices I use will serve as a proof of concept. Particular focus of this project is going to be spent on automation. Why? Simply put, it reduces the requirement for additional people to achieve the same economy of effort. _Oh, and cause I can!!_


## Goal

Design, build and deploy computing infrastructure using open source software that could be used by both the enterprise and home user and wherever possible, simplify to lower the bar of entry.


## Requirements

- Automated

- multi-site

- multi-tenant


## Areas

The areas of infrastructure that are covered are as detailed:

- Certificate Authority

- HyperVisor - _KubeVirt via K3s Kubernetes_

- Identity Management - _IPA_

- Identity Provider (SSO) - _Keycloak_

- IT Operations (ITOPs)

    - Backup Management

    - Computer Lifecycle Management - _GLPI_

    - Help desk - _GLPI_

    - IP Address Management (IPAM) - _phpIPAM_

    - Knowledge Management

        - Playbooks

        - Runbooks

    - Logging Management

    - Metrics Management

    - Remote Desktop Support - _Mesh Central_

    - Software Library - _Pulp?????_

- IT Service Management (ITSM)

    - Change Management - _GLPI_

    - Config Management - _AWX_

    - Enterprise Service Management (ESM)

    - Incident Management - _GLPI_

    - IT Asset Management - _GLPI_

    - Patch Management - _Foreman_

    - Problem Management - _GLPI_

    - Request Management - _GLPI_

        - Service Catalog - _GLPI_

    - Secrets Management - _Hashicorp Vault_

    - Security Management

- Networking

    - DNS - _Bind??_

    - DHCP

    - Radius

    - TFTP

- Password Storage

- Storage - _Ceph_

- Virtual Desktop Infrastructure (VDI) - _Mesh Central ???_

- Website - _Markdown built with MKDocs_


## Workflow

Within the IT world there are multiple working components to support the business goal. With this in mind, workflows are required for the start and endpoints of the lifecycle of those components. This can be broken down into two items that become the workflows for the infrastructure, they are:

- Devices

- People

For the remainder of the infrastructure and services workflows, fall under one of the areas mentioned above. There is an argument to be made that devices do too; however have defined here due to a potential for a rare occasion that the ITOPS workflows were not followed, that the devices would still be captured.

### Devices

Of particular importance is the infrastructure's devices. whether they be Computers, Servers, Laptops etc. There must be workflows that are followed that cater for: discovery, existence and absence; without this it's likely that you will miss a device.


### People

Without a workflow for people, why are you even building the infrastructure?? As people access the system there must be workflows like devices that cater for: New, discovery, existence, absence and leaving. Defining these workflows will aid in management as well as define the requirements which can be used as the start point for automating the workflows.
