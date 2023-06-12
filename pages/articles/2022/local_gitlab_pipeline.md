---
title: Running GitLab CI/CD Pipeline Locally with Docker-in-Docker using GitLab Runner Container
description: This article details how to use GitLab CI/CD pipelines locally which can be useful for testing and debugging purposes.
date: 2022-06-12
template: article.html
type: blog
author: jon
about: https://hub.docker.com/r/gitlab/gitlab-runner
tags:
  - Gitlab
  - Docker
  - CD/CI
  - Pipeline
  - VSCode
---

Running GitLab CI/CD pipelines locally can be useful for testing and debugging purposes. While GitLab provides robust CI/CD capabilities on its platform, there may be scenarios where executing the pipeline locally within your development environment, such as Visual Studio Code (VS Code), can be beneficial. In this blog post, we'll explore how to set up and run a GitLab CI/CD pipeline locally using the GitLab Runner container with Docker-in-Docker (DinD) support.


## Prerequisites

- Docker installed on your machine

- Basic knowledge of GitLab CI/CD and Docker concepts


## Step 1: Pull the GitLab Runner Image

To begin, ensure that you have Docker installed on your machine. Open a terminal within VS Code or any command prompt and pull the latest GitLab Runner Docker image by executing the following command:

```shell
docker pull gitlab/gitlab-runner:latest
```


## Step 2: Execute the Pipeline or Multiple Jobs with DinD

Next, navigate to your project's root directory containing the `.gitlab-ci.yml` file. To execute the entire GitLab CI/CD pipeline locally or specific jobs within it with Docker-in-Docker functionality, use the following command:

```shell
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
  -v /path/to/your/project:/builds/project \
  -w /builds/project gitlab/gitlab-runner:latest \
  gitlab-runner exec docker --docker-privileged [<job-name1>,<job-name2>,<job-name3>,...]
```

Replace `/path/to/your/project` with the local path to your project directory, and `<job-name1>,<job-name2>,<job-name3>,...` with the comma-separated list of job names you want to execute (optional).

By mounting the Docker socket (`/var/run/docker.sock`) as a volume inside the container and using the `--docker-privileged` flag, the GitLab Runner container gains access to Docker-in-Docker functionality. This allows the execution of Docker commands within the runner.

If you don't specify any job names, the GitLab Runner container will execute all the jobs defined in your `.gitlab-ci.yml` file sequentially, providing a local simulation of the GitLab CI/CD pipeline execution.

If you specify one or more job names, only those specific jobs will be executed within the GitLab Runner container, allowing you to selectively test and debug multiple parts of your pipeline.

Make sure your project directory contains the necessary files, configurations, and dependencies required for the pipeline or jobs to run successfully.

Remember to exercise caution when running Docker-in-Docker, as it can have security implications. Ensure that your environment is appropriately secured and follow best practices.


## Conclusion

Running GitLab CI/CD pipelines locally within your development environment can greatly enhance the development and testing process. By leveraging the GitLab Runner container with Docker-in-Docker support, you can simulate the GitLab CI/CD pipeline execution within tools like VS Code. This enables you to test and validate your pipeline configurations before pushing them to the GitLab platform.

That's it! You now have the knowledge to run an entire GitLab CI/CD pipeline or multiple jobs locally with Docker-in-Docker using the GitLab Runner container. Happy pipeline testing and debugging!

