"""Advanced decorator tests for Click - targeting low coverage areas"""
import click
from click.testing import CliRunner


def test_deeply_nested_command_groups():
    """Test command groups nested 3 levels deep"""
    @click.group()
    def level1():
        pass
    
    @level1.group()
    def level2():
        pass
    
    @level2.command()
    def level3():
        click.echo("Deep command executed")
    
    runner = CliRunner()
    result = runner.invoke(level1, ['level2', 'level3'])
    assert result.exit_code == 0
    assert "Deep command executed" in result.output


def test_shared_options_propagation():
    """Test option propagation from group to subcommand"""
    @click.group()
    @click.option('--verbose', is_flag=True)
    @click.pass_context
    def cli(ctx, verbose):
        ctx.obj = {'verbose': verbose}
    
    @cli.command()
    @click.pass_context
    def sub(ctx):
        if ctx.obj['verbose']:
            click.echo("Verbose mode ON")
        else:
            click.echo("Normal mode")
    
    runner = CliRunner()
    
    result = runner.invoke(cli, ['sub'])
    assert "Normal mode" in result.output
    
    result = runner.invoke(cli, ['--verbose', 'sub'])
    assert "Verbose mode ON" in result.output


def test_multiple_option_with_validation():
    """Test multiple option with custom validation callback"""
    def validate_email(ctx, param, value):
        emails = []
        for email in value:
            if '@' not in email:
                raise click.BadParameter(f'{email} is not valid')
            emails.append(email)
        return emails
    
    @click.command()
    @click.option('--email', multiple=True, callback=validate_email)
    def send(email):
        for e in email:
            click.echo(f"Sending to: {e}")
    
    runner = CliRunner()
    
    # Valid
    result = runner.invoke(send, [
        '--email', 'test@example.com',
        '--email', 'user@test.com'
    ])
    assert result.exit_code == 0
    assert 'test@example.com' in result.output
    
    # Invalid
    result = runner.invoke(send, ['--email', 'invalid'])
    assert result.exit_code != 0


def test_variadic_arguments_with_options():
    """Test combining variadic arguments with multiple options"""
    @click.command()
    @click.argument('files', nargs=-1, required=True)
    @click.option('--tag', multiple=True)
    def process(files, tag):
        click.echo(f"Processing {len(files)} files")
        click.echo(f"Tags: {len(tag)}")
    
    runner = CliRunner()

    #Valid
    result = runner.invoke(process, [
        'file1.txt', 'file2.txt', 'file3.txt',
        '--tag', 'important',
        '--tag', 'urgent'
    ])

    assert result.exit_code == 0
    assert "Processing 3 files" in result.output
    assert "Tags: 2" in result.output

    result = runner.invoke(process, [
        'file1.txt', 'file2.txt', 'file3.txt'
    ]) 
    assert result.exit_code == 0
    assert "Processing 3 files" in result.output
    assert "Tags: 0" in result.output

    #Invalid 
    result = runner.invoke(process, [
        '--tag', 'important',
        '--tag', 'urgent'
    ])
    assert result.exit_code != 0 



