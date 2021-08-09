import re


class ReqDicts(object):
    def __init__(self, req_file):
        self._dicts = [self.line_to_dict(line)
                       for line in open(req_file)]

    def dicts(self):
        return self._dicts

    def line_to_dict(self, line):
        regexp = ''        # version, defined to be anything between [ and ]

        if line.strip() and not line.startswith('#'):
            m = re.findall('[a-zA-Z-]+', line)
            v = re.findall('[0-9.]+', line)


            if m:
                pkg = m
                vrs = v
                output = {'pkg': pkg,
                          'vrs': vrs}

            else:
                output = None
        else:
            output = None
   
        return output


if __name__ == '__main__':
    check_deploy = 'int.txt'

    ck = ReqDicts(check_deploy)
    print(ck.dicts())

