def receive_data():
    for i in range(10):
        data = yield
        print(data*data)


def send_data():
    c = receive_data()
    c.send(None)
    i = 0
    while True:
        try:
            c.send(i)
        except StopIteration:
            break
        i += 1
    c.close()

send_data()