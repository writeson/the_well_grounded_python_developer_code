import click


@click.command(help='This tool will reverse and/or uppercase a passed string parameters')
@click.option('-r', '--reverse', is_flag=True, default=False, help='reverse the user input string')
@click.option('-u', '--uppercase', is_flag=True, default=False, help='uppercase the user input string')
@click.argument('input_string', type=str)
def main(reverse: bool=False, uppercase: bool=False, input_string=None) -> None:

    output_string = input_string

    if reverse:
        output_string = ''.join(reversed(output_string))

    if uppercase:
        output_string = output_string.upper()

    click.echo(output_string)

if __name__ == "__main__":
    main()
