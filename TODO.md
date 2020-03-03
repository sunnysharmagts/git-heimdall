- Test cases
- Documentation
- Generate template file from config file.

Good to have
-------------
Need to create a secret creator which would allow user to create secrets. I think it would be better if the template creator module to create secrets templates too based on the template created. Something far-fetched :)

As per my current thought I think there should be a creator API which will create templates from the current configuration file. Hence, it would work something like this :-

- the template file will replace sensitive data in the config file like email id , password, hash etc with mustache data.
- create secrets.yaml file automatically from the configurations file. In case if the config file is already created then, append sensitive data in the secrets.yaml file


CHECK COMMIT FILES
------------------

1) Initialize a generate a hook in pre-commit. The pre-commit should run a
python script which would check if there are any sensitive data in the
committed files or not.
2) Use trufflehog to do this.
3) The diff needs to be pulled in the latest commit.

    Code Flow
    =========

    1) Create a `pre-commit` file for checking the checkin code. This can be done by running a secretfy command like `secretfy init`.
    2) Once any commit is done it would trigger the codescan module of the secretfy tool and would send the staged files changes to that module.
    3) The codescan module would scan the code and inform about any sensitive data present in the commit. 
    4) The committer can go ahead and change the code OR commit the existing code since there can be false positive cases or the committer doesn't care :).
