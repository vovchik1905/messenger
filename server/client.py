import socket
from client.client_states import *

HOST = "localhost"  # The remote host
PORT = 5001  # The same port as used by the server
IS_RECONNECT_ENABLED = False

def client_part():
    is_started = False
    while IS_RECONNECT_ENABLED or not is_started:
        is_started = True
        print("Create client")
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((HOST, PORT))
            print("Client connected")
            while True:
                data_bytes = sock.recv(4096)
                received_data = data_bytes.decode()

                answer = prosess_request(received_data)

                data_bytes = answer.encode()
                sock.sendall(data_bytes)

                """data = input("Type the message to send:")
                if data == "exit":
                    print("Close by client")
                    sock.close()
                    print("Client disconnected")
                    yield None
                # Send
                data_bytes = data.encode()
                sock.sendall(data_bytes)
                # Receive
                data_bytes = sock.recv(4096)
                output_data = data_bytes.decode()
                print(f"!!: {output_data}\n")
                #print("Received:", repr(data))
                if not output_data:
                    print("Closed by server")
                    sock.close()
                    print("Client disconnected")
                    yield None
                yield data_bytes.decode()"""


def main():
    loop_checker = True
    client_gen = client_part()
    while loop_checker:
        answer = next(client_gen)
        if answer is None:
            loop_checker = False
        else:
            print(answer)                

if __name__ == "__main__":
    main()