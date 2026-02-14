"""Advanced utils tests for Click - targeting low coverage areas"""
import click
from click.testing import CliRunner

def test_echo_unicode_characters():
    """Test echo with various Unicode scripts"""
    @click.command()
    def cmd():
        click.echo("Ћирилица")  # Cyrillic
        click.echo("你好世界")    # Chinese
        click.echo("مرحبا")      # Arabic
        click.echo("🎉🚀💯")      # Emoji
    
    runner = CliRunner()
    result = runner.invoke(cmd)
    
    assert result.exit_code == 0
    assert "Ћирилица" in result.output
    assert "你好世界" in result.output
    assert "🎉" in result.output


def test_echo_special_characters():
    """Test echo with special and control characters"""
    @click.command()
    def cmd():
        click.echo("!@#$%^&*()")
        click.echo("Line1\nLine2\nLine3")
        click.echo("Col1\tCol2\tCol3")
    
    runner = CliRunner()
    result = runner.invoke(cmd)
    
    assert result.exit_code == 0
    assert "!@#$%^&*()" in result.output
    assert "Line1" in result.output
    assert "Line3" in result.output


def test_echo_edge_cases():
    """Test echo handles None, empty string, and whitespace without crashing"""
    @click.command()
    def cmd():
        click.echo(None)         
        click.echo("")           
        click.echo("   ")        
        click.echo("\n\n")       
        click.echo("marker")  
    
    runner = CliRunner()
    result = runner.invoke(cmd)
    
    assert result.exit_code == 0
    assert "marker" in result.output
    assert isinstance(result.output, str)
    assert len(result.output) > 0

def test_echo_to_file_unicode():
    """Test echo writing Unicode to file"""
    @click.command()
    @click.argument('output', type=click.File('w'))
    def write(output):
        click.echo("ASCII text", file=output)
        click.echo("Ћирилица", file=output)
        click.echo("你好", file=output)
    
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(write, ['output.txt'])
        assert result.exit_code == 0
        
        with open('output.txt', 'r', encoding='utf-8') as f:
            content = f.read()
            assert "ASCII text" in content
            assert "Ћирилица" in content
            assert "你好" in content


def test_format_filename_unicode():
    """Test filename formatting with Unicode characters"""
    @click.command()
    @click.argument('filename', type=click.Path())
    def show(filename):
        click.echo(f"File: {filename}")
    
    runner = CliRunner()
    
    # Unicode filename
    result = runner.invoke(show, ['Ћирилица.txt'])
    assert result.exit_code == 0
    assert 'Ћирилица.txt' in result.output
    
    # Special characters
    result = runner.invoke(show, ['file@#$.txt'])
    assert result.exit_code == 0
    
    # Very long
    long_name = 'a' * 200 + '.txt'
    result = runner.invoke(show, [long_name])
    assert result.exit_code == 0

def test_get_binary_stream():
    """Test binary stream handling"""
    @click.command()
    @click.argument('output', type=click.File('wb'))
    def write_binary(output):
        output.write(b'Binary data')
        click.echo("Written")
    
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(write_binary, ['output.bin'])
        assert result.exit_code == 0
        
        with open('output.bin', 'rb') as f:
            assert f.read() == b'Binary data'


def test_echo_bytes():
    """Test echoing bytes"""
    @click.command()
    def cmd():
        click.echo(b'Byte string')
    
    runner = CliRunner()
    result = runner.invoke(cmd)
    assert result.exit_code == 0


def test_format_filename_bytes():
    """Test filename formatting with bytes"""
    @click.command()
    @click.argument('filename', type=click.Path())
    def show(filename):
        # format_filename handles bytes/str
        formatted = click.format_filename(filename)
        click.echo(f"File: {formatted}")
    
    runner = CliRunner()
    result = runner.invoke(show, ['test.txt'])
    assert result.exit_code == 0


def test_echo_color_strip():
    """Test echo with color stripping"""
    @click.command()
    def cmd():
        # When not a TTY, colors are stripped
        click.secho("Red text", fg='red')
        click.secho("Blue text", fg='blue')
        click.secho("Bold", bold=True)
    
    runner = CliRunner()
    result = runner.invoke(cmd)
    assert result.exit_code == 0
    # Text should be there without ANSI codes in test env
    assert "Red text" in result.output
    assert "Blue text" in result.output
    assert "\x1b[" not in result.output

    # Allow ANSI codes
    result = runner.invoke(cmd, color=True)
    assert "Red text" in result.output
    assert "Blue text" in result.output
    assert "\x1b[" in result.output
