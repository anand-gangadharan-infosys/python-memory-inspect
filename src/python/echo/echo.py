import socket
from MessageTracker import MessageTracker
from memory_profiler import profile


def listen():
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind(('0.0.0.0', 5555))
    connection.listen(10)
    msgTrack = MessageTracker()
    while True:
        current_connection, address = connection.accept()
        echo(current_connection,msgTrack)

@profile
def echo(current_connection,msgTrack):
    while True:
        data = current_connection.recv(2048)

        if data == 'quit\r\n':
            current_connection.shutdown(1)
            current_connection.close()
            msgTrack.printMessages()
            break

        elif data == 'stop\r\n':
            current_connection.shutdown(1)
            current_connection.close()
            exit()

        elif data:
            current_connection.send(data)
            msgTrack.addMessage(data)
            print data

if __name__ == "__main__":
    try:
        print "Echo Server started on port 5555"
        listen()
    except KeyboardInterrupt:
        pass