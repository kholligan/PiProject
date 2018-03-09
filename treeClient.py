import socket

HOST, PORT = "localhost", 8080
MESSAGE = "TALK"

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # sock.connect((HOST, PORT))
    sock.sendto(MESSAGE.encode(), (HOST, PORT))
    print("Request sent to server")


#import asyncio

#@asyncio.coroutine
#def tcp_echo_client(message, loop):
#    reader, writer = yield from asyncio.open_connection('127.0.0.1', 8000, loop=loop)

#    print('Send: %r' % message)
#    writer.write(message.encode())

#    print('Close the socket')
#    writer.close()

#message = 'some message'
#loop = asyncio.get_event_loop()
#loop.run_until_complete(tcp_echo_client(message, loop))
#loop.close()
