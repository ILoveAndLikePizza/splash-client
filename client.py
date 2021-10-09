import socket
from argparse import ArgumentParser
from pynput import keyboard

class Keys:
    def __init__(self, ip):
        self.keys = {"a": False, "d": False, "w": False}
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, 42069))
        self.send()
        while True:
            with keyboard.Listener(on_release=self.on, on_press=self.off) as l:
                l.join()

    def on(self, key):
        if hasattr(key, "char") and key.char in self.keys:
            self.keys[key.char] = False
            self.send()

    def off(self, key):
        if hasattr(key, "char") and key.char in self.keys:
            self.keys[key.char] = True
            self.send()

    def msg(self):
        return "".join([
            f"{int(value)}" for key, value in self.keys.items()
        ]).encode()

    def send(self):
        self.sock.sendall(self.msg())


def main():
    parser = ArgumentParser()
    parser.add_argument("ip", nargs="?", help="ip of the splash server")
    args = parser.parse_args()
    host = "100.64.0.65"
    if "ip" in args and args.ip:
        host = args.ip
    print(f"connecting to {host}")
    try:
        Keys(host)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()