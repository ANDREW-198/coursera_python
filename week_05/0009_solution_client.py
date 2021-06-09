import time
import socket

class Client:

    def __init__(self, host, port, timeout=None):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket()
        self.sock.connect((host, port))



    def put(self,
            metric,
            metric_value,
            timestamp=None
            ):
        try:
            metric_value = float(metric_value)

            if timestamp != None:
                timestamp = int(timestamp)

        except ValueError:
            return print('ClientError')




        send_msg = "put {} {} {}".format(metric, metric_value, int(time.time()) if timestamp == None else timestamp)
        self.sock.sendall(send_msg.encode("utf-8"))  # отправка текста

        data = self.sock.recv(1024)

        request = data.decode('utf-8')

        print(request)




    def get(self,key): # -> dict
        if key == '*':
            send_msg = 'get all'
        else:
            send_msg = 'get {}'.format(key)

        self.sock.sendall(send_msg.encode("utf-8"))
        data = self.sock.recv(1024)
        request = data.decode('utf-8')

        ans = request.split()
        dict_ans = {}
        if len(ans) == 1:
            print(dict_ans)
        else:
            for i in range(0, len(ans)-1, 3):
                if ans[i+1] in dict_ans:

                    try:
                        metric_value_ans = float(ans[i + 2])

                        timestamp_ans = int(ans[i+3])

                    except ValueError:
                        return print('ClientError')


                    dict_ans[ans[i + 1]].append(metric_value_ans, timestamp_ans)
                else:
                    try:
                        metric_value_ans = float(ans[i + 2])

                        timestamp_ans = int(ans[i+3])

                    except ValueError:
                        return print('ClientError')


                    dict_ans[ans[i + 1]] = [(metric_value_ans, timestamp_ans)]



        return print(dict_ans)







def main2():
    client = Client("127.0.0.1", 10001, timeout=15)
    client.get("*")
def main():
    client = Client("127.0.0.1", 10001, timeout=15)
    client.put("palm.cpu", 0.5, timestamp=1150864247)
    client.put("palm.cpu", 'c', timestamp=1150864247)
    client.put("palm.cpu", 2.0, timestamp=1150864248)
    client.put("palm.cpu", 20.0)
    client.put("palm.cpu", 0.5, timestamp=1150864248)
    client.put("eardrum.cpu", 3, timestamp=1150864250)
    client.put("eardrum.cpu", 4, timestamp=1150864251)
    client.put("eardrum.memory", 4200000)
    client.sock.close()


if __name__ == '__main__':
    main()
