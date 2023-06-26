import threading
import random
import queue
import time


def producer(q: queue.Queue, time_in_sec: int, event: threading.Event):
    """
    Produce some random message for given duration of time
    :return:
    """
    startTime = time.time()
    while True:
        current_time = time.time()
        if int(current_time-startTime) >= time_in_sec:
            break
        message = "Message Id: {}".format(random.randint(1, 500000))
        q.put(message)
    event.set()


def consumer(q: queue.Queue, event: threading.Event):
    """
    consume the message until the till the producer notify
    :return:
    """
    while not event.is_set():
        if not q.empty():
            message = q.get()
            print("Received message: {}".format(message))


if __name__ == "__main__":
    eventObj = threading.Event()
    q = queue.Queue()
    duration_in_sec = 2
    prod_th = threading.Thread(target=producer, args=(q, duration_in_sec, eventObj), kwargs={})
    con_th = threading.Thread(target=consumer, args=(q, eventObj), kwargs={})
    start_time = time.time()
    print("Started producer consumer at: {}".format(start_time))
    prod_th.start()
    con_th.start()
    prod_th.join()
    con_th.join()
    end_time = time.time()
    print("Completed producer consumer at: {}, total_time: {}"\
          .format(end_time, end_time-start_time))
