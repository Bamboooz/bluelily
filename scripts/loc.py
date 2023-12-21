# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os


def count_code_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    code_lines = 0
    in_comment_block = False

    for line in lines:
        stripped_line = line.strip()

        if stripped_line == '':
            continue

        # Handle multiline comments with triple double-quotes
        if stripped_line.startswith('"""') and not in_comment_block:
            in_comment_block = True
            continue

        if stripped_line.endswith('"""') and in_comment_block:
            in_comment_block = False
            continue

        # Skip lines inside multiline comments
        if in_comment_block:
            continue

        # Handle single-line comments
        if stripped_line.startswith('#'):
            continue

        code_lines += 1

    return code_lines


def should_exclude_folder(folder_name):
    # Add folder names to exclude here
    excluded_folders = ['venv', '__pycache__']
    return folder_name in excluded_folders


def process_folder(folder_path):
    total_lines = 0

    for root, dirs, files in os.walk(folder_path):
        # Exclude certain folders
        dirs[:] = [d for d in dirs if not should_exclude_folder(d)]

        for file_name in files:
            file_path = os.path.join(root, file_name)
            _, extension = os.path.splitext(file_name)
            extension = extension[1:]  # Remove the leading dot

            if extension == 'py':
                total_lines += count_code_lines(file_path)

    return total_lines


def main():
    # Specify the directory path here
    parent = os.path.dirname
    folder_path = parent(parent(__file__))

    if not os.path.isdir(folder_path):
        print("Error: The specified path is not a folder.")
        return

    total_lines = process_folder(folder_path)

    print(f'Total code lines in {folder_path}: {total_lines}')


if __name__ == '__main__':
    # count code lines in bluelily
    main()
