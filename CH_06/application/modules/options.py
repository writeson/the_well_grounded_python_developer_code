import argparse
from typing import Iterable


parser = argparse.ArgumentParser(
    description='Get the weather by zipcode or city name'
)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument(
    '-z', '--zipcode',
    type=str,
    dest='zipcode',
    default=None,
    help='zipcode of the desired weather information'
)
group.add_argument(
    '-c', '--city',
    type=str,
    dest='city',
    default=None,
    help='city name of the desired weather information'
)
parser.add_argument(
    '-u', '--units',
    type=str,
    dest='units',
    default='I',
    choices=['I', 'M', 'S'],
    help='units to display data in, I=Imperial, M=Metric, S=Scientific'
)
parser.add_argument(
    '-f', '--format',
    type=str,
    default='json',
    choices=['json', 'text'],
    help='the format to get the information in, JSON or text'
)


def get_args(arguments: Iterable = None) -> list:
    """This function parses the passed in list of arguments
    and returns the args as defined by the argparse configuration
    
    Arguments:
        arguments {Iterable} -- The arguments (usually sys.args[1:]) to parse
    
    Returns:
        list -- The args as parsed by the argparse configuration
    """
    return parser.parse_args(arguments)

