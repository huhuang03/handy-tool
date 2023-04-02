import argparse
import os
import json
import subprocess


def login():
    pass


def connect(server):
    os.system(f"ssh {server['server']}")


def list_remotes():
    server_list = load_list()
    print(server_list)


RESERVE_NAME = []

PATH_AUTHORIZED_KEYS = ".ssh/authorized_keys"

PATH_SERVER_LIST = os.path.join(os.path.dirname(__file__), "../.server_list.txt")

def load_list() -> [dict]:
    if not os.path.exists(PATH_SERVER_LIST):
        return []
    f = open(PATH_SERVER_LIST, 'r', encoding="utf-8")
    data = json.loads(f.read())
    f.close()
    if data:
        return data
    else:
        return []


def save_list(data):
    f = open(PATH_SERVER_LIST, 'w', encoding="utf-8")
    f.write(json.dumps(data))
    f.close()


def add(args):
    name = args.name
    if name in RESERVE_NAME:
        exit(f"{name} is reserved, please use another name")
    # ok, let's do some check
    local_ssh_pub = os.path.expanduser("~/.ssh/id_rsa.pub")
    if not os.path.exists(local_ssh_pub):
        exit("Can't find id_rsa.pub file, did you create one?")
    with open(local_ssh_pub, 'r') as f:
        id_rsa_text = f.read().strip()

    assert (id_rsa_text)

    # ok, now let's read the rmote known_keys
    username_host = input("please input username@host: ")
    already_added = False
    try:
        authorized_keys = subprocess.check_output(f'ssh {username_host} "cat .ssh/authorized_keys"', shell=True,
                                                  timeout=1)
        authorized_keys = authorized_keys.decode("utf-8")
        already_added = id_rsa_text in authorized_keys
    except subprocess.SubprocessError:
        # leave empty
        pass

    if already_added:
        print(f"already configured, just add the {name} into remote list")
        save_list(load_list() + [{'name': name, 'server': username_host}])
    else:
        # ok, we need config the it now.
        subprocess.run(f'cat ~/.ssh/id_rsa.pub | ssh {username_host} "cat >> {PATH_AUTHORIZED_KEYS}"')


def copy():
    pass


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    command_add = subparsers.add_parser("add", help="add a server")
    command_add.add_argument("name", type=str, help="a remember name, not the remote username")

    subparsers.add_parser("list", help="list all server")

    data = load_list()
    for item in data:
        subparsers.add_parser(item['name'], help=f"connect to {item['name']}[{item['server']}]")

    args = parser.parse_args()

    if args.command == "add":
        add(args)
    elif args.command == "list":
        list_remotes()
    elif args.command in [item['name'] for item in data]:
        connect([item for item in data if item['name'] == args.command][0])


if __name__ == "__main__":
    pass
