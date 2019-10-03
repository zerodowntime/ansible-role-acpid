import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_acpid_is_running_and_enabled(host):
    acpid = host.service("acpid")
    assert acpid.is_running
    assert acpid.is_enabled
