import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize("package", [
    'Cython', 'numpy', 'python-jinja2', 'python-matplotlib', 'python2-numexpr',
    'python-pillow', 'python2-pip', 'python-tables', 'PyYAML'])
def test_packages(host, package):
    assert host.package(package).is_installed
