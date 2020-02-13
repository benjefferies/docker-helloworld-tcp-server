#!/usr/bin/env python
import socket
import os

def start_tcp_server():
  # Create a socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  # Ensure that you can restart your server quickly when it terminates
  sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

  # Set the client socket's TCP "well-known port" number
  well_known_port = int(os.getenv("TCP_PORT", "8080"))
  sock.bind(('', well_known_port))

  # Set the number of clients waiting for connection that can be queued
  sock.listen(5)

  # loop waiting for connections (terminate with Ctrl-C)
  try:
      while True:
          newSocket, address = sock.accept(  )
          print(f"Connected from {address}")
          # loop serving the new client
          while True:
              receivedData = newSocket.recv(1024)
              if not receivedData: break
              # Echo back the same data you just received
              newSocket.send(bytes("world\n", "UTF-8"))
          newSocket.close(  )
          print(f"Disconnected from {address}")
  finally:
      sock.close(  )

if __name__ == "__main__":
    start_tcp_server()