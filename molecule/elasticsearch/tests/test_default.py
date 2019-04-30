import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_elasticsearch_is_installed(host):
    elasticsearch = host.package("elasticsearch")
    assert elasticsearch.is_installed
    assert elasticsearch.version.startswith('6.7.1')


def test_elasticsearch_is_running(host):
    """Test if the services are enabled and running."""
    elasticsearch = host.service("elasticsearch")
    assert elasticsearch.is_enabled
    assert elasticsearch.is_running
