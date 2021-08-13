import re


class ReqDicts(object):
    def __init__(self, req_file):
        self._dicts = [self.line_to_dict(line)
                       for line in open(req_file, 'r')
                       if line.strip() and not line.startswith('#') and not 'modules deployed to' in line]

    def dicts(self, key=None):
        return list(self.iterdicts(key=key))

    def iterdicts(self, key=None):
        if key:
            return (item
                    for item in sorted(self._dicts, key=key))
        else:
            return (item
                    for item in self._dicts)

    def line_to_dict(self, line):
        m = re.search(r'''([a-zA-Z-]+).*(\d\.\d\.\d)''', line, re.X)

        if m:
            output = {m.group(1): m.group(2)}

            return output


if __name__ == '__main__':
    check_deploy_int = 'files_2_compare/int.txt'
    check_deploy_prod = 'files_2_compare/prod.txt'
    # add second txt file
    # compare differences
    # export differences to file
    # allow for multiple lists?

    ckInt = ReqDicts(check_deploy_int)
    ckProd = ReqDicts(check_deploy_prod)
    print(ckInt.dicts())
    print(ckProd.dicts())


    if ckInt.dicts() == ckProd.dicts():
        print('\nThe deployment matches!')
    else:
        print('\nThe deployments are different!')
