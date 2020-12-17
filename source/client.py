import socket
import json
import os 
host = os.environ["ELASTICSEARCH_HOST"]
if (os.environ.get("ELASTICSEARCH_PORT")):
    port = int(os.environ["ELASTICSEARCH_PORT"])
else:
    port = 9000
    
def to_logstash_json(log_d):

    json_data = json.dumps(log_d)
    json_data += '\n'

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(json_data.encode())

    return None
