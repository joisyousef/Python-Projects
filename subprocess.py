import subprocess

#subprocess.call(["calc"],shell=True)

out = subprocess.check_call(["cmd","/c","asd"])

out = subprocess.check_output(["cmd","/c","whoami"])

print("the output was: {}".format(out.decode()))