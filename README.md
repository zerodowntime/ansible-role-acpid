# acpid

Role to install acpid, Advanced Configuration and Power Interface event daemon.

## Requirements

- Ansible >= 2.7

### Supported platforms

```yml
- EL
  - 7
- Ubuntu
  - xenial
```

## Default role variables

| Name | Description | Type | Default | Required |
| -----| ----------- | :--: | :------:| :------: |
| acpid__package_state | Whether to install the package or not | string | `present` | True |

**All default variables are described in [defaults/main.yml](defaults/main.yml) file.**

## Static role variables

This section describes static variables implemented in the role.

### Main variables

| Name | Description | Type | Default |
| -----| ----------- | :--: | :-----: |
| acpid__package_name | Package name to be installed | string | `acpid` |
| acpid__service_name | Service name | string | `acpid` |

**All static main variables are described in [vars/main.yml](vars/main.yml) file.**

## Example Playbook

```yaml
    - hosts: all
      become: true
      roles:
        - role: zerodowntime.acpid
```

## License

[Apache License 2.0](LICENSE)

## Support

ZeroDowntime Team <support@zdt.io>

For more information about the project, please visit <https://www.zdt.io/building-blocks/>.