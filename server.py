import socket
import logging
import pickle
from arithmetic_operations import Addition, Subtraction, Multiplication, Division

logging.basicConfig(level=logging.INFO, filename='logs/server.log', filemode='a',
                    format='%(asctime)s - %(levelname)s - %(message)s')


def get_operation_instance(op_name):
    if op_name == 'add':
        return Addition()
    elif op_name == 'sub':
        return Subtraction()
    elif op_name == 'mul':
        return Multiplication()
    elif op_name == 'div':
        return Division()
    else:
        raise ValueError("Unknown operation")


def main():
    logging.info("---- Function main Enter ----")
    host = '127.0.0.1'
    port = 65432

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        logging.info("Server started and listening")

        while True:
            conn, addr = s.accept()
            with conn:
                logging.info(f"Connected by {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                request = pickle.loads(data)
                logging.info(f"Received request: {request}")
                try:
                    operation = get_operation_instance(request['operation'])
                    result = operation.execute(request['a'], request['b'])
                    response = {'result': result}
                except Exception as e:
                    response = {'error': str(e)}

                conn.sendall(pickle.dumps(response))
                logging.info(f"Sent response: {response}")

    logging.info("---- Function main Exit ----")


if __name__ == "__main__":
    main()
