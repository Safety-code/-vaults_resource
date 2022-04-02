#Running the ping command using the subprocess module
import subprocess



subprocess.call("ping -c 5 127.0.0.1", shell=True)
