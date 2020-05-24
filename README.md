# Port 2 Process
#### Input a port, receive information about the process behind it

### Dependencies:

```bash
pip install psutils
```

### Example:

```bash
python port2process.py 5425

# Ouput
Command line arguments:
['C:\\windows\\system32\\svchost.exe', '-k', 'netsvcs', '-p', '-s', 'Schedule']

Found 2 connections.
Connections details:

##### Connection 1 #####
IP Version: IPv4
Local address: localhost
Status: LISTEN
##### Connection 2 #####
IP Version: IPv6
Local address: localhost
Status: LISTEN
```

