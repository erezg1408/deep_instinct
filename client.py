import socket
import logging
import pickle


logging.basicConfig(level=logging.INFO, filename='logs/client.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_user_input():
    logging.info("---- Function get_user_input Enter ----")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (add, sub, mul, div): ").strip()
    logging.info("---- Function get_user_input Exit ----")
    return a, b, operation


def main():
    logging.info("---- Function main Enter ----")
    host = '127.0.0.1'
    port = 65432

    a, b, operation = get_user_input()
    request = {'a': a, 'b': b, 'operation': operation}

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        logging.info(f"Connected to server at {host}:{port}")
        s.sendall(pickle.dumps(request))
        logging.info(f"Sent request: {request}")
        data = s.recv(1024)
        response = pickle.loads(data)

    if 'result' in response:
        print(f"The result is: {response['result']}")
    else:
        print(f"Error: {response['error']}")

    logging.info(f"Received response: {response}")
    logging.info("---- Function main Exit ----")


if __name__ == "__main__":
    main()
