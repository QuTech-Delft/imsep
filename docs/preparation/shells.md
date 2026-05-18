# Shells

In this day and age, it is common to have graphical user interfaces (GUI) for almost everything. An interface based on
typing in commands, known as a command-line interface (CLI) can therefore feel unintuitive at first. 
However, it could save time in the long run compared to a GUI with practice. Secondly, for some tools, a CLI is the only option. 
An example of this is the operating system (OS) shell. It is a CLI to interact with the OS. 

During the workshop, the shell is used extensively to demonstrate software development tools.
The shell differs per OS, and is further described below. Each participant should be familiar with the shell belonging to their OS.

## Linux

Unix-based systems typically use the Bash shell. It can be recognised by the dollar sign at the start of the line.
In the example below, the following commands are executed:

1. Make a new directory in the home folder.
2. Navigate to this directory.
3. Print to the console, capture this output, and redirect it to a file.
4. List the files in the current directory.
5. Print the content of the created file in the console.

!!! example "Bash"

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

## MacOS

Current versions of macOS use a slightly different version of the Bash shell, namely the Z-shell. 
For this workshop, all provided commands work in both shells.

## Windows

The Windows shell (called PowerShell) is completely different from the Bash shell, even though some commands can be used identically (like `cd`).
When switching frequently between a Unix-based system and Windows, Git Bash can be good alternative to PowerShell and is automatically installed with Git.
The example below executes the same steps as in the Linux one, but using the PowerShell syntax:

!!! example "PowerShell"
    
    ```shell
    mkdir ~/some-dir
    cd ~/some-dir
    echo "hello world!" > output.txt
    ls
    Get-Content output.txt
    ```

The handy hotkeys for (Git) Bash unfortunately do not work in PowerShell.

!!! note

    `Get-Content` is one of the many built-in functions of PowerShell. When writing PowerShell scripts, it is best
    practice to use these functions, instead of the Bash equivalent. E.g. `Set-Location` can be used instead of `cd`.
