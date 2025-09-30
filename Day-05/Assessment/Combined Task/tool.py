import os
import sys

file = str(sys.argv[1])
mode = os.getenv("APP_MODE") #Create env variable APP_Mode first

print (f"Running {file} in {mode} mode.")