---
title: Running GitLab Pipeline from GitHub Actions
description: An explanation on how to run a GitLab Pipeline or job from GitHub Actions.
date: 2022-06-12
template: article.html
type: blog
author: jon
about: https://www.fail2ban.org/
tags:
  - Gitlab
  - Github
  - Docker
  - CD/CI
  - Pipeline
---

Migrating from GitLab to GitHub or having existing GitLab configurations in your repository? No worries! In this article, we will explore how to seamlessly execute GitLab pipelines using GitHub Actions, enabling you to leverage the power of GitHub's CI/CD capabilities while maintaining your existing GitLab configurations.

If you already have a GitLab CI/CD pipeline defined in your repository, this guide will help you execute it without the need for major modifications. By configuring a self-hosted GitLab Runner Docker container in GitHub Actions and utilizing the .gitlab-ci.yml file, you can easily trigger your GitLab pipeline and benefit from GitHub's collaborative features.

Let's dive into the steps required to configure GitHub Actions, execute the GitLab Runner Docker container, and seamlessly run your GitLab pipeline from within your GitHub repository.


## Prerequisites

- Access to a GitHub repository with the desired project code.

- Basic knowledge of GitLab CI/CD and GitHub Actions concepts.


## Step 1: Configure GitHub Actions Workflow and Execute GitLab Runner Docker Container

1. Open your workflow configuration file (e.g., `.github/workflows/main.yml`) in your GitHub repository.

2. Specify the runner using the `runs-on` field:

   ```yaml
   jobs:
     build:
       runs-on: self-hosted
       steps:
         - name: Checkout code
           uses: actions/checkout@v2
   ```

   The `runs-on` field is set to `self-hosted`, instructing GitHub Actions to use a self-hosted runner.

3. Update the workflow file to include the following step for executing the GitLab Runner Docker container:

   ```yaml
   jobs:
     build:
       runs-on: self-hosted
       steps:
         - name: Checkout code
           uses: actions/checkout@v2

         - name: Start GitLab Runner Docker Container
           run: |
             docker run -d --name gitlab-runner \
               -v /var/run/docker.sock:/var/run/docker.sock \
               -v /path/to/runner/config:/etc/gitlab-runner \
               -v ${{ github.workspace }}:/${{ github.workspace }} \
               -w /${{ github.workspace }} \
               gitlab/gitlab-runner:latest
   ```

   Replace `/path/to/runner/config` with the actual path where you want to store the GitLab Runner configuration files.

4. Commit and push your workflow configuration file to your GitHub repository.


## Step 2: Use .gitlab-ci.yml for Jobs and Pipelines

1. Create or update the `.gitlab-ci.yml` file in your GitHub repository to define the jobs and pipelines for your GitLab Runner.

   ```yaml
   stages:
     - build
     - test
     - deploy

   build:
     stage: build
     script:
       - echo "Running build job"

   test:
     stage: test
     script:
       - echo "Running test job"

   deploy:
     stage: deploy
     script:
       - echo "Running deploy job"
   ```

   Customize the jobs and their respective scripts according to your specific CI/CD requirements.

2. Commit and push the `.gitlab-ci.yml` file to your GitHub repository.


## Step 3: Execute GitLab Pipeline using GitHub Actions

1. With the changes pushed to your GitHub repository, the self-hosted GitLab Runner Docker container will utilize the `.gitlab-ci.yml` file to execute the defined jobs and pipelines.

2. To run a specific job, add the job name as a parameter to the GitLab Runner command. For example, to run only the `test` job, modify the workflow configuration file as follows:

   ```yaml
   jobs:
     build:
       runs-on: self-hosted
       steps:
         - name: Checkout code
           uses: actions/checkout@v2

     test:
       runs-on: self-hosted
       steps:
         - name: Run GitLab Runner job
           run: |
             docker exec gitlab-runner gitlab-runner exec docker test
   ```

   In this example, the `test` job

 is executed using the `docker exec` command.

3. To run the entire pipeline defined in `.gitlab-ci.yml`, remove the specific job parameter from the `docker exec` command:

   ```yaml
   jobs:
     build:
       runs-on: self-hosted
       steps:
         - name: Checkout code
           uses: actions/checkout@v2

     test:
       runs-on: self-hosted
       steps:
         - name: Run GitLab Runner pipeline
           run: |
             docker exec gitlab-runner gitlab-runner exec docker
   ```

   By removing the job parameter, the entire pipeline will be executed.


## Conclusion

By configuring a self-hosted GitLab Runner Docker container in GitHub Actions and utilizing the `.gitlab-ci.yml` file, you can seamlessly execute GitLab pipelines from within your GitHub repositories. This enables you to leverage the powerful CI/CD capabilities of GitLab while still benefiting from the collaborative features of GitHub.
















I apologize for the confusion. If you want to focus solely on running GitLab pipelines from GitHub Actions and exclude any other methods, here's the revised article:

# Article 7: Running GitLab Pipeline from GitHub Actions

## Introduction
If you're looking to migrate from GitLab to GitHub or have existing GitLab configurations in your repository, this article is for you. We'll explore how to seamlessly execute GitLab pipelines using GitHub Actions, leveraging GitHub's CI/CD capabilities while maintaining your GitLab configurations.

By configuring GitHub Actions to trigger your GitLab pipeline, you can take advantage of GitHub's collaborative features while running your pipeline in a familiar environment.

## Prerequisites
Before we get started, make sure you have the following:

- A GitHub repository with your GitLab project code
- A `.gitlab-ci.yml` file defining your GitLab pipeline jobs

## Step 1: Configure GitHub Actions Workflow
1. In your GitHub repository, navigate to the **Actions** tab.

2. Click on **Set up a workflow yourself** to create a new workflow file.

3. Replace the contents of the workflow file with the following:

   ```yaml
   name: Run GitLab Pipeline

   on:
     push:
       branches:
         - main
     pull_request:
       branches:
         - main

   jobs:
     run-gitlab-pipeline:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout repository
           uses: actions/checkout@v2

         - name: Set up GitLab Runner
           uses: docker://gitlab/gitlab-runner:latest

         - name: Execute GitLab pipeline
           run: |
             # Customize this command to match your GitLab Runner configuration
             gitlab-runner exec docker <your-pipeline-name>
   ```

   Note: Replace `<your-pipeline-name>` with the name of your GitLab pipeline defined in `.gitlab-ci.yml`.

4. Commit and push the workflow file to your GitHub repository.

## Step 2: Customize GitLab Runner Configuration
1. In your GitHub repository, navigate to the **Settings** tab.

2. Click on **Secrets** in the left sidebar.

3. Add any necessary secrets or environment variables required for your GitLab Runner configuration.

   For example, you may need to set the `CI_JOB_TOKEN` secret to authenticate with your GitLab repository.

## Step 3: Trigger GitLab Pipeline
Any push or pull request events on the `main` branch will now trigger the GitHub Actions workflow, which in turn executes your GitLab pipeline.

## Conclusion
Congratulations! You've successfully configured GitHub Actions to run your GitLab pipeline. By leveraging GitHub's CI/CD capabilities, you can seamlessly execute your GitLab pipelines and benefit from the collaborative features provided by GitHub.

Remember to keep your `.gitlab-ci.yml` file up to date with your desired pipeline configurations. Feel free to explore other features of GitHub Actions to further enhance your CI/CD workflows.

If you have any questions or encounter any issues along the way, don't hesitate to reach out for assistance. Happy automating!

Please note that this article assumes you already have a working `.gitlab-ci.yml` file and focuses solely on executing the GitLab pipeline using GitHub Actions.

I hope this revised version of Article 7 meets your requirements.