Ansible Role: dotfiles
======================

Installs dotfiles by symlinking them from another directory (usually a git repository).

Requirements
------------

A directory or git repository containing your dotfiles and an inventory file in YAML format is required. The file should follow the following data structure:

```yaml
- src: "zsh/zshrc"
  dest: "~/.zshrc"
  mode: "0644"
  post_command: "zgen update && source ~/.zshrc"
```

The `post_command` mapping is optional for each file and is run in a handler after the rest of the run is complete.

The `mode` mapping is also optional and is used for tools to restore files and directories to their original locations.

Role Variables
--------------

Available variables are listed below along with default values (see `defaults/main.yml'):

```yaml
dotfiles: []
```

List of files to deploy/link. This defaults to an empty list but should be included in the inventory file as per above.

```yaml
dotfiles_inventory_file: inventory.yml
```

Inventory file name.

```yaml
dotfiles_directory: "{{ playbook_dir }}"
```

Directory where dotfiles exist. Defaults to the `playbook_dir` variable.

```yaml
dotfiles_inventory: "{{ dotfiles_directory }}/{{ dotfiles_inventory_file }}"
```

Location of the inventory file. Defaults to a combination of the `dotfiles_directory` and `dotfiles_inventory_file` variables.

```yaml
dotfiles_history_file: "{{ dotfiles_directory }}/.history.yml"
```

Location of the history file that is stored between runs (allows for files to be removed from the inventory).

```yaml
dotfiles_previous: []
```

Previously installed inventory entries. This defaults to empty and is populated by the history file.

```yaml
dotfiles_post_items: []
```

Post run commands to run. This defaults to empty and is populated as the role is run.


Dependencies
------------

No Galaxy dependencies are required for this role.

Example Playbook
----------------

Assuming the role has been installed, to run this role from inside a dotfiles repository:

```yaml
- hosts: localhost
  roles:
    - role: gunzy83.dotfiles
```

To run this with a dotfiles repository somewhere else:

```yaml
- hosts: localhost
  roles:
    - role: gunzy83.dotfiles
      dotfiles_directory: /some/dotfiles/dir/
```

License
-------

BSD

Author Information
------------------

This role was created in 2016 by [Ross Williams](http://rosswilliams.id.au/).
