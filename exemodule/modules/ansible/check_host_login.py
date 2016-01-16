#!/usr/bin/env python
# coding:utf-8

from ansible_config import *

class ModuleHandle(object):
    def __init__(self):
        self.hosts = "127.0.0.1"
        self.Runresult = ""

    def run(self):
        try:
            self.Runresult = ansible.runner.Runner(host_list="hosts.ini", pattern=self.hosts, forks=forks, module_name="command", module_args="who",).run()
            if len(self.Runresult['dark']) == 0 and len(self.Runresult['contacted']) == 0:
                return "No hosts found,请确认主机已经添加ansible环境！"
        except Exception, e:
            return str(e)
        return self.Runresult

