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

2. TestPyPI upload: `twine upload --repository-url https://test.pypi.org/legacy/ dist/*`

3. PyPI upload: `twine upload dist/*`
## Generate empty config file

To generate an empty configuration file based on the one with doc: `python bin/gen_cfg_file.py > .orchester-empty.json`

