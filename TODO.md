File formats
- Xml
- json

The file is generated and is getting added to gitignore. The problem is that everytime a new file is generated, its getting added to .gitignore and the .gitignore file does show in the `git status` a modified file.

What if the secretfy-template-creator library is imported and its .gitignore is added to the .gitignore of the current project. In that the case even if the library's .gitignore is changed, the it doesn't matter, it won't be shown in `git status`.

TODO
----
- In case if the .git/info/exclude is not available then no need to add files in that. Although it can be added .gitignore.
- Support for xml data too
- Implement PEP standards.
- Test cases
- Documentation

Good to have
-------------
Need to create a secret creator which would allow user to create secrets. I think it would be better if the template creator module to create secrets templates too based on the template created. Something far-fetched :)

As per my current thought I think there should be a creater API which will create templates from the current configuration file. Hence, it would work something like this :-

- provide xml, json, yaml config file from which the template will be created.
- the template file will replace sensitive data in the config file like email id , password, hash etc with mustache data.
- create secrets.yaml file automatically from the configurations file. In case if the config file is already created then, append sensitive data in the secrets.yaml file
