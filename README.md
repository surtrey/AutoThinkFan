# AutoThinkFan
A small python script to autocally edit the thinkfan.conf file with the new locations of your devices and fans
It was written for use on Linux only, but may work on other Unix-like operating systems.


## equirements
python3, ![thinkfan](https://github.com/vmatare/thinkfan) 


### how to use
the script edits the file at /etc/thinkfan.conf with the new configuration. you can now make thinkfan run on startup by adding the following to your rc.local file
```shell
python /home/user/downloads/autothinkfan.py # replace with the location of autothinkfan.py
thinkfan
```
