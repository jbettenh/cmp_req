import difflib
import os
import re
import sys
from collections import defaultdict


class ReqDicts(object):
    def __init__(self, file1, file2):
        self.current_server = ''
        self.filename1 = os.path.basename(file1)
        self.filename2 = os.path.basename(file2)
        self.env1 = self.file_2_dict(file1)
        self.env2 = self.file_2_dict(file2)

    def __repr__(self):
        # doesn't work
        output = ''
        for server, modules in self.env1.items():
            output += server
            for module, version in modules.items():
                output += module
        return output

    def file_2_dict(self, file):
        file_dict = {}

        for line in open(file, 'r'):

            server_name = re.search(r'''([A-Z]+[0-9]+)''', line, re.X)
            module_version = re.search(r'''([a-zA-Z-]+).*(\d\.\d\.\d)''', line, re.X)

            if server_name:
                self.current_server = server_name.group(1)
                file_dict[self.current_server] = {}

            if module_version:
                file_dict[self.current_server][module_version.group(1)] = (module_version.group(2))

        return file_dict

    def dicts(self, key=None):
        return list(self.iterdicts(key=key))

    def iter_dicts(self, key=None):
        if key:
            return (item
                    for item in sorted(self.env1, key=key))
        else:
            return (item
                    for item in self.env1)

    def flatten_dict(self):
        self.env1 = [modules
                     for server in self.env1.items()
                     for modules, version in server
                     if version[0]]

        self.env2 = [modules
                     for server in self.env2.items()
                     for modules in server]


if __name__ == '__main__':
    deploy_int = 'files_2_compare/int.txt'
    deploy_prod = 'files_2_compare/prod.txt'

    module_versions = ReqDicts(deploy_int, deploy_prod)

    print(f'Environment 1 is {module_versions.env1}')
    print(f'Environment 2 is {module_versions.env2}')
