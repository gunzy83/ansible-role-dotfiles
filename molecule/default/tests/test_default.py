import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_file1(host):
    f = host.file('/home/gunzy/test1')

    assert f.exists
    assert f.user == 'gunzy'
    assert f.group == 'gunzy'
    assert f.is_symlink


def test_file2(host):
    f = host.file('/home/gunzy/test2')

    assert f.exists
    assert f.user == 'gunzy'
    assert f.group == 'gunzy'
    assert f.is_symlink


def test_file3(host):
    f = host.file('/home/gunzy/test3')

    assert f.exists
    assert f.user == 'gunzy'
    assert f.group == 'gunzy'


def test_dir(host):
    f = host.file('/home/gunzy/test_dir')

    assert f.exists
    assert f.is_directory
    assert f.user == 'gunzy'
    assert f.group == 'gunzy'


def test_file4(host):
    f = host.file('/home/gunzy/test_dir/test4')

    assert f.exists
    assert f.user == 'gunzy'
    assert f.group == 'gunzy'
