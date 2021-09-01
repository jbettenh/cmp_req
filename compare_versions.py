"""
https://florian-dahlitz.de/articles/create-your-own-diff-tool-using-python
"""
import difflib
import os
import re
import sys


class ReqDicts(object):
    def __init__(self, file1, file2):
        self.current_server = ''
        self.filename1 = os.path.basename(file1)
        self.filename2 = os.path.basename(file2)
        self.env1 = self.file_2_dict(file1)
        self.env2 = self.file_2_dict(file2)
        self.env1_output = self.flatten_dict(self.env1)
        self.env2_output = self.flatten_dict(self.env2)
        self.create_output()

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

    def flatten_dict(self, env):
        flat_env = []

        for server, all_modules in sorted(env.items()):
            flat_env.append('\n')
            flat_env.append(server)
            for module, version in sorted(all_modules.items()):
                flat_env .append(module)
                flat_env .append(version)
                flat_env.append('\n')

        return flat_env

    def create_output(self):
        output_file = 'diff.html'
        if output_file:
            delta = difflib.HtmlDiff().make_file(
                self.env1_output, self.env2_output, fromdesc=self.filename1, todesc=self.filename2
            )
            with open(output_file, "w") as f:
                f.write(delta)

        else:
            delta = difflib.ndiff(self.env1_output, self.env2_output)
            sys.stdout.writelines(delta)


if __name__ == '__main__':
    deploy_int = 'files_2_compare/int.txt'
    deploy_prod = 'files_2_compare/prod.txt'

    module_versions = ReqDicts(deploy_int, deploy_prod)

    # print(f'Environment 1 is {module_versions.env1_output}')
    # print(f'Environment 2 is {module_versions.env2_output}')



