import argparse

import psutil


def find_process_by_port(port: int):
    for conn in psutil.net_connections(kind="inet"):
        if conn.laddr and conn.laddr.port == port:
            if conn.status == psutil.CONN_LISTEN:
                try:
                    proc = psutil.Process(conn.pid)
                    return proc.name(), conn.pid
                except psutil.NoSuchProcess:
                    return None
    return None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('port', type=int)
    args = parser.parse_args()

    result = find_process_by_port(args.port)

    if result:
        name, pid = result
        print(f"Port {args.port} is listening by {name} (PID: {pid})")
    else:
        print(f"No program is listening on port {args.port}")


if __name__ == '__main__':
    main()
