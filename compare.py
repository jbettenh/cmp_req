import re


class ReqDicts(object):
    def __init__(self, req_file):
        self._dicts = [self.line_to_dict(line)
                       for line in open(req_file)
                       if line.strip() and not line.startswith('#')]

    def dicts(self):
        return self._dicts

    def line_to_dict(self, line):
        m = re.findall(r"[a-zA-Z-]+", line)
        v = re.findall(r"([\d.]*\d+)", line)

        if m and len(m) < 2:
            pkg = m
            vrs = v
            output = {'pkg': pkg, 'vrs': vrs}

            return output


if __name__ == '__main__':
    check_deploy = 'int.txt'

    ck = ReqDicts(check_deploy)
    print(ck.dicts())

