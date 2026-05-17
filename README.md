#create the conn_montitor service in systemd
sudo nano /etc/systemd/system/conn_monitor.service

#what to add to the service file

[Unit]
Description=Network Connection Monitoring Daemon
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/monitor.py
Restart=always
User=root

[Install]
WantedBy=multi-user.target
