import platform
import os
os.system('termux-setup-storage')
#os.system('git pull')
#try:os.system('mkdir /sdcard/Chi-DATA')
#except:pass
#try:os.system('mkdir /sdcard/Chi-DATA/OK')
#except:pass
#try:os.system('mkdir /sdcard/Chi-DATA/CP')
#except:pass
try:os.system('touch .prox.txt')
except:pass
arc = str(platform.uname().machine)
if 'arm' in arc:
        __import__("CODER").login()
elif 'aarch' in arc:
        __import__("CODER").login()
else:
        exit(f' Unknow device machine {arc}')
