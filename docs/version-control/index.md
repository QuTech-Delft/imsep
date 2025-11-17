# Version control

This chapter of the workshop aims to answer questions related to version control. On this page the following topics are addressed:

- What are shells, and how do they differ per operating system (OS)?
- What is Git, and how can it be set up?

!!! note

    Shells are a prerequisite for using Git from the command-line, and is therefore addressed in this chapter. 

## Shells

In this day and age, it is common to have graphical user interfaces (GUI) for almost everything. An interface based on
typing in commands, known as a command-line interface (CLI) can therefore feel unintuitive at first, 
but could save time compared to a GUI with practice. Secondly, for some tools, a CLI is the only option. 
An example of this is the OS shell. It is a CLI to interact with the OS. This shell differs per OS, and is further described below.

### Linux

Unix-based systems use the Bash shell by default. It can be recognised by the dollar sign at the start of the line.
In the example below, the following commands are executed:

1. Make a new directory.
2. Navigate to this directory.
3. Print to the console, capture this output, and redirect it to a file.
4. List the files in the current directory.
5. Print the content of the created file in the console.

!!! example

    ```shell
    mkdir ~/some-dir
    cd ~/some-dir
    echo "hello world!" > output.txt
    ls
    cat output.txt
    ```

Note that these simple commands are like key-value pairs, but commands are often built like `cli command options`.
The option can either be in a short format, or spelled-out fully, for better readability. 
Note that some short-format options don't always have a spelled-out version, and vise versa. E.g. when listing files with the `ls` command,
the hidden files remain hidden. The `-a` or `--all` option shows these files as well:

```shell
ls --all
```

To master the command-line, these hotkeys can be useful:

- `ctrl + w`, clear a word.
- `ctrl + u`, clear the entire line.
- `ctrl + a`, go to the start of the line.
- `ctrl + e`, go to the start of the line.
- `ctrl + r`, search for a previously-executed command.
- `left / right`, navigate through the line.
- `up / down`, go through previously-executed commands in order.

There are many more, which can be found online.

!!! note

    How much longer would it have taken to execute the example in a GUI?

### MacOS

Current versions of macOS use a slightly different version of the Bash shell, namely the Z-shell. 
But, for all intends and purposes, it can be assumed identical for the commands used in this workshop.

### Windows

The Windows shell (called PowerShell) is completely different from the Bash shell, even though some commands can be used identically (like `cd`).
Keep in mind that the path is defined differently on Windows, namely with `\` as separators, and not `/`.
When switching frequently between a Unix-based system and Windows, Git Bash can be good alternative to PowerShell and is automatically installed with Git.
The example below executes the same steps as in the Linux one, but using the PowerShell syntax:

!!! example
    
    ```shell
    mkdir ~\some-dir
    cd ~\some-dir
    echo "hello world!" > output.txt
    ls
    Get-Content output.txt
    ```

The handy hotkeys for (Git) Bash unfortunately do not work in PowerShell.

!!! note

    `Get-Content` is one of the many built-in functions of PowerShell. When writing PowerShell scripts, it is best
    practice to use these functions, instead of the Bash equivalent. E.g. `Set-Location` can be used instead of `cd`.

## Git

Version control starts with a base version of a text-based file, and tracks the changes made over time. 
When used properly, it enables a controlled flow of new features, and a rollback to a previous version will always be 
possible. Next to these major benefits, it offers a complete history of the project, including its authors.
At some point, multiple people could be working in the same file, with many more on the same project. Version control
ensures the changes are applied in a controlled fashion, instead of becoming an incomprehensible mess.

Git is the most commonly-used CLI tool to manage version control. It is applied to a special storage system called a repository.
Normally, the repository is stored in a remote location, like [GitHub](https://github.com/) or [GitLab](https://gitlab.com/), 
and collaborators copy this repository locally to contribute to the project. This process is called "cloning".
With the desired changes made, the contributors then "push" their changes to the remote repository. 
This way of working is common practice among software development teams, but even when working individually, 
using this process can speed up development and safeguard against mistakes.

### Configure Git

Git only requires a few configurations before it can be used, which can be achieved with the following command:

```shell
git config --global user.name "<NAME>"
git config --global user.email "<EMAIL>"
```

The configuration can be found in `~/.gitconfig`. The `~` means the path to the home folder of the current user.
This is usually `C:\users\<USER>` on Windows systems and `/home/<USER>` on Unix-based systems.
When using Git on Unix-based systems, the following configuration can be useful as well:

```shell
git config --global core.editor vim
```

[Vim](https://www.vim.org/) is a terminal user interface (TUI), which sits between a CLI and a GUI. 
It offers an interface to read and edit text, but the commands still have to be typed. 
The following commands are used in this workshop:

- `:`, start a command.
- `esc`, clear the command or exit editing mode.
- `i`, enter editing mode.
- `:wq`, save the changes and exit.
- `:q!`, discard the changes and exit.

Like the Bash hotkeys, there are many more commands, which can be found online.

### Clone a remote repository

Most projects start with an initialised remote repository. Initialised means a default branch is available, usually with a file like a README.
The concept of branches is covered in the next chapter of this workshop. To clone a remote repository:

```shell
git clone "<URL>"
```

!!! note

    Most providers offer an HTTPS and an SSH option to clone repositories with. SSH is safer, but requires a more extensive setup,
    which is not covered in this workshop. With HTTPS the user is usually prompted for credentials, or an access token can be used.

After cloning, it could be useful to store the credentials when prompted for them. This way, they don't need to be re-typed every time.
To configure the helper for the credentials:

```shell
git config credential.helper store
```

Note that the `--global` flag is not used, this configuration is only valid for the current repository. 
The credentials can be found (and deleted) in `~/.git-credentials`. When using SSH, the helper doesn't need to be used.

### Create a local repository

It is possible to start a local repository with Git, use its version control features, and optionally push it to a remote repository later. 
To initialise a local repository in the current directory:

```shell
mkdir "<REPOSITORY>"
cd "<REPOSITORY>"
git init
```

## Further reading

Next up is the [basic work cycle](./basic-cycle.md) with Git. In this chapter the frequently used commands are discussed to create changes in the repository. 
The subsequent [chapter](./advanced-cycle.md) delves further into Git with more advanced scenarios, like merge conflicts and code reviews.
