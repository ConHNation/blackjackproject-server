# Packet reviever, sender and translator

# dependencies
import logging
import socket
import threading

# config
server = None
HOST_ADDR = "127.0.0.1"
HOST_PORT = 420

# initialize logger
log = logging.getLogger("Packet Manager")

# packet reciever
log.info("Initializing packet reciever.")

# function to start server
def start_server(name):
	global HOST_PORT, HOST_ADDR, log

	# sets server object
	log.debug("")
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print(socket.AF_INET)
    print(socket.SOCK_STREAM)

	# starts listening for new players
	log
	log.info("Initializing listener for new players.")
  server.bind((HOST_ADDR, HOST_PORT))
  server.listen(5)
  log.info("Listener online.")

  # starts a thread that listens for new players
	log.info("Moving listener to seperate thread.")
	threading._start_new_thread(accept_clients, (server, " "))