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

- PIP.

    ```shell
    pip install ...
    ```

- Poetry.

    ```shell
    poetry add ...
    ```

- UV.

    ```shell
    uv ... 
    ```

## Package distribution

Also semantic versioning section?

!!! Note

    Goal of this section is to give the example of setting up and distributing a package in a virtual environment.
