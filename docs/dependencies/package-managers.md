# Package managers

Although it has the major components for managing dependencies, PIP lacks convenient features offered by other package managers. 
This is especially true when [distributing](#package-distribution) packages. Currently, [Poetry](https://python-poetry.org/) and [UV](https://docs.astral.sh/uv/) are popular managers. 
The commands might be different, but each of them has commands to add, remove, update, and install dependencies.
Before addressing these managers, the [pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/) is discussed.
It serves as a convenient file which many Python tools use for configuration, including the package managers.

## Configuring metadata

Before using the `pyproject.toml` to configure specific packages, the project metadata need to be defined. 
Most of the information is added to the package when it is distributed to a package registry, like the [Python Package Index](https://pypi.org/) (PyPI). 
An example with the mandatory metadata is given below. 

!!! example "pyproject.toml"

    ```text
    [project]
    name = "my-awesome-project"
    version = "0.1.0"
    description = "Let's get bought by Google!"
    readme = "README.md"
    requires-python = ">=3.10,<4.0"
    authors = [{ name = "QuTech", email = "software@qutech.support"}]
    dependencies = [
        "numpy (>=2.3,<2.4)",
    ]
    ```

There are more options available, like a link to the repository, a list of maintainers, etc. In most cases, a [software licence](https://choosealicense.com/licenses/) is given as well.
Either as link, or as a separate file, usually called `LICENCE.md`. Software licencing is beyond the scope of a workshop,
but specific information about the TU Delft software policy can be found [here](https://zenodo.org/records/4629662).

## Poetry

Poetry can be installed on the system using an [installer](https://python-poetry.org/docs/#installation), or in a virtual environment using `pip install poetry`.
It offers commands to both manage and install project dependencies at the same time. To install dependencies from the
`pyproject.toml`, the following command can be used:

```shell
poetry install
```

Dependencies can be managed with the `poetry add ...` and `poetry remove ...` commands. Depending on the command, 
a dependency will be added or removed from the `pyproject.toml` dependencies section. It also works with a file called the `poetry.lock`,
in which a specific version of the dependency is stored. This way, everyone using `poetry install` will install exactly the same version.

!!! tip "Question"

    How can version `2.3.1` of the `pandas` package be added with Poetry?

    ??? info "Solution"
        
        Using the `add` command:
    
        ```shell
        poetry add pandas==2.3.1
        ```

    What happens when you manually add the package to the `pyproject.toml` instead, and run `poetry install`?

    ??? info "Solution"

        !!! failure "Poetry"
            
            pyproject.toml changed significantly since poetry.lock was last generated. Run `poetry lock` to fix the lock file.

Poetry can also be used to set up a virtual environment, sync or update an existing environment, etc. Additionally,
dependencies can be managed in separate groups, of which `dev` is commonly used to indicate packages required for development,
but not for the package itself. The full documentation can be found [here](https://python-poetry.org/docs/).

## UV

UV is [installed](https://docs.astral.sh/uv/getting-started/installation/) and used in a similar matter as Poetry.
It does not have an `install` command, but works with `sync` to update a virtual environment.

## Package distribution

All publicly available packages are distributed via PyPI.
Private package registries can be used as well, but need to be explicitly given when installing a package from it, e.g.
`pip install <PACKAGE> --extra-index-url <REGISTRY>`.

The steps to publish a package are highly coupled to the package manager used, but it generally consists of the following parts:

1. Define the package metadata (e.g. name, author(s), etc.) and its dependencies.
2. Configure a token from a PyPI account. There is also a [test version](https://test.pypi.org/) of PyPI available, it requires a separate account and token.
3. Build and publish the package on PyPI.

Obviously, when publishing to a private registry, different credentials need to be configured. 

### Package versioning

It is good practice to stick to [semantic versioning](https://semver.org/) when releasing a new version of a package. 
Each version number consists of the following elements:

1. Major version, an increase in this number suggests incompatible changes compared to the previous version. E.g. from `1.X.X` to `2.X.X`.
Additionally, test versions are flagged as `0.X.X`.
2. Minor version, an increase in this number suggests compatible changes compared to the previous version. E.g. from `X.1.X` to `X.2.X`.
3. Patch version, for changes without adding new functionality, e.g. bug fixes. 
