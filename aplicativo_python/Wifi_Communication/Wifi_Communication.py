import http.client

esp8266IP = ''      #preencher
esp8266PORT = 8080  #preencher

client = http.client.HTTPConnection(esp8266IP, esp8266PORT)

def check_connection():
    client.request("GET", "/")
    resp = client.getresponse()
    if resp.status != 200:
        client.close()
        return False

    else:
        client.close()
        return True


def check_status():
    client.request("GET", "/status")
    status = client.getresponse().read().decode("utf-8")
    if status == "R": # R for running
        client.close()
        return True
    else:
        client.close()
        return False

def check_running_time():
    client.request("GET", "/irrigation")
    time = client.getresponse().read().decode("utf-8")
    client.close()
    return time
