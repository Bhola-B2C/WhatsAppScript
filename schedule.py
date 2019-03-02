import subprocess

f = open("error.log", "a")
command = 'echo "export DISPLAY=:0 && python whatsapp.py" | at 16:47'
subprocess.call(command, shell=True)