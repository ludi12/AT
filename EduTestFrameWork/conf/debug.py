# -*-coding:utf-8 -*-
import yaml
def read_conf(filename):
    with open(filename) as f:
        return yaml.load(f)
if __name__ == '__main__':
    print read_conf('testcase_conf.yml')
