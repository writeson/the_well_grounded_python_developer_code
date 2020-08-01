import sys

def main(args: list) -> None:

    output_string = None

    # get the user input string
    for arg in args:
        if arg[0] != '-':
            output_string = arg
            args.remove(arg)
            break

    # iterate over the command line arguments
    for arg in args:

        if arg == '-r':
            output_string = ''.join(reversed(output_string))

        elif arg == '-u':
            output_string = output_string.upper()

        else:
            print(f'Unrecognized argument: {arg}')
            sys.exit()
    
    print(output_string)


if __name__ == "__main__":
    main(sys.argv[1:])
    
