import argparse


def main() -> None:

    parser = argparse.ArgumentParser(description='Reverse / Capitalize some text')
    parser.add_argument(
        '-r', '--reverse',
        action='store_true',
        dest='reverse',
        default=False,
        help='reverse the string passed as a parameter'
    )
    parser.add_argument(
        '-u', '--uppercase',
        action='store_true',
        dest='uppercase',
        default=False,
        help='uppercase the string passed as a parameter'
    )
    parser.add_argument(
        'input_string',
        type=str,
        help='user input string to process'
    )
    args = parser.parse_args()

    output_string = args.input_string

    if args.reverse:
        output_string = ''.join(reversed(output_string))

    if args.uppercase:
        output_string = output_string.upper()

    print(output_string)


if __name__ == "__main__":
    main()
