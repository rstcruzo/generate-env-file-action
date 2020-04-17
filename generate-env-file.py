import argparse
from os import environ


parser = argparse.ArgumentParser(
    description='Generate env file from environment.')

parser.add_argument('-i', '--input', help='Input filename path.',
                    default='.env.example')
parser.add_argument('-o', '--output', help='Output filename path.',
                    default='.env')

args = parser.parse_args()

input_variables = {}


def is_empty_line(line):
    """
    Skip line if line is empty or commented.
    """
    stripped = line.lstrip()
    return not stripped or stripped[0] == '#'


def generate_env_files():
    line_errors = 0

    with open(args.input, 'r+') as f:
        for line in f:
            if is_empty_line(line):
                continue

            try:
                key, value = line.split('=')
                input_variables[key] = value
            except ValueError as exc:
                print(f'[ERROR] Unexpected line: {line}')
                line_errors += 1

    if line_errors:
        print(f'{line_errors} unexpected lines in {args.input}.')
        exit(1)

    values_text = ''

    for key, value in input_variables.items():
        if environ.get(key) is not None:
            value = environ[key]
        values_text += f'{key}={value}\n'

    # remove last line break
    values_text = values_text[:-1]

    with open(args.output, 'w+') as f:
        f.write(values_text)
        print(f'Generated {args.output}')


if __name__ == "__main__":
    generate_env_files()