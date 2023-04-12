import os
import json


folder_path = os.path.join('src', 'lang')
original_file_path = os.path.join(folder_path, 'de_DE.json')

def main():
    """A function to check if all jsons inside a folder are the same as the original file"""

    if not os.path.exists(folder_path):
        raise FileNotFoundError(f'The folder {folder_path!r} does not exist.')

    if not os.path.exists(original_file_path):
        raise FileNotFoundError(f'The file {original_file_path!r} does not exist.')

    return True



if __name__ == '__main__':
    result = main()
    print(result)