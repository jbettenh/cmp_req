import os
import re
from collections import defaultdict


class ReqDicts(object):
    def __init__(self, file1, file2):
        self.servers = defaultdict(lambda: defaultdict(list))
        self.current_server = ''
        self.filename = os.path.basename(file1)
        self.file1_feeder = [self.line2dict(line)
                             for line in open(file1, 'r')
                             if line.strip() and not line.startswith('#')]
        self.file2_feeder = [self.line2dict(line)
                             for line in open(file2, 'r')
                             if line.strip() and not line.startswith('#')]

    def line2dict(self, line):
        server_name = re.search(r'''([A-Z]+[0-9]+)''', line, re.X)
        module_version = re.search(r'''([a-zA-Z-]+).*(\d\.\d\.\d)''', line, re.X)

        if 'modules deployed to' in line:
            self.current_server = server_name.group(1)

        elif module_version:
            # save the module and version
            self.servers[self.current_server][module_version.group(1)].append(module_version.group(2))

    def dicts(self, key=None):
        return list(self.iterdicts(key=key))

    def iterdicts(self, key=None):
        if key:
            return (item
                    for item in sorted(self.servers, key=key))
        else:
            return (item
                    for item in self.servers)


if __name__ == '__main__':
    check_deploy_int = 'files_2_compare/int.txt'
    check_deploy_prod = 'files_2_compare/prod.txt'

    ckInt = ReqDicts(check_deploy_int, check_deploy_prod)
    # ckProd = ReqDicts()

    print(ckInt.servers)

    """
   
    if ckInt.dicts() == ckProd.dicts():
        print('The deployment matches!')
    else:
        print('The deployments are different!')

    print(f'{ckInt.filename:35} {ckProd.filename}')

    """

    for server, modules in ckInt.servers.items():
        print(server)
        for module, version in modules.items():
            print(f'{module:15}{version}')

        print()

