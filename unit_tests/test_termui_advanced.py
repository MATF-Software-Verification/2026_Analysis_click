"""Terminal UI tests to improve termui.py coverage"""
import click
from click.testing import CliRunner
import sys

def test_prompt_basic():
    """Test basic prompt functionality"""
    @click.command()
    def cmd():
        name = click.prompt('Enter name')
        click.echo(f"Hello {name}")
    
    runner = CliRunner()
    result = runner.invoke(cmd, input='Alice\n')
    assert result.exit_code == 0
    assert "Hello Alice" in result.output
    assert "Enter name" in result.output


def test_prompt_with_default():
    """Test prompt with default value"""
    @click.command()
    def cmd():
        name = click.prompt('Enter name', default='World')
        click.echo(f"Hello {name}")
    
    runner = CliRunner()
    
    # Just press enter (use default)
    result = runner.invoke(cmd, input='\n')
    assert result.exit_code == 0
    assert "Hello World" in result.output
    assert "Enter name" in result.output



def test_prompt_with_type():
    """Test prompt with type conversion"""
    @click.command()
    def cmd():
        age = click.prompt('Enter age', type=int)
        click.echo(f"Age: {age}, Type: {type(age).__name__}")   

    runner = CliRunner()
    
    # Valid integer
    result = runner.invoke(cmd, input='25\n')
    assert result.exit_code == 0
    assert "Age: 25" in result.output
    assert "Type: int" in result.output


def test_confirm():
    """Test confirmation prompt"""
    @click.command()
    def cmd():
        if click.confirm('Continue?'):
            click.echo("Continuing")
        else:
            click.echo("Aborted")
    
    runner = CliRunner()
    
    # Yes
    result = runner.invoke(cmd, input='y\n')
    assert "Continuing" in result.output
    
    # No
    result = runner.invoke(cmd, input='n\n')
    assert "Aborted" in result.output


def test_confirm_with_default():
    """Test confirm with default value"""
    @click.command()
    def cmd():
        # Default is True
        if click.confirm('Continue?', default=True):
            click.echo("Yes")
        else:
            click.echo("No")
    
    runner = CliRunner()
    
    # Just press enter (use default=True)
    result = runner.invoke(cmd, input='\n')
    assert "Yes" in result.output


def test_progressbar_display():
    
    @click.command()
    def cmd():
        items = range(5)
        with click.progressbar(items, label='Processing') as bar:
            for item in bar:
                pass
        click.echo("Done")

    runner = CliRunner()
    result = runner.invoke(cmd)

    assert result.exit_code == 0
    assert "Processing" in result.output
    assert "Done" in result.output



def test_progressbar_with_length():
    """Test progress bar with explicit length"""
    @click.command()
    def cmd():
        with click.progressbar(length=100, label='Loading') as bar:
            for i in range(100):
                bar.update(1)
        click.echo("Complete")
    
    runner = CliRunner()
    result = runner.invoke(cmd)
    assert result.exit_code == 0
    assert "Complete" in result.output


def test_pause():
    """Test pause functionality"""
    @click.command()
    def cmd():
        click.pause()
        click.echo("After pause")
    
    runner = CliRunner()
    result = runner.invoke(cmd, input='\n')
    assert result.exit_code == 0
    assert "After pause" in result.output

