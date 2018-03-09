import RPi.GPIO as GPIO
import socketserver
import random
from time import sleep

TREE_MOUTH = 12
TREE_EYES = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(TREE_MOUTH, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(TREE_EYES, GPIO.OUT, initial=GPIO.LOW)

def open_tree():
    GPIO.output(TREE_MOUTH, GPIO.HIGH)
    GPIO.output(TREE_EYES, GPIO.HIGH)

def close_tree():
    GPIO.output(TREE_MOUTH, GPIO.LOW)
    GPIO.output(TREE_EYES, GPIO.LOW)
 
def talking_tree():
    print("executing tree function")
    open_tree()
    sleep(random.uniform(0.07, 0.3))
    close_tree()

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request[0].strip()
        print('Request received')
        talking_tree()
        return

if __name__ == '__main__':
    HOST, PORT = "localhost", 8080

    server = socketserver.UDPServer((HOST, PORT), RequestHandler)
    print('Server created at {}:{}'.format(HOST, PORT))
    server.serve_forever()

# @asyncio.coroutine
# def process_requests(reader, writer):
#    data = yield from reader.read(100)
#    #addr = writer.get_extra_info('peername')
#    print("Received request") 
#    talking_tree()

#    print("Close the client socket")
#    writer.close()

#loop = asyncio.get_event_loop()
#coro = asyncio.start_server(process_requests, '127.0.0.1', 8000, loop=loop)
#server = loop.run_until_complete(coro)

## Serve requests until force quit
#print('Serving on {}'.format(server.sockets[0].getsockname()))
#try:
#    loop.run_forever()
#except KeyboardInterrupt:
#    pass

# Close the Server
#server.close()
#loop.run_until_complete(server.wait_closed())
#loop.close()

