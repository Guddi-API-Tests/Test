import os

import toml


with open('pyproject.toml', 'r') as f:
    data = toml.load(f)
    config: dict = data['tool']['datamodel-codegen']


def main():
    """Runs the datamodel-codegen command and checks if there are any changes
    returns True if changes are made
    """
    output_file_path = config.pop('output')
    if not os.path.exists(output_file_path):
        # run the datamode-code-generator
        os.system('datamodel-codegen')
        return True

    with open(output_file_path, 'r') as f:
        old_file_lines = f.readlines()

    # run the datamode-code-generator
    os.system('datamodel-codegen')

    with open(output_file_path, 'r') as f:
        index = -1
        while line := f.readline():
            index += 1
            if line.startswith('#'):
                continue
            if line == old_file_lines[index]:
                continue
            else:
                return True
        return False


if __name__ == '__main__':
    result = main()
    print(result)