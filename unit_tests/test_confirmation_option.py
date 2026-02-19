from click.testing import CliRunner
import click


@click.command()
@click.confirmation_option("--yes", prompt="Confirm? y/n")
def confirm_cmd():
    click.echo("Proceeded with action.")


def test_confirmation_prompt_accepted():
    # If user said yes proceed with action
    runner = CliRunner()
    result = runner.invoke(confirm_cmd, input="y\n")
    assert result.exit_code == 0
    assert "Proceeded with action." in result.output


def test_confirmation_prompt_declined():
    # If user said no do not proceed with action
    runner = CliRunner()
    result = runner.invoke(confirm_cmd, input="n\n")
    assert result.exit_code == 1
    assert "Proceeded with action." not in result.output


def test_confirmation_with_flag():
    # If user specified --yes flag proceed with action
    runner = CliRunner()
    result = runner.invoke(confirm_cmd, ["--yes"])
    assert result.exit_code == 0
    assert "Proceeded with action." in result.output
