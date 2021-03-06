import os
import subprocess as sp
import sys
if sys.stdin.isatty(): #if running interactively
	verbose = True
else:
 	verbose = False
dev = str(sp.check_output("""find /sys/devices -type f -name "temp*_input"|sed 's/^/hwmon /g'""",shell=True, universal_newlines=True))
devconf = str("""(1,	60,	65)
(2,	65,	70)
(3,	70,	75)
(4,	75,	80)
(5,	80,	85)
(7,	85,	32767)""")
# devconf = device temperature and fan speed configs for ThinkFan, respectively.
thinkfan = open("/etc/thinkfan.conf", "w")
thinkfan.writelines(dev +  devconf)
if verbose == True:
	print("configured thinkfan for " + str(dev.count("\n")) + ' devices')
exit()
