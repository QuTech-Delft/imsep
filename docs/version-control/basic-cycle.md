# Basic development cycle

!!! abstract "Overview"

    - What are branches, and how can a simple model be set up for individual development?
    - How can changes be made in the repository?
    - How can files be restored to a previous version?
    - How can files be exempted from version control?

As Git is extremely popular, it is part of most integrated development environments (IDE) as a GUI.
This can feel more intuitive at first, but the following sections describe the workflow using the original Git commands. 
These are used by the IDE as well, and knowing them gives a better understanding of how Git works.

## Branches

Branching means you diverge from the main line of development and continue to do work without messing with that main line.

When the repository is initialised, a default branch is created, usually named "main" or "master". Apart from the initial setup,
it is good practice to create a new branch from the default branch before starting any form of development. 
This way of branching gives a clear oversight of what is developed where, as depicted below.

![Basic cycle](../assets/images/git_1.jpg)

For the Git examples given on this page, a local repository will suffice. 
The snippet below makes a new directory, creates a local Git repository, and creates the default branch:

```shell
mkdir ~/workshop
cd ~/workshop
git init
```

!!! note

    All the snippets given in this chapter work in both (Git) Bash and PowerShell.

The second step is to create a new branch from the default branch. There are two ways to do this, with the second option
being a shorthand for the first one:

```shell
git branch "feature"
git switch "feature"
```

```shell
git switch --create "feature"
```

!!! note

    The `--create` flag can be replaced with the short version `-c`.

## Commiting changes

Within the feature branch, code can be written, documentation can be added etc. To show the way to commit these changes,
a tedious textfile is used (within the `~/workshop` directory):

```shell
echo "Hello Git!" > code.txt
```

Git registers that the repository contains "untracked" files, as in, changes made to these files can not be tracked,
as there isn't a reference version of the file in the repository yet:

```shell
git status
```

The next step is to add the file to the staging area. If you think of Git as taking snapshots of changes over the life of a project, 
`git add` specifies what will go in a snapshot (the staging area), and `git commit` then actually takes the snapshot, 
making a permanent record of it as a commit. When adding untracked files, it is best to add them individually. 
There is also an option to add all files at once to Git, but this could easily include files which should be [ignored](#ignoring-files):

```shell
git add code.txt
```

The last step is commit this change to the repository. It's good practice to use short, but descriptive commit messages.
Imagine having to find the commit where a bug was introduced, and all of them were called "added feature":

```shell
git commit --message "added text file"
```

To see if everything went as expected, the `git status` command can be called again, to see it empty. 
With new changes, the same cycle is repeated until the feature is completed and the branch can be [merged](#merging) into the default branch. 

Git also has a command to check the differences within a changed file (`git diff`), and logs with all commits (`git log`), 
but with realistic code changes spread over multiple files, the output of these commands can become difficult to interpret. 
It is recommended to use a GUI for this.

## Restoring files

Often it can be useful to make temporary changed to code, simply to check something, or for debugging purposes. 
Git offers a command to immediately restore the file to the version stored in the current branch:

```shell
git restore "<FILE>"
```

Files can also be removed from the staging area, in the scenario they are accidentally added:

```shell
git restore --staged "<FILE>"
```

In both cases, `git status` should reflect the intended recovery.

## Ignoring files

When working with large repositories, and/or a variety of tools that create local files, the Git status page can quickly become filled with files, 
of which a large portion should not be commited. Having to select the right file each time would be an arduous job, 
and in this scenario the ignore functionality comes into its own. Files and/or directories can be ignored based on a pattern, 
of which the following are useful to remember:

- `/hello`, the "hello" directory in the root directory is ignored.
- `hello`, anything named "hello" in the root directory is ignored.
- `*hello*`, anything that contains "hello" in the root directory is ignored.
- `**/*hello*`, anything that contains "hello" in any directory is ignored.

These patterns can be defined the `.gitignore` file, and Git automatically picks up the items to ignore.
The `git status --ignored` command can be used to see the ignored files.

!!! exercise
    
    What is the patterns to ignore the `.idea` folder in the root directory, but not `idea.txt`?

??? Solution
    
    ```text
    /.idea
    ```

## Merging

When developing in a single branch at the time, merging is straight-forward. This becomes a different story when 
collaborating with others, especially on the same piece of code. Chances of getting a [merge conflict](advanced-cycle.md/#merge-conflicts) in these scenarios are high.
For now, a branch can simply be merged into the default branch with the following command:

```shell
git switch "master"
git merge "feature"
```

After a successful merge, first check if the correct branch is checked out with `git branch`, then, the feature branch can be deleted:

```shell
git branch --delete "feature"
```

## Further reading

Next up is the [advanced work cycle](./advanced-cycle.md), which delves further into Git with more advanced scenarios, like merge conflicts and code reviews.
