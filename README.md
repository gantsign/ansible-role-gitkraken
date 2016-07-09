Ansible Role: GitKraken
=======================

Role to download and install the [GitKraken](https://www.gitkraken.com) Git client.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# The download URL for the redistributable package
gitkraken_redis_url: https://release.gitkraken.com/linux/gitkraken-amd64.deb

# Path for Ansible to store downloaded files
local_ansible_data_path: '/tmp/ansible/data'
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - { role: gantsign.gitkraken }
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
