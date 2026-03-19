import paramiko
import threading

print("\nWelcome to SHELLY.PY, your ssh tool!")
print("\n----------------------------------")
print("============SHELLY.PY=============")
print("============BY ZENOZ==============")
print("----------------------------------")

hostname = input("\nEnter IP Address: ")
port = int(input("Enter Port to connect to: "))
username = input("\nEnter username to sign in with: ")
password = input("Enter password to sign in with: ")
print("Waiting for connection...")

# Creates an SSH client instance
ssh_client = paramiko.SSHClient()

    # Automatically add the remote server's host key (use with caution in production)
    # For better security, manage known hosts explicitly
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())


# Connect to the remote host using password authentication
# Replace 'hostname', 'PORT', 'username', and 'password' with your details
try:
    ssh_client.connect(hostname= hostname, port= port, username= username, password= password)
    print(f"connect to {hostname}")
    #this varaible opens an interactive shell
    shell = ssh_client.invoke_shell()
    #this function continuously reads the output from the remote shell
    def read_from_shell():
        while True:
            if shell.recv_ready():
                output = shell.recv(1024).decode()
                print(output, end="")
                #print without extra newline
    #start thread to read output
    t= threading.Thread(target=read_from_shell,daemon=True)
    t.start()
    #main while loop to send commands
    while True:
        cmd = input()
        if cmd.lower() in ["exit", "quit"]:
            print("Exiting Shell... ")
            break
        shell.send(cmd + "\n")
        #send command to remote shell
except paramiko.SSHException as e:
    print(f"SSH Connection Error: {e}")

finally:
    ssh_client.close()
