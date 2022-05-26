import socket
import requests

ip = socket.gethostbtname(socket.gethostname())
url = "http://"+str(ip)+":5000/set_stat"


requests.post(url, {'data': 1})
