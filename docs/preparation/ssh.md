# SSH

In software development, managing automated access with minimal rights is one of the most important aspects. 
If done incorrectly, this often leads to news articles and/or lawsuits. This page describes how to set up [SSH](https://www.geeksforgeeks.org/computer-networks/introduction-to-ssh-secure-shell-keys/) authentication,
a safe way to manage access to code repositories and virtual machines. 

During the workshop, this form of authentication is used to give access to protected resources, like the code repository.

## Generating an SSH key

Typically, SSH keys are stored in the `~/.ssh` folder. New keys can be generated using the `ssh-keygen` CLI tool:

```shell
ssh-keygen -t <ENCRYPTION> -f <NAME>
```

E.g. to generate a key for GitLab using the EdDSA algorithm as an encryption type:

```shell
ssh-keygen -t ed25519 -f gitlab
```

Two files will be generated in the `~/.ssh` folder, `gitlab` and `gitlab.pub`. The `gitlab` file contains the secret private key.
The `gitlab.pub` file contains the public key, which can be used to grant access.
In GitLab, this key can be added via the website under the account preferences.

!!! warning

    Never share your private key with anyone!
