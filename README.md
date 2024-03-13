# create-sidebar-for-gitlabwiki

## About 
This is a Python script that creates a custom sidebar for a GitLab wiki page.

## Prerequisite
Python is required to run this tool.<br>
Please make sure that Python commands can be executed on the command line.


## Usage
1. Save the `pre-commit` file in `.git/hooks`
2. Save `create_sidebar.py` to the root directory of the wiki repository
3. When the changes are committed, create_sidebar.py is automatically executed to generate the latest sidebar.


## Restriction
- Only the first level of directories supports folding.<br>
  This is because folding the second and subsequent levels will result in a broken sidebar layout.

## Related Articles
- https://stackoverflow.com/questions/51216965/gitlab-custom-wiki-sidebar-not-working
