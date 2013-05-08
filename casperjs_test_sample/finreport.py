import os
import subprocess

my_env = os.environ.copy()
CASPERJS = "/usr/local/bin/casperjs"
CMD = [CASPERJS, 'test', 'good.js']

# print os.environ['PATH'].split(":")
pingPopen = subprocess.Popen(args=CMD, shell=False, stdout=subprocess.PIPE, env=my_env)
print pingPopen.stdout.read()

