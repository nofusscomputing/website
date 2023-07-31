---
title: Site Refurbishment
description: it's an update.
date: 2023-08-01
template: article.html
type: blog
author: jon
copyrightHolder: jon
about: https://nofusscomputing.com
tags:
  - Automation
  - Website
  - Update
---

It's been a while and for all intents and purposes; Prior to today you would not have been mistaken for thinking that our site was dead in the water. I could give reasons, but the reality is it's an excuse and we all know that *"they're like arseholes, everyones got one!!"* As it currently stands, I find myself with a little extra time on my hands so this site revamp is the start and first visibility of what I've been doing.

I've spent a good part of a few of a few decades working with computers. Whilst this has been an interesting journey, in the last few years I've discovered Configuration-as-Code. The concept itself wasn't exactly new to me, I just put off learning anything about it past the name. As creatures of habits, us humans, once we have found our way we tend to stick to that routine or better stated, with what we know.
Moving from the early days (norton ghost and clonezilla) with manually built images for every different type of machine. which became very monotonous to manually update the images with patches. The opportunity had presented itself resently where for the first time in over two decades, I'm required to rebuild my infrastructre from scratch. As daunting as this sounds, given the leaps and bounds that have occured in the last decade, even more in the last five years. Technologies have evolved to the point where now it takes a fraction of the time to do what used to take upwards of a week. Upgrades now are not rebuild the image from scratch, clone and redeploy. Now, I punch the keyboard and characters show on the screen, then I run a program, Ansible. It reads the jibberish (json/yaml) and presto, Bobs your uncle, a deploy has occured. Fresh deployment or updates, doesn't matter, run the same code again and Ansible ensures it's setup how it's supposed to be. Need to update a piece of software, too easy, change the version number in your config files.

Other things of note worthy mention:

- For Family and friends, free of course I host Password vault, <https://vault.nofusscomputing.com>. This enables you to install an app on your phone and within your web browser which lets you sync your passwords, identities and secrets-and using zero-trust full encryption. Best feature of all,you only have to remember your vault password, as everything else is stored in the vault.

- Helpdesk now deployed publicly, <https://helpdesk.nofusscomputing.com>. Along with automating everything else a Service Catalog is being extended to automate other tasks.

- Website updating now occurs automagically. We do this via Gitlab using CD/CI pipelines. Now I just edit a file, push the changes and the changes deploy my site on the interwebs.

- Our [projects](../../projects/index.md) from [GitHub](https://github.com/NoFussComputing) and [GitLab](https://gitlab.com/nofusscomputing) deploy their docs to our site, again automagically.
