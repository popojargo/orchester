- [Getting started](#getting-started)
- [Build](#build)
- [Generate empty config file](#generate-empty-config-file)


## Getting started

1. Clone the repository: `git clone git@github.com:popojargo/orchester.git`
2. Create your virtualenv and activate it.
3. Install your dependencies: `pip install -r requirements.txt`
4. Create an `.orchester.json` configuration file. You can copy the example coming from [.orchester-empty.json](.orchester-empty.json)


## Build

To build the project, do the following:

1. `python setup.py sdist bdist_wheel`
2. `twine upload --repository-url https://pypi.org/legacy/ dist/*`

## Generate empty config file

To generate an empty configuration file based on the one with doc: `python bin/gen_cfg_file.py > .orchester-empty.json`

