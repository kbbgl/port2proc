import psutil
import argparse

parser = argparse.ArgumentParser(description="Find what process is listening on an input port")
parser.add_argument('port', type=int)

args = parser.parse_args()

# Get port
port = args.port

if port < 0 or port > 65535:
    raise Exception("Valid ranges for port is between 0 < port < 65535")
    exit(0)

try:
    process = psutil.Process(args.port)
    print("Command line arguments:")
    print(process.cmdline())

    print("Found " + str(len(process.connections())) + " connections.")
    print("Connections details: ")
    for connection in process.connections():
        print(connection)
        af = connection.family

        print(af)

        local_address = connection.laddr
        if local_address.ip == "::" or local_address.ip == "0.0.0.0":
            local_address = "localhost"    
        
        print(local_address)

        remote_address = connection.raddr
        if not all(remote_address):
            print("No remote address found")
            print(remote_address)

        status = connection.status
        print(status)

except psutil.NoSuchProcess as e:
    print(e) 

except psutil.AccessDenied as e:
    print("Cannot read command line arguments. Access denied. Try running using sudo or as an Administrator.")