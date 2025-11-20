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

another-example

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
Git needs user inputs to resolve the conflict and merge successfully. When executing Git commands from the commandline, 
it will open the text editor Nano by default to resolve the conflicts by hand. 
This program is pure terror and should be abolished from the known universe and beyond.

To demonstrate such a conflict, say two developers have been adding changes to the `.gitignore` file. The first developer
merges with the default branch without problems. As the second developer tries to merge as well, Git prompts to resolve 
the changes made in both the default and feature branches. 

Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque. 
Vitae pellentesque sem placerat in id cursus mi. Cursus mi pretium tellus duis convallis tempus leo. Tempus leo eu aenean sed diam urna tempor. 
Urna tempor pulvinar vivamus fringilla lacus nec metus.

```shell
cd path/to/dir
```

## Merge requests

Lorem ipsum dolor sit amet consectetur adipiscing elit. Adipiscing elit quisque faucibus ex sapien vitae pellentesque. 
Vitae pellentesque sem placerat in id cursus mi. Cursus mi pretium tellus duis convallis tempus leo. Tempus leo eu aenean sed diam urna tempor. 
Urna tempor pulvinar vivamus fringilla lacus nec metus.

## Code reviews

Lorem ipsum dolor sit amet consectetur adipiscing elit. Amet consectetur adipiscing elit quisque faucibus ex sapien. 
Quisque faucibus ex sapien vitae pellentesque sem placerat. Vitae pellentesque sem placerat in id cursus mi.

1. Lorem ipsum dolor sit amet consectetur adipiscing elit.
2. Lorem ipsum dolor sit amet consectetur adipiscing elit.
3. Lorem ipsum dolor sit amet consectetur adipiscing elit.
4. Lorem ipsum dolor sit amet consectetur adipiscing elit.
