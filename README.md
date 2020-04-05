# HEIMDALL

Heimdall is a guardian/gatekeeper tool for scanning sensitive data before
committing files to github.

## What is Heimdall

Heimdall is a tool for scanning sensitive data before the staged files are
added to a commit. So, if a user makes some changes into his repository and
tries to commit those changes via `git commit`, those files will be first
scanned by `HEIMDALL` to check whether there are any sensitive data in those
changes that are going to be pushed into repo and informs the user about it.
This process is automated and nothing extra is done for scanning those files.
Infact those files are scanned automaticallywhen git commit is called.

## How to use it.

For easy usage do the following:-

```bash
   pip install secretfy-config-creator==0.0.1a1
   
   heimdall -i // VERY IMPORTANT
```

That's it. And you are ready.

## Test it with sample repo

Do the following for testing the repo

**New repository**

```bash   
    cd /tmp
    mkdir sample-repo
    git init
    echo "Sample test inside a file" >> ns-file.txt
    echo "<some sensitive data like private key>" >> s-file.txt
    git add .
    git config user.name '<user-name>' //Optional
    git config user.email '<email-id>' //Optional
    git commit -m 'Initial commit'
```

This will initiate scanning process.


**Existing repository**

```bash
    cd /tmp
    git clone <repo-name>
    Edit an existing file
    git add <file-name>
    git commit -m "<message>"
```
This will initiate scanning process

