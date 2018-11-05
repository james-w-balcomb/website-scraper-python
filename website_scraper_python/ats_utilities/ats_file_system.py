import errno
import fnmatch
import json
import os


def is_directory_useable(directory_path):

    useable_directory = False

    directory_exist = os.path.exists(directory_path)

    is_directory = os.path.isdir(directory_path)

    is_readable = os.access(directory_path, os.R_OK)

    if directory_exist and is_directory and is_readable:
        useable_directory = True

    return useable_directory


def is_file_useable(file_path_name):

    useable_file = False

    # TODO(JamesBalcomb): make this raise an error if the file does not exist
    exists_file = os.path.exists(file_path_name)
    # TypeError: stat: path should be string, bytes, os.PathLike or integer, not NoneType

    is_file = os.path.isfile(file_path_name)

    is_readable = os.access(file_path_name, os.R_OK)

    if exists_file and is_file and is_readable:
        useable_file = True

    return useable_file


def get_directory_path_list(directory_path):

    directory_path_list = list()

    directory_name_list = get_directory_name_list(directory_path)

    for directory_name in directory_name_list:
        directory_path_list.append(os.path.join(directory_path, directory_name))

    return directory_path_list


def get_directory_path_name_pair(directory_path):

    directory_path_name_pair = list()
    directory_path_name_pair_path_list = list()
    directory_path_name_pair_name_list = list()

    directory_name_list = get_directory_name_list(directory_path)

    for directory_name in directory_name_list:
        directory_path_name_pair_path_list.append(os.path.join(directory_path, directory_name))
        directory_path_name_pair_name_list.append(directory_name)

    # directory_path_name_pair =\
    #     list(list(directory_path_name_pair_path_list), list(directory_path_name_pair_name_list))

    directory_path_name_pair.append(directory_path_name_pair_path_list)
    directory_path_name_pair.append(directory_path_name_pair_name_list)

    return directory_path_name_pair


def get_directory_name_list(directory_path):

    directory_name_list = os.listdir(directory_path)

    return directory_name_list


def get_csv_file_list(directory_path):

    file_name_list = os.listdir(directory_path)

    file_list = list()

    for file in file_name_list:
        if fnmatch.fnmatch(file, '*.csv'):
            file_list.append(file)

    return file_list


def get_csv_file_name_list(directory_path):

    file_name_list = list()

    directory_entries = os.listdir(directory_path)

    for entry in directory_entries:
        if fnmatch.fnmatch(entry, '*.csv'):
            file_name_list.append(entry)

    return file_name_list


def list_of_files(directory):

    return [
        d for d in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, d))
    ]


def dir_to_dict(path):
    """
    https://btmiller.com/2015/03/17/represent-file-structure-as-yaml-with-python.html
    Retrieved: 2018-10-06 12:41
    :param path:
    :return: directory_structure
    :rtype: dict
    """
    directory_structure = dict()

    for directory_name, directory_names, file_names in os.walk(path):
        current_directory_name = os.path.basename(directory_name)
        directory_structure[current_directory_name] = []

        if directory_names:
            for next_directory_name in directory_names:
                # directory_structure[current_directory_name].append(
                #     dir_to_dict(path=os.path.join(path, next_directory_name)))
                next_directory_path = os.path.join(path, next_directory_name)
                # directory_structure[current_directory_name].append(
                #     dir_to_dict(next_directory_path))
                directory_structure[current_directory_name] = dir_to_dict(next_directory_path)

            for file_name in file_names:
                directory_structure[current_directory_name].append(file_name)
        else:
            directory_structure[current_directory_name] = file_names

    return directory_structure


def get_directories_and_files(directory_path_root):
    # def get_directories_and_files(directory_path_root, max_depth=1):

    directories_and_files = dict()

    directories_and_files[directory_path_root] = dict()

    directory_name_list = os.listdir(directory_path_root)

    for directory_name in directory_name_list:

        directory_path = os.path.join(directory_path_root, directory_name)

        directories_and_files[directory_path_root][directory_path] = dict()

        directories_and_files[directory_path_root][directory_path]["directory_name"] = \
            directory_name

        directories_and_files[directory_path_root][directory_path]["files"] = dict()

        file_name_list = os.listdir(directory_path)

        for file_name in file_name_list:

            file_path_name = os.path.join(directory_path, file_name)

            directories_and_files[directory_path_root][directory_path]["files"][
                file_path_name] = dict()

            directories_and_files[directory_path_root][directory_path]["files"][
                file_path_name]["file_name"] = file_name

    return directories_and_files


def dir_to_json(directory_path_root):
    """
    https://unix.stackexchange.com/questions/164602/how-to-output-the-directory-structure-to-json-format
    Retrieved: 2018-=10-06 14:33
    :param directory_path_root:
    :return:
    """

    # import os
    # import errno
    # import json

    def path_hierarchy(path):
        hierarchy = {
            'type': 'folder',
            'name': os.path.basename(path),
            'path': path,
        }

        try:
            hierarchy['children'] = [
                path_hierarchy(os.path.join(path, contents))
                for contents in os.listdir(path)
            ]
        except OSError as e:
            if e.errno != errno.ENOTDIR:
                raise
            hierarchy['type'] = 'file'

        return hierarchy

    dir_json = json.dumps(path_hierarchy(directory_path_root), indent = 4, sort_keys = True)

    return dir_json
