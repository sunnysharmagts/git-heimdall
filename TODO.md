- Test cases
- Documentation
- Change the config and baseconfig file to python file so that it can be packaged.
- README needs to be more discrete.
  - More data about the mock.
  - There is too much mentioning of the config. Need separate keywords for each thing.
  - The mock files needs to be descriptive.
  - The keys format in the mustache file needs to be descriptive.
  - Describe the dependencies packages used in this project

Good to have
-------------
Need to create a secret creator which would allow user to create secrets. I think it would be better if the template creator module to create secrets templates too based on the template created. Something far-fetched :)

As per my current thought I think there should be a creator API which will create templates from the current configuration file. Hence, it would work something like this :-

- provide xml, json, yaml config file from which the template will be created.
- the template file will replace sensitive data in the config file like email id , password, hash etc with mustache data.
- create secrets.yaml file automatically from the configurations file. In case if the config file is already created then, append sensitive data in the secrets.yaml file
