import json
import os
import re

import deepdiff
import deepdiff.model


folder_path = os.path.join('src', 'lang')
original_file_path = os.path.join(folder_path, 'de_DE.json')
pattern = re.compile(r"\['([^']*)']")


def format_keys(value: deepdiff.model.PrettyOrderedSet) -> str:
    items = []
    for item in value.items:
        keys = pattern.findall(item)
        items.append('  - `' + '.'.join(keys) + '`')
    return '\n'.join(items)


def main():
    """A function to check if all jsons inside a folder are the same as the original file"""

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f'The folder {folder_path!r} does not exist.')

    if not os.path.exists(original_file_path):
        raise FileNotFoundError(f'The original file {original_file_path!r} does not exist.')

    with open(original_file_path, 'r') as f:
        original_json = json.load(f)

    files = []
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if file_path == original_file_path:
            continue
        with open(file_path, 'r') as f:
            compare_json = json.load(f)
        diff = deepdiff.DeepDiff(original_json, compare_json, ignore_order=True, verbose_level=0)
        file_diff = []
        for key, value in diff.items():
            formatted_values = format_keys(value)
            file_diff.append(f'- **{key}:**\n{formatted_values}\n\n')

        if file_diff:
            file_diff = '\n'.join(file_diff)
            files.append(f'\n<details>\n<summary>{filename}</summary>\n\n{file_diff}</details>')

    if files:
        files_text = '\n'.join(files)
        with open('comment.md', 'w+') as f:
            f.write(f'#### Found Differences in the following files:\n{files_text}')
        return False
    else:
        with open('comment.md', 'w+') as f:
            f.write(f'#### All language files are the same 😃')
        return True


if __name__ == '__main__':
    result = main()
    print(result)
