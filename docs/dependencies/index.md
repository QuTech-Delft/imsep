# Dependency management

When working on new software, it is common to re-use existing software for functionalities which are already developed.
These pieces of software are known as dependencies. When mismanaged, this can lead to unforeseen problems, either during development,
or for the enduser. This chapter aims to explain in what form dependencies come, how to manage them using Python as an example,
and how software can be distributed with them.

## Dependencies

Dependencies can become an issue when mismanaged. This mismanagement can come in different levels, from dependencies not being defined at all,
to no versions being specified. Sometimes dependencies are being used from unverified sources with infrequent maintenance.
For each of these situations, an example is given below.

!!! example "No management"
    
    Imagine receiving a script from a friend, without any information on what's required to run it. By manually digging through the libraries used,
    the script can finally be run. With this form of mismanagement, automation is impossible, and to get it to run manually, can be quite a hassle.

!!! example "Some management"

    After sending an email to the imaginary friend, a list with the dependencies is given. It mentions "Numpy", but it doesn't say which version,
    and that it needs at least Python `3.10`. It doesn't say if it will run on the latest version. Getting the script to run is far easier,
    but it runs into an error saying "'out' argument in 'maximum' is deprecated".

!!! example "Fully managed"

    As it turns out, the "Numpy" dependency should be at least version `2.0`, but no larger than `2.3`, and the script cannot be run on
    Windows machines. Tests for the latest Python builds fail, so `3.13` is the current maximum.

!!! example "Easily breakable dependency"

    The list also mentions another dependency from an individual. The repository needs to cloned, and set to a specific version,
    otherwise the code build for the current Linux distribution will fail.

The given examples are tedious, as the dependencies are independent of one another, but as the number gets larger, and interconnected,
this can quickly become a hassle to manage manually.

## Isolated environments

Developers often work on various pieces of software, each with its own set of dependencies. When running these codes from the same environment,
it could lead to conflicts. What if software `A` requires a higher version of a dependency, compared to the maximum allowed version for software `B`?
The idea of isolation has become so popular, all kinds of tools exist to provide an isolated environment, with various levels of automation.
In this section, the idea is illustrated using the `venv` package from Python, and its package installer PIP.

!!! note
  
    The examples in the section below only work in (Git) Bash.

Using the example from the previous section, a Python environment needs to be set up that has the Numpy package installed, 
from version `2.0` to `2.3`. Additionally, the Python version has to be from `3.10` to `3.13`. To check the current Python version:

```shell
python3 --version
```

This Python command runs via the system interpreter. From this interpreter, a virtual environment can be created. 
It has the same Python version as the system interpreter, but does not include pre-installed packages. Within this isolated environment,
dependencies can be easily managed. Once it is no longer needed, the environment can be removed without leaving traces.
A virtual environment can be created with the following command:

```shell
mkdir ~/workshop
python3 -m venv ~/workshop/venv
```

Once created, the environment has to be activated. If this is not done, all the commands use the system interpreter instead!

```shell
source ~/workshop/venv/bin/activate
```

!!! note

    The name of the environment will appear in brackets in the shell after it is activated.

Once activated, PIP can be used to install the necessary dependency:

```shell
pip install numpy==2.3
```

The environment can be deactivated and removed with the following commands:

```shell
deactivate
rm --recursive ~/workshop/venv
```

!!! warning

    Be careful when using the `rm --recursive` command, it deletes the entire directory, including subfolders.

## Package managers

Combining virtual environments with a package manager is an efficient way for managing dependencies in Python. Different flavours exist,
of which PIP was introduced in the previous section. It works with a file called `requirements.txt` in which the dependencies are defined.
To generate this file from an existing environment, run:

```shell
pip freeze > requirements.txt
```

This command generates a list of all the currently installed packages, and dumps it in the file. This file can subsequently be used to 
set up a new environment:

```shell
pip install --requirement requirements.txt
```

Although it has the major components for managing dependencies, other package managers make it even easier, especially when
[distributing](#package-distribution) packages. Currently, [Poetry](https://python-poetry.org/) and [UV](https://docs.astral.sh/uv/) are popular managers. 
Even though the commands are different, each of them has commands to add, remove, update, and install dependencies.

## Package distribution

All publicly available packages are distributed via the [Python Package Index](https://pypi.org/)(PyPI). 
Private package registries can be used as well, but need to be explicitly given when installing a package from it, e.g.
`pip install <PACKAGE> --extra-index-url <REGISTRY>`.

The steps to publish a package are highly coupled to the package manager used, but it generally consists of the following steps:

1. Define the package metadata (e.g. name, author(s), etc.) and its dependencies.
2. Configure a token from a PyPI account. There is also a [test version](https://test.pypi.org/) of PyPI available, it requires a separate account and token.
3. Build and publish the package on PyPi.

Obviously, when publishing to a private registry, different credentials need to be configured. When publishing packages, it is good practice to 
stick to [semantic versioning](https://semver.org/). Each version number consists of the following elements:

1. Major version, an increase in this number suggests incompatible changes compared to the previous version. E.g. from `1.X.X` to `2.X.X`.
Additionally, test versions are flagged as `0.X.X`.
2. Minor version, an increase in this number suggests compatible changes compared to the previous version. E.g. from `X.1.X` to `X.2.X`.
3. Patch version, for changes without adding new functionality, e.g. bug fixes. 
