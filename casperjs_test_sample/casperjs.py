import subprocess

CASPERJS = "/usr/local/bin/casperjs"
subprocess.call(['echo', 'Hello World'])
CMD = [CASPERJS, 'casperjs.js']
# pingPopen = subprocess.Popen(args='ping -c4 www.google.cn', shell=True, stdout=subprocess.PIPE)
pingPopen = subprocess.Popen(args='/usr/local/bin/casperjs casperjs.js', shell=True, stdout=subprocess.PIPE)
print pingPopen.stdout.read()

