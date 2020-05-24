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
['C:\\windows\\System32\\svchost.exe', '-k', 'LocalServiceNetworkRestricted', '-p', '-s', 'EventLog']
Found 2 connections.
Connections details:

AddressFamily.AF_INET6
localhost
LISTEN

AddressFamily.AF_INET
localhost
LISTEN
```

