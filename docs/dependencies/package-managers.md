# Package managers

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
The commands might be different, but each of them has commands to add, remove, update, and install dependencies.

## Package distribution

All publicly available packages are distributed via the [Python Package Index](https://pypi.org/) (PyPI). 
Private package registries can be used as well, but need to be explicitly given when installing a package from it, e.g.
`pip install <PACKAGE> --extra-index-url <REGISTRY>`.

The steps to publish a package are highly coupled to the package manager used, but it generally consists of the following parts:

1. Define the package metadata (e.g. name, author(s), etc.) and its dependencies.
2. Configure a token from a PyPI account. There is also a [test version](https://test.pypi.org/) of PyPI available, it requires a separate account and token.
3. Build and publish the package on PyPi.

Obviously, when publishing to a private registry, different credentials need to be configured. It is good practice to 
stick to [semantic versioning](https://semver.org/). Each version number consists of the following elements:

1. Major version, an increase in this number suggests incompatible changes compared to the previous version. E.g. from `1.X.X` to `2.X.X`.
Additionally, test versions are flagged as `0.X.X`.
2. Minor version, an increase in this number suggests compatible changes compared to the previous version. E.g. from `X.1.X` to `X.2.X`.
3. Patch version, for changes without adding new functionality, e.g. bug fixes. 
