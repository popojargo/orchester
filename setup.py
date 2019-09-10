from setuptools import setup, find_packages

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='orchester',
    version='0.0.5',
    packages=find_packages(),
    install_requires=[
        'Flask>=1.0.2,<2',
        'google-api-python-client>=1.7.7,<2',
        'oauth2client>=4.1.3,<5',
        'py-trello>=0.14.0,<1',
        'PyGithub>=1.43.4,<2',
        'slackclient>=1.3.0,<2',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    url='https://github.com/popojargo/orchester',
    license='MIT',
    author='Alexis Côté',
    author_email='alexiscote19@hotmail.com',
    keywords='orchester auth trello github drive google groups slack manage cli',
    description='Orchester allows you to easily add/remove use to your favorite platforms.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    python_requires='~=3.5',
    py_modules=["orchester_cli"],
    entry_points={
        'console_scripts': [
            "orchest = orchester_cli:cli"
        ]
    },
)
