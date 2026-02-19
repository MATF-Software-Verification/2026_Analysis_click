import click 
from click.testing import CliRunner
 
@click.command()
@click.password_option()
def print_password(password): 
    click.echo(f'Password: {password}.')

def test_password_via_flag():
    # When --password is sent as an option we do not need to confirm it
    runner = CliRunner()
    result = runner.invoke(print_password, ["--password", "secret123"])
    assert result.exit_code == 0
    assert "Password: secret123" in result.output

# When --password option is not sent password needs to be written twice 
def test_password_via_prompt_matching():
    runner = CliRunner()
    result = runner.invoke(print_password, input='secret123\nsecret123\n')
    assert result.exit_code == 0
    assert "Password: secret123" in result.output

def test_password_via_prompt_mismatch():
    runner = CliRunner()
    result = runner.invoke(print_password, input='secret123\nsecret\n')
    assert result.exit_code == 1
    assert "Error: The two entered values do not match." in result.output
    assert "secret123" not in result.output
