import socket
import argparse
from tracemalloc import start
from colorama import init, Fore
from threading import Thread, Lock
from queue import Queue

init()

GREEN = Fore.GREEN
RED = Fore.RED
RESET = Fore.RESET

N_THREADS = 200
q = Queue()
print_lock = Lock()

def port_scan(port):
    try:
        s = socket.socket()
        s.connect((host, port))
    except:
        s.close()
    else:
        with print_lock:
            print(f"{GREEN}[!] {host:15}:{port:15} is open    {RESET}")
    finally:
        s.close()

def scan_thread():
    global q
    while True:
        worker = q.get()
        port_scan(worker)
        q.task_done()

def main(host, ports):
    global q
    for t in range(N_THREADS):
        t = Thread(target=scan_thread)
        t.daemon = True
        t.start()
    for worker in ports:
        q.put(worker)
    q.join()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Port Scanner")
    parser.add_argument("host", help="Host to scan.")
    parser.add_argument("--ports", "-p", dest="port_range", default="1-65535", help="Port range to scan, default range is 1-65535 (all ports)")
    args = parser.parse_args()
    host, port_range = args.host, args.port_range

    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)

    ports = [ p for p in range(start_port, end_port)]

    main(host, ports)
