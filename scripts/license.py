# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

import os


notice = '''# Copyright (c) 2023, Bamboooz
# All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.
'''


def process_files(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if the file is a Python file
            if file_path.endswith(".py"):
                process_file(file_path)


def process_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        content = file.read()

    # Check if the content doesn't start with the specified header
    if not content.startswith(notice):
        new_content = notice + '\n' + content

        with open(file_path, 'w', encoding="utf-8") as file:
            file.write(new_content)
            print(f"Successfully added copyright notice to {file_path}.")


if __name__ == "__main__":
    parent = os.path.dirname
    directory_path = os.path.join(parent(parent(__file__)), "bluelily")
    process_files(directory_path)
