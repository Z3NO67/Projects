import nmap
import sys
import io
import pandas as pd

if len(sys.argv) < 1:
   print("input ip address to scan")

nm = nmap.PortScanner()
#does a full port scan on the target
print(f"scanning {sys.argv[1]}...")
nm.scan(sys.argv[1], arguments='-sV -T4 -A')

print(f"\nHost: {sys.argv[1]}")
print(f"State: {nm[sys.argv[1]].state()}")
print("---------------------------------")
#stores the exported csv file in the csv data variable
csv_data = nm.csv()

#takes the data frames reads them and seperates the strings by a semi colon
df = pd.read_csv(io.StringIO(csv_data), sep=';')
print(df.to_string(index=False))

