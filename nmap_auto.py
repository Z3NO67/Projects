import os
import sys
import time
#checks to see if the arguments aren't less than two/also showing the usage.
if len(sys.argv) < 2:
    print("Usage: pyhton nmap_auto.py <Target IP>")
    sys.exit()

target = sys.argv[1]
os.system(f"nmap -sVC -p- {target} -oN AutoScan.txt")
print("saving scan...")
time.sleep(1)
print("scan saved to AutoScan.txt")
