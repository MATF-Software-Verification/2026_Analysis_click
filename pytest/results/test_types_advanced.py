"""Type tests for uncovered type functionality"""
import click
from click.testing import CliRunner
import os
import tempfile


def test_file_type_read():
    """Test File type for reading"""
    @click.command()
    @click.argument('input', type=click.File('r'))
    def read_file(input):
        content = input.read()
        click.echo(f"Length: {len(content)}")
    
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('test.txt', 'w') as f:
            f.write('Hello World')
        
        result = runner.invoke(read_file, ['test.txt'])
        assert result.exit_code == 0
        assert "Length: 11" in result.output


def test_file_type_write():
    """Test File type for writing"""
    @click.command()
    @click.argument('output', type=click.File('w'))
    def write_file(output):
        output.write('Test output')
        click.echo("Written")
    
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(write_file, ['output.txt'])
        assert result.exit_code == 0
        
        with open('output.txt') as f:
            assert f.read() == 'Test output'


def test_file_type_stdin():
    """Test File type with stdin"""
    @click.command()
    @click.argument('input', type=click.File('r'), default='-')
    def read_stdin(input):
        content = input.read()
        click.echo(f"Got: {content}")
    
    runner = CliRunner()
    result = runner.invoke(read_stdin, input='stdin data\n')
    assert result.exit_code == 0
    assert "Got: stdin data" in result.output


def test_path_type_resolve():
    """Test Path type with resolve_path"""
    @click.command()
    @click.argument('path', type=click.Path(resolve_path=True))
    def show_path(path):
        click.echo(path)
    
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("test.txt", "w") as f:
            f.write("data")

        result = runner.invoke(show_path, ["./test.txt"])

        assert result.exit_code == 0

        expected = os.path.abspath("test.txt")
        assert result.output.strip() == expected


def test_bool_type():
    """Test Bool type conversion"""
    @click.command()
    @click.option('--enabled', type=click.BOOL)
    def cmd(enabled):
        click.echo(f"Enabled: {enabled}")
    
    runner = CliRunner()
    
    # True values
    for val in ['true', 'True', '1', 'yes', 'y']:
        result = runner.invoke(cmd, ['--enabled', val])
        assert "Enabled: True" in result.output
    
    # False values
    for val in ['false', 'False', '0', 'no', 'n']:
        result = runner.invoke(cmd, ['--enabled', val])
        assert "Enabled: False" in result.output


def test_tuple_type():
    """Test Tuple type"""
    @click.command()
    @click.option('--point', type=(float, float))
    def plot(point):
        if point:
            click.echo(f"Point: {point[0]}, {point[1]}")
    
    runner = CliRunner()
    result = runner.invoke(plot, ['--point', '1.5', '2.5'])
    assert result.exit_code == 0
    assert "Point: 1.5, 2.5" in result.output

    result = runner.invoke(plot, ['--point', '1.5'])
    assert result.exit_code != 0


def test_choice_case_insensitive():
    """Test Choice type case insensitive"""
    @click.command()
    @click.option('--env', type=click.Choice(['dev', 'prod'], 
                  case_sensitive=False))
    def deploy(env):
        click.echo(f"Environment: {env}")
    
    runner = CliRunner()
    
    # Different cases should all work
    result = runner.invoke(deploy, ['--env', 'DEV'])
    assert result.exit_code == 0
    
    result = runner.invoke(deploy, ['--env', 'Dev'])
    assert result.exit_code == 0

    result = runner.invoke(deploy, ['--env', 'non-valid'])
    assert result.exit_code != 0

