# Dependency management

!!! abstract "Overview"

    - What are dependencies, and how can they be managed?
    - What are isolated environments, and how can they be used?
    - What are package managers, and how can they be used?
    - What are best practices when distributing packages?

## Dependencies

When working on new software, it is common to re-use existing software from others to cover certain functionalities.
These pieces of software are known as dependencies. When mismanaged, this can lead to unforeseen problems, either during development,
or for the user. This mismanagement can come in different levels, each of which is described with an example below.

!!! example "No management"
    
    Imagine receiving a script from a friend, without any information on what's required to run it. By manually digging through the libraries used,
    the script can finally be run, but apparently only on a MacBook.

The first level doesn't apply any form of management. Any form of automation will be impossible, and to get it to run manually, can be quite a hassle.

!!! example "Some management"

    After sending an email to the imaginary friend, a list with the dependencies is given. It mentions "Numpy", but it doesn't say which version,
    and that it needs at least Python `3.10`. It doesn't say if it will run on the latest version. Getting the script to run is far easier,
    but it runs into an error saying "the 'out' argument in 'maximum' is deprecated".

The second level gives the required dependencies, but doesn't say anything about the versions. Depending on the maturity level of the project,
this might be sufficient, but could lead to a mismatch in the version used in development, and the one the user installs. 

!!! example "Fully managed"

    As it turns out, the "Numpy" dependency should be at least version `2.0`, but no larger than `2.3`, and the script cannot be run on
    Windows machines. Tests for the latest Python builds fail, so `3.13` is the current maximum.

On the fully-managed level, both the lower and upper limits of the dependencies are given. Additional constraints, like an OS-specific dependency,
can usually be defined in a [package manager](#package-managers) as well.

!!! example "Easily breakable dependency"

    The list also mentions another dependency from an individual. The repository needs to be cloned, and set to a specific version,
    otherwise the code build for the current Linux distribution will fail.

The fully-managed level could still contain easily breakable dependencies. Either they are updated infrequently, or simply lack quality.
When adding new dependencies to a code base, it is worth the effort to check the repository for potential red flags.
This can show in the form of failing builds, incomplete test coverage, inconsistent versioning, etc.

!!! info "Question"

    You want to add [this](https://pypi.org/project/apistar/#description) dependency to your code base, what could be potential pitfalls?

??? question "Answer"

    The following items suggest this dependency could easily break in the near-future:

    1. Last update was in 2019.
    2. It reports a code coverage of only 85%.
    3. The suggested Python version is already end-of-life.
    4. No major version (1.X.X) is available.

## Isolated environments

Developers often work on various pieces of software, each with its own set of dependencies. When running these codes from the same environment,
it could lead to conflicts. What if software `A` requires a higher version of a dependency, compared to the maximum allowed version for software `B`?
The idea of isolation has become so popular, all kinds of tools exist to provide an isolated environment, with various levels of automation.

### Virtual environments in Bash

In this section, the idea of isolation is illustrated using the `venv` package from Python, and its package installer PIP.
The `venv` package creates an isolated Python environment, which is called a virtual environment. 

!!! note
  
    The snippets in this section only work in (Git) Bash, see the [Windows](#virtual-environments-on-windows) section for their PowerShell equivalent.

Using the example from the previous section, a Python environment needs to be set up that has the `numpy` package installed, 
from version `2.0` to `2.3`. Additionally, the Python version has to be from `3.10` to `3.13`. To check the current Python version:

```shell
python3 --version
```

This Python command runs via the system interpreter. From this interpreter, a virtual environment can be created. 
It has the same Python version as the system interpreter, but does not include pre-installed packages. Within this isolated environment,
dependencies can be easily managed. Once it is no longer needed, the environment can be removed without leaving traces.
A virtual environment can be created with the following command:

```shell
python3 -m venv ~/workshop/venv
```

!!! note

    Create the workshop directory with the `mkdir ~/workshop` command, if not yet done so previously.

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

### Virtual environments on Windows

On Windows, the sequence of events is identical, only the syntax differs slightly. In Bash, each Python version has its own command,
e.g. `python3`. Once the environment is activated, the `python` command works. In PowerShell, this is always `python`, linking to a specific
Python version. Using the same snippets from the previous section, with their PowerShell equivalent:

1. Python commands:
    
    ```shell
    python --version
    ```
    
    ```shell
    mkdir ~/workshop
    python -m venv ~/workshop/venv
    ```

2. Activating the virtual environment:
    
    ```shell
    ~/workshop/venv/Scripts/activate.ps1
    ```

!!! note

    If a command is missing, it means that it is identical to the one in Bash.

### Managing dependencies with PIP

Combining virtual environments with a package manager is an efficient way for managing dependencies in Python. Different flavours exist,
of which PIP is the pre-installed version. It works with a file called `requirements.txt` in which the dependencies are defined.
To generate this file from an existing environment, run:

```shell
pip freeze > requirements.txt
```

The command generates a list of all the currently installed packages and dumps them in a file. 
Using the virtual environment defined in the previous section, this file will contain the following line:

!!! example "requirements.txt"
     
    numpy==2.3

The file can subsequently be used to set up a new environment:

```shell
pip install --requirement requirements.txt
```

If an environment needs to be cleaned up (including the system interpreter), the following sequence of commands could prove useful:

```shell
pip freeze > requirements.txt
pip uninstall --requirement requirements.txt
```

!!! note

    Run `pip list` on the system interpreter, how many packages are installed?
