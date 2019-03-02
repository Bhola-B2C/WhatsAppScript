import subprocess
import sys

target = sys.argv[1]
message = sys.argv[2]
try:
    time = sys.argv[3]
except IndexError:
    time = "now"
command = 'echo "export DISPLAY=:0 && python whatsapp.py \'{}\' \'{}\'" | at {}'.format(target, message, time)
subprocess.call(command, shell=True)