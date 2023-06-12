---
title: Running GitLab Runner with VS Code Tasks
description: An explanation on how to setup VSCode Tasks to run Gitlab Pipelines directly from VSCode.
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

In a previous article, we learned how to run GitLab CI/CD pipelines locally using the GitLab Runner container. In this article, we'll explore how to streamline the process by creating VS Code tasks that allow us to launch the GitLab Runner with a simple keyboard shortcut. This will provide a convenient way to execute our pipelines or specific jobs directly from within the VS Code environment.


## Prerequisites

- VS Code installed on your machine

- [Completion of the previous steps](local_gitlab_pipeline.md)


## Step 1: Create a `.vscode` Directory

First, open your project in VS Code. In the root directory of your project, create a new directory called `.vscode` if it doesn't already exist.


## Step 2: Create a `tasks.json` File

Inside the `.vscode` directory, create a new file called `tasks.json`. This file will define the tasks we want to create.

Add the following content to the `tasks.json` file:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "Run GitLab CI/CD Pipeline",
      "type": "shell",
      "command": "docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v ${workspaceFolder}:/builds/project -w /builds/project gitlab/gitlab-runner:latest gitlab-runner exec docker --docker-privileged"
    },
    {
      "label": "Run Specific Job",
      "type": "shell",
      "command": "docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v ${workspaceFolder}:/builds/project -w /builds/project gitlab/gitlab-runner:latest gitlab-runner exec docker --docker-privileged",
      "args": [
        "--",
        "<job-name>"
      ],
      "problemMatcher": []
    }
  ]
}
```

The `tasks` array contains two tasks: "Run GitLab CI/CD Pipeline" and "Run Specific Job". The commands specified in the `command` field are the same as the ones we used previously to execute the GitLab Runner container.

For the "Run Specific Job" task, we have an additional `args` field where you should replace `<job-name>` with the name of the specific job you want to execute.


## Step 3: Define Keybindings (Optional)

To make it even more convenient, you can define keybindings for the tasks. Open the keybindings settings in VS Code by going to **File** -> **Preferences** -> **Keyboard Shortcuts** (or by pressing `Ctrl+K Ctrl+S`).

Add the following keybindings to the keybindings settings file:

```json
[
  {
    "key": "ctrl+shift+p",
    "command": "workbench.action.tasks.runTask",
    "args": "Run GitLab CI/CD Pipeline"
  },
  {
    "key": "ctrl+shift+j",
    "command": "workbench.action.tasks.runTask",
    "args": "Run Specific Job"
  }
]
```

These keybindings assign the "Run GitLab CI/CD Pipeline" task to `Ctrl+Shift+P` and the "Run Specific Job" task to `Ctrl+Shift+J`. Feel free to modify the keybindings according to your preference.


## Step 4: Run the Pipeline or Specific Job

You're now ready to run your GitLab CI/CD pipeline or specific job using the VS Code tasks. Press the assigned keybinding (`Ctrl+

Shift+P` for the pipeline or `Ctrl+Shift+J` for a specific job) to launch the GitLab Runner container and execute the desired task.


## Conclusion

By creating VS Code tasks, we've made it even easier to run GitLab CI/CD pipelines or specific jobs locally using the GitLab Runner. With a simple keyboard shortcut, we can now execute our pipelines or test individual jobs directly from within the VS Code environment.

That's it! You've learned how to set up VS Code tasks to launch the GitLab Runner. Enjoy the streamlined process of running your pipelines and jobs with ease.
