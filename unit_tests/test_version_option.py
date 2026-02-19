from click.testing import CliRunner
import click
import importlib.metadata

def test_version_explicit(): 

    @click.command()
    @click.version_option(version='1.2.3')
    def cli_version():
        pass

    runner = CliRunner()
    result = runner.invoke(cli_version, ['--version'])
    assert result.exit_code == 0 
    assert 'cli-version, version 1.2.3' in result.output

def test_version_custom_message():

    @click.command('Custom message')
    @click.version_option(version='1.2.3', message='v%(version)s')
    def cli_version():
        pass

    runner = CliRunner()
    result = runner.invoke(cli_version, ['--version'])
    assert result.exit_code == 0 
    assert 'Custom message, version v1.2.3'

def test_version_from_package():
    expected_version = importlib.metadata.version("click")
    @click.command()
    @click.version_option(package_name="click")
    def click_version():
        pass

    runner = CliRunner()
    result = runner.invoke(click_version, ["--version"])
    assert result.exit_code == 0
    assert f'click-version, version {expected_version}' in result.output

def test_version_package_not_found():
    @click.command()
    @click.version_option(package_name="invalid-package")
    def invalid_package():
        pass

    runner = CliRunner()
    result = runner.invoke(invalid_package, ["--version"])
    assert result.exit_code != 0
    assert isinstance(result.exception, RuntimeError)