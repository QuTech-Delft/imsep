# Advanced development cycle

!!! abstract "Overview"

    - How can a branch model be set up for collaborative development?
    - What are the causes of merge conflicts, and how can they be resolved?
    - How to protect branches, and use merge requests to change them?
    - How to review code from other collaborators?

## Branches

The branch model for collaborative development is pretty much identical to the individual one, with the only exception being 
that multiple feature branches can exist at the same time. The idea is that each developer works on an item individually,
and merge with the default branch once it is completed. It is not recommended to have multiple people work in the same branch,
this often leads to conflicts when attempting to push changes. The merging does not have to be done in sequence, and is
depicted in the image below.

![Advanced cycle](../assets/images/git_2.jpg)

### Pushing changes

As mentioned above, development is often done in a remote repository, and developers need to push their changes to it.
When commiting changes, only the local branch is affected. The remote version needs to be updated as well. 
In Git, this remote version is called the "origin". When using the `git clone` command, the origin of the default branch is
copied into a local branch, and the configuring is done automatically by Git. This means that, 
in addition to the steps described in the [commit changes](./basic-cycle.md#commiting-changes) section in the previous chapter,
the following command automatically updates the origin:

```shell
git push
```

However, when creating local branches, this configuring is not done automatically. E.g., the following sequence of commands will fail,
as Git does not understand where to push to:

```shell
git clone "<URL>"
git switch -c "feature"
git push
```

This can be solved by "connecting" the local and origin versions of a branch with the following command instead:

```shell
git clone "<URL>"
git switch -c "feature"
git push --set-upstream origin "feature"
```

!!! note
    
    The `--set-upstream` flag can be replaced with the short version `-u`.

After this, changes can simply be pushed with the `git push` command. Like changes, deleting a branch only affects the local version.
To delete an origin, use the following commands:

```shell
git push origin -d "feature"
git push origin -D "feature"
```

The first command pushes a branch delete, for which Git sometimes asks for a confirmation. The second command confirms this push.

!!! note

    Most repository providers have a feature to automatically delete a branch after it is merged.

### Getting up-to-date

As other people could have pushed changes, it is a good habit to frequently check for changes made to the repository.
The first command checks for changes, the second command checks for changes and merges them in the current local branch:

```shell
git fetch
git pull
```

!!! warning

    When working with multiple people in the same branch, or working from multiple devices, e.g. a work laptop and a
    PC at home, the `git pull` command can give rise to a merge conflict if not careful.

Additionally, before a feature branch can be merged, it needs to be "up-to-date" with the changes from the default branch.
In this case, the default branch is first merged into the feature branch. Note that this update is not done with the `git pull` command, 
but rather with `git merge "<DEFAULT>"`. If identical files have changed in both branches, it will lead to a merge conflict.

## Merge conflicts

When Git detects different changes in two different branches, e.g. a feature branch and the default branch, 
or two different versions of the same branch, e.g. a local version and the origin, it warns about a merge conflict. 
Git needs user inputs to resolve the conflict and merge successfully. When executing Git commands from the command-line, 
it will open the text editor Nano by default to resolve the conflicts by hand. 
This program is pure terror and should be abolished from the known universe and beyond.

To demonstrate such a conflict, say two developers have been adding changes to the `.gitignore` file. The first developer
merges with the default branch (`main`) without problems. As the second developer tries to merge as well, Git prompts to resolve 
the changes made in both the default and feature branches:

!!! warning "Git"

    ``` text
    CONFLICT (content): Merge conflict in .gitignore
    Automatic merge failed; fix conflicts and then commit the result.
    ```

During the merge, the `.gitignore` file will look like this:

!!! note ".gitignore"

    ```text
    <<<<<<< HEAD
    change(s) from second developer
    =======
    change(s) from first developer
    >>>>>>> main
    ```

`<<<<<<< HEAD` marks the start of the changes in the current branch. For the second developer, this would be the local feature branch. 
`=======` marks the end of the changes in the current branch, and the start of the changes made in the other branch (`main`).
`>>>>>>> main` marks the end of the other changes.

It is up to the second developer to resolve the conflict, by editing the `.gitignore` file and marking the issue as resolved.
This can be done by editing the file in a text editor or in the GUI provided by an IDE. In both cases, the file should look like this in the end:

!!! note ".gitignore"

    ```text
    change(s) from first developer
    change(s) from second developer
    ```

Note that the mark blocks like `<<<<<<< HEAD` have to be manually removed. After, the standard procedure for commiting changes can be followed,
and the conflict is resolved. When merge conflicts get more complex, e.g. between blocks of code, and across multiple files, a GUI can be preferred. 
It usually excels in giving an overview of what needs to be fixed where compared to the command-line.

## Merge requests

In collaborative repositories, the default branch should be protected. This means no changes can be directly pushed to it,
and merges can only occur when certain conditions have met, e.g. an approval after a [code review](#code-reviews).
A merge request is initiated through a GUI in the remote repository. This can be a webpage, via an IDE, or a separate program, e.g. 
[GitHub desktop](https://desktop.github.com). 

The merge request can be coupled to a CI/CD pipeline, which is an automated execution
of a number of tasks. This can be a task which runs the code tests, checks the dependencies etc. 
Setting up such a pipeline is beyond the scope of this workshop. An open merge request is a sign for other developers that the suggested changes can be reviewed.

## Code reviews

Depending on the maturity of the project and/or developers, the code review can serve multiple functions. 
[Mature](../software-development/index.md#qsmm) projects allows reviews to focus on their primary purpose, namely checking 
if the suggested change(s) are optimal with respect to the desired feature(s) and if it could lead to unforeseen problems.

When reviewing codes from inexperienced developers, or vise versa, it could be useful to understand the syntax, 
and simply ask questions about what is happening. This way, either of them can learn something new, and the proficiency of the team increases. 
Immature projects require extensive reviews, which can include the following additional items:

- understanding the philosophy behind the changes.
- writing and running tests to check for breaking changes.
- checking syntax.

As review remarks are often made as comments online, it is common to make simple ones concise and to the point.
However, this could be perceived as pedantic, and even a little patronising when receiving a few of these comments in sequence. For example:

1. "function names must be lowercase"
2. "docstring does not include parameters"
3. "why don't you use Path library here?"

Especially teams that do not have code quality standards defined beforehand, can have comments related to code style and usage of dependencies.
Code reviews are for the most part about the bigger picture. If there are consistent patterns throughout multiple comments, 
it can be better to summarise it in a single one, or make the remark in-person.

There can also be remarks that are far from tedious, and have a large impact on the suggested changes. In this scenario,
it can be also beneficial to have a small meeting in-person, instead of writing an extensive comment. 
