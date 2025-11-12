# Version control

This chapter of the workshop aims to answer questions related to version control. The [shells](#shells) section explains what shells are, 
and how they differ for each operating system (OS). It is a prerequisite for using Git from the command-line,
and is therefore addressed in this chapter. The subsequent [Git](#git) section starts with a summary of what version control is about,
and continues with instructions on how to set it up.

## Shells

In this day and age, it is common to have graphical user interfaces (GUI) for almost everything. An interface based on
typing in commands, known as a command-line interface (CLI) can therefore feel unintuitive at first, but could save time
with practice. Secondly, for some programs, a CLI is the only option. An example of this is the OS shell. It is a CLI to
give commands to the OS. This shell differs per OS, and is further described below.

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

!!! note

    How long would it have taken to execute these steps in a GUI?

To master the command-line, these hotkeys can be useful:

- `ctrl + w`, clear a word.
- `ctrl + u`, clear the entire line.
- `ctrl + a`, go to the start of the line.
- `ctrl + e`, go to the start of the line.
- `ctrl + r`, search for a previously-executed command.
- `up / down`, go through previously-executed commands in order.

### MacOS

Current versions of macOS use a slightly different version of the Bash shell, namely the Z-shell. 
But, for all intends and purposes, it can be assumed identical.

### Windows

The Windows shell (called PowerShell) is completely different from the Bash shell, although some commands can be used identically (like `cd`).
Keep in mind that the path is defined differently on Windows, namely with `\` as separators, and not `/`.
When switching frequently between a Unix-based system and Windows, Git Bash can be good alternative to PowerShell and is automatically installed with Git.
The example below executes the same steps as in the Linux one, but using the PowerShell syntax:

!!! example
    
    ```shell
    cd path/to/dir
    ```

<details>
<summary>Solution</summary>

Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet consectetur adipiscing elit quisque faucibus.

```shell
cd path/to/dir
```

</details>

## Git

Lorem ipsum dolor sit amet consectetur adipiscing elit. Amet consectetur adipiscing elit quisque faucibus ex sapien. 
Quisque faucibus ex sapien vitae pellentesque sem placerat. Vitae pellentesque sem placerat in id cursus mi.

### Configure Git

Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet consectetur adipiscing elit quisque faucibus.

### Create a local repository

Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet consectetur adipiscing elit quisque faucibus.

### Clone a remote repository

Lorem ipsum dolor sit amet consectetur adipiscing elit. Dolor sit amet consectetur adipiscing elit quisque faucibus.

## Further reading


