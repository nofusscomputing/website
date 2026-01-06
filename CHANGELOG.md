## 1.0.0 (2026-01-06)

### feat

- **docs**: Add centurion role - git
- **child-docs**: enable homeassistant on local git
- **child-docs**: enable nodered_ldap_self_service on local git
- **child-docs**: disable nodered_ldap_self_service
- **child-docs**: enable nodered_ldap_self_service role on dev branch
- **child-docs**: enable kubernetes_monitoring role on dev branch
- **child-docs**: enable itil_runbooks role on dev branch
- **child-docs**: enable git_configuration role on dev branch
- **child-docs**: enable gitlab-ci role on dev branch
- **child-docs**: enable docker-mail role on dev branch
- **child-docs**: enable docker-bind role on dev branch
- **child-docs**: enable common role on dev branch
- **child-docs**: enable ansible_playbooks on dev branch
- **child-docs**: disable nodered_ldap_self_service
- **child-docs**: disable kubernetes_monitoring
- **child-docs**: disable itil_runbooks
- **child-docs**: disable homeassistant
- **child-docs**: disable git_configuration
- **child-docs**: disable gitlab-ci
- **child-docs**: disable docker mail
- **child-docs**: disable docker bind
- **child-docs**: disable ansible roles common
- **child-docs**: disable ansible-playbooks
- migrate child docs from gitlab ci
- **sub-docs**: Add firewall
- **centurion**: add ansible collection centurion
- **centurion_erp**: rename doc path
- django itsm
- **project**: add django itsm docs
- publish netbox collection docs
- **project**: add docker bind
- **firewall**: fix nav
- **firewall**: add project to nav
- **firewall**: update project path
- restructure kube role to collection
- **kubernetes_collection**: restructured from role to collection
- Matrix assemble
- Add Ansible Collection phpIPAM Scan Agent for documentation build
- **project**: add phpIPAM ansible collection project to docs
- Add project itil runbooks to website deploy
- **project**: add itil runbooks
- Mkdocs update
- document the playbook dynamic hosts selection
- **ansible**: update playbook requirements with awx vars
- **ansible**: playbook setup and setting of variables
- site navigation restructure and k3s deployment
- **ansible**: document inventory_hostname requirement
- **hosting**: migrate to new hosting service
- **ansible**: added further docs of inventory, specifically templates
- add project ansible role common
- add project dns
- **ansible_roles**: added start of role standardization docs.
- **ansible**: add inventory setup
- **ansible**: started documenting ansible
- add projects firewall, kubernetes and homeassistant
- **project**: added project Public Playbooks
- **docs**: add kubernetes monitoring helm chart project
- **docs**: add kubernetes monitoring helm chart project
- **docker_glpi**: add project docs for publishing
- **docker_glpi**: add project docs for publishing
- **docker_glpi**: add project docs for publishing
- **docs**: add project ldap self service
- **docs**: added project ldap self service
- New logo
- **logo**: add new logo
- **article**: site updated and deployed
- **ci**: add resource groups to build jobs
- **ci**: add resource groups to build jobs
- **artifcts**: always make available
- **artifcts**: always make available
- **artifcts**: always make available
- **artifcts**: always make available

### Fixes

- build docs on api trigger
- **firewall**: remove link from ansible roles
- **ci**: ensure for non dev/master build is avail for pages
- **ci**: dont attempt to move sub-project docs if not exist
- **ci**: pages dep is also build
- **ci**: pages only requires merge job on merge
- merge docs
- merge docs
- mkdir
- mkdir
- use correct path
- prepare built site and dir structure
- no trailing slant for paths
- use correct path
- run the echo'ed commands
- run the echo'ed commands
- ensure fetch project job creates directory
- ensure fetch project job creates directory
- **phpipam_scan_agent**: use correct path when assembling site again.
- **phpipam_scan_agent**: use correct path when assembling site again.
- **phpipam_scan_agent**: use correct path when assembling site
- **phpipam_scan_agent**: use correct path when assembling site
- nav ansible EE
- **ansible-ee**: update nav to match repo
- ensure ansible_test placeholder exists
- git config project
- **git_configuration**: update path for docs
- **publish**: correct artifacts path
- **publish**: ensure job is tagged to select correct runner
- **unit_test**: added an ignore for alive check for pages that are alive, but return 404
- edit url
- **unit_test**: 401|403 are valid returns for a link
- navigation, common
- **docker_glpi**: add docks to site structure
- **docker_glpi**: add docks to site structure
- **docker_glpi**: correct docs path
- **docs**: use correct ldap project path
- **ci**: ensure jobs don't run on schedule

### Refactoring

- update template path
- **child-docs**: homeassistant to use internal
- dont use stage name dirs
- **project_docs**: use matrix job to assemble site
- docker nav structure

### Tests

- correct ignore link
- **unit**: ignore alive check for nofusscomputing.com

## 1.0.0rc3 (2023-05-31)

### Fixes

- **ci**: website.lint paths updated

## 1.0.0rc2 (2023-05-29)

### feat

- **ci**: assemble job now does check for sub-site dependencies
- **ci**: use automagic gitlab-ci template
- docker-mail docs to be included
- **ci**: enable publishing docker-mail docs
- **website**: enable edit button
- work on article templates and config
- **ci**: add resource groups to prevent dup jobs
- **publish**: on publish website on success
- **build**: include project gitlab-ci docs
- **requirements.txt**: removed as part of template
- **md_lint_config**: moved to website-template repo
- **publish**: clean remote dir first anduse correct source
- **operations**: Pull Operations website pages job artifacts.
- **website_template**: Added website template as submodule
- **mkdocs**: enabled tabbed content
- **wiki**: remove wiki as it wont be used.
- **article**: added microdata to the article.
- **article**: articles must have a type
- **markdown_lint**: allow html p in markdown
- **vscode**: extension recommendations added.
- **home_page**: setup homepage as a template
- **article**: migrate mdt setup article
- **home_page**: created template for homepage
- **home_page**: add metadata

### Fixes

- **ci**: get working
- **cz**: remove 'v' suffix from tag
- **cz**: remove 'v' suffix from tag
- **unit_test**: ignore gitlab ide links for alive checks
- **ci**: only deploy when assemble site success
- **assemble_site**: remove downloaded artifacts
- **ci**: url encode artifact path for assemble
- **build**: use correct gitlab-ci index page
- **ci**: typo in includes
- use relative path
- set ssh user
- typo
- **artifacts**: fix fetching ops artifacts and allow publish
- **ssh**: ssh key set to file var
- **ci**: fix pages job to run
- **website-template**: update module to fixed template commit
- **vscode**: don't force mkdocs strict
- **mobile_display**: added padding between sections
- **article**: add required metadata.

### Refactoring

- **assemble_site**: use new job name
- **ci**: use new build job name `Website.Build`
- ad copy holder to article
- clear up MD linting errors
- **blog_post**: renamed to article to reflect direction
- **home_page**: added nfc logo
- **gitlab_templates**: changed to use correct path

## 1.0.0rc1 (2023-05-24)

### feat

- **merge_requests**: added article MR template
- **vscode**: fix junit path to use workspace folder
- **blog_list**: layout not to include post content
- **blog_post**: remove meta.description from page
- **theme**: removed post content from 'blog_list'
- **sitemap**: git_revision_date for page change
- **vscode**: added pytest settings
- **vscode**: added build task
- **minify**: disable minifying website until site ready to deploy
- **minify**: minify the mkdocs static html build files
- **mkdocs**: minify plugin added to pipfile for usage with build
- **emoji**: removed emoji support until a solution can be found to self-host.
- **blog_post**: change location of updated date to be in the social metadata.
- **gitlab**: added  a default issue templete for reporting issues with the website.
- **blog_list**: change articles page to be a preview list of articles.
- **blog_post**: include git revision date plugin
- **blog**: added blog capability to posts
- **markdownlint**: specifiy the allowed inline html elements
- **mkdocs**: use custom plugin from custom-plugins/mkdocs-plugin-tags
- **plugin**: cloned plugin tags repo so it can be customized and used
- **mkdocs**: add lists and task lists to markdown
- **sitemap**: remove sitemap as the changed dates for files is wrong.
- **operations**: Added markdown syntax page.
- **article**: migrated choosing an internet service from old wiki
- **contact**: updated the page content to include how to fix an issue with a page.
- **markdown**: added ability to colour by brand name.
- **markdown**: Support admonations in markdown.
- **footer**: Add colour to the social icons within the page footer
- **mkdocs**: add document creation and last edited date.
- **mkdocs**: Add the default config and the site layout directory

### Fixes

- **mkdocs-plugin-tags**: ensure trailing '/' added to tag hyperlink
- **vscode**: use correct params for tests
- **blog_metadata**: set the date to be in a format that is normal
- **mkdocs-plugin-tags**: fix markdown generation so it passes linting
- **mkdocs-plugin-tags**: ensure heading reference in a url is in lower case.
- **mkdocs-plugin-tags**: the template not using the specified css class for the tag
- **mkdocs-plugin-tags**: Build a relative link for the url to the tag page

### Refactoring

- update article requirements
- **article**: include meta.description
- **mkdocs.yml**: fix tabbing of plugin
- **privacy_test**: rename test 'test_page_external_requests' -> 'test_page_load_external_requests'
- **syntax**: updated tags and added title metadata
- **choose_internet_service**: removed extra tags and moved archive notice to bottom of page
- change hover for content tags to yellow text.
- **navigation**: rename tags -> 'Content Tags'
- **markdown_lint**: correct linting errors
- **mkdocs-plugin-tags**: rebranded plugin to be from nfc
- md linting error, ul must be indent four spaces
- linting error. removed trailing empty line in choosing an internet service.
- **article**: fixing lists in choosing an internet service
- **markdown_lint**: clean up linting errors.

### Tests

- **unit_test**: internal hyperlink validation
- build URLs dont require the build path in the name
- **test_hyperlink_internal_alive_check**: added test
- named test to refelect its function.
- **ssl_hyperlinks_only**: Test added
- **dead_link_check**: test for dead hyperlinks
- **privacy**: print the test data to stdout
- **privacy**: clear the class data
- **unit_test_data**: web driver to be class obj
- **unit_test_data**: include the url in url dict
- **unit_test_data**: chrome driver should not be a class object.
- **data**: add fetching of all hyperlinks
- **data**: created a function to parse url to dict
- **privacy**: Created a test to check external requests during page load

## v1.0.0rc0 (2022-01-29)
