import time
import psutil as p
import logging as l

#logging to write connection to events file
l.basicConfig(filename="/var/log/connection_monitor.log",
                    level=l.INFO,
                    format="%(asctime)s - %(message)s")

def monitor_connections(interval=5):
    known_connections = set()
    #Iterate over all active connections
    while True:
        current_connections = set()
        for conn in p.net_connections(kind='inet'):
            if conn.raddr: #only tracks established connections
                conn_info = (conn.laddr, conn.raddr, conn.pid)
                current_connections.add(conn_info)

                #log new connections
                if conn_info not in known_connections:
                    proc = p.Process(conn.pid)
                    l.info(f"New Connection | PID: {conn.pid} | Process: {proc.name()} | "
                                 f"Local: {conn.laddr.ip}:{conn.laddr.port} -> "
                                 f"Remote: {conn.raddr.ip}:{conn.raddr.port}")

        known_connections = current_connections
        time.sleep(interval)

if __name__ == "__main__":
    monitor_connections()
