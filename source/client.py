import socket
import json

def to_logstashJson(log_d):

    host = socket.gethostname()
    #host = '192.168.42.10'
    port = 9000
    #json_data = json.dumps(LOG, sort_keys=False, indent=2)
    LOG = log_d
    json_data = json.dumps(LOG)
    json_data += '\n'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    s.sendall(json_data.encode())
    data = s.recv(1024)
    s.close()
