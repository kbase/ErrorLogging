import socket
import json
import os

host = os.environ.get("ELASTICSEARCH_HOST")
if (os.environ.get("ELASTICSEARCH_PORT")):
    port = int(os.environ["ELASTICSEARCH_PORT"])
else:
    port = 9000

if host is not None:
    print("Elasticsearch endpoint is %s:%d\n" % (host, port))
else:
    print("No ELASTICSEARCH_HOST set, no records will be sent to elasticsearch\n")


def to_logstash_json(log_d):

    if host is not None:
        json_data = json.dumps(log_d)
        json_data += '\n'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(json_data.encode())
    return None
