import subprocess
subprocess = subprocess.Popen("pip list", shell=False, stderr=subprocess.PIPE)
subprocess_return = subprocess.stderr.read()
print(subprocess_return)