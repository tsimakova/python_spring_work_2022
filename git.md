# Git Guide
------------
Git initial set up
---------------

`git config --global user.name _MyName_`

`git config --global user.email _MyEmail_`

------------
SSH key generation
---------------
https://selectel.ru/blog/tutorials/how-to-generate-ssh/

**Note that private key file should be protected!**

Set up correct rights:
`chmod =600 _MyFile.pub_`

------------
Troubleshooting
---------------

Permission denied (publickey).
fatal: Could not read from remote repository.

Please make sure you have the correct access rights
and the repository exists.

**Solution**

eval `ssh-agent -s`

`ssh-add KeyFile` (not KeyFile.pub)


------------
Basic git commands
---------------

| Command      | Description |
| ----------- | ----------- |
| git clone MyURL | clone remote repo to local |
| git pull origin MyBranch | update branch |
| git status   | check changes |
| git checkout MyBranch | move to MyBranch branch |
| git log -1   | show commit info |
| git merge | integrate changes |
| git init   | make git repo from folder |
| git config --list | show settings |
| git ignore   | set files/folders that shouldn't be traced |
| git add | index changed files |
| git rm -cashed   | stop tracing |
------------

Connect local repo to remote repo
------------
`git remote add origin MyRepo.git`

------------
