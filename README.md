# This example show you how to generate data content on GitHub repository using GitHub Actions.
The pipeline (content-generator.yml) run a Python script that generate a file in TMP directory called 'pkey.txt'. The content of the file is the result of a call of web services.
Finally, the pipeline invoke the commands git commit and git push.


[![run-python](https://github.com/flai78/testactions/actions/workflows/content-generator.yaml/badge.svg?branch=main)](https://github.com/flai78/testactions/actions/workflows/content-generator.yaml)
