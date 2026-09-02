<div align="center">
🛰️ BrowserHook

A lightweight Python WebSocket controller for executing JavaScript in a connected browser.



Python • WebSockets • JavaScript • AsyncIO • Browser Automation

</div>
✨ What is BrowserHook?

BrowserHook is a small Python-based WebSocket server that allows a connected browser page to receive JavaScript commands and execute them remotely.

The project combines:

🐍 Python WebSocket server
🌐 A lightweight browser client
⚡ AsyncIO for communication
🧩 A simple module/script system
🖥️ An interactive terminal interface
🎧 A customizable browser page

Once a browser connects, commands entered into the Python terminal can be sent directly to the browser and executed as JavaScript.

🎬 Demo Flow
$ python3 main.py

Hosting IP: 127.0.0.1
Port: 8765

Browser hook hosting IP: 127.0.0.1
Port: 8080

Browserhook full websocket call back address:
ws://127.0.0.1:8765

Hosting server at: 127.0.0.1:8765.

Browser can have false positives and vice versa.
Type "help" to load help menu

CLIENTS: 1

javascript> document.body.style.background = "black"
javascript> alert("Hello from BrowserHook!")


The connected browser receives the JavaScript and executes it immediately.

🧠 How It Works

BrowserHook consists of two main pieces.

🐍 Python Server

The Python application:

Starts a WebSocket server.
Hosts the browser client from the page/ directory.
Tracks connected WebSocket clients.
Provides an interactive terminal.
Sends JavaScript commands to connected browsers.
Receives status/error messages from the browser.
🌐 Browser Client

The HTML page:

Loads websocket_config.json.
Connects to the configured WebSocket server.
Waits for incoming messages.
Executes received JavaScript.
Sends the result/status back to the server.
Automatically attempts to reconnect if disconnected.

⚙️ Installation

Clone the repository:

git clone https://github.com/YOUR_USERNAME/BrowserHook.git
cd BrowserHook


Install the Python dependencies:

pip3 install -r requirements.txt

🚀 Running

Start the server:

python3 bhook.py


You'll be prompted for the WebSocket and web-server configuration:

Hosting IP:
Port:

Browser hook hosting IP:
Port:


Example:

Hosting IP: 127.0.0.1
Port: 8765

Browser hook hosting IP: 127.0.0.1
Port: 8080


The browser page can then be opened at:

http://127.0.0.1:8080

🎮 Terminal Commands

BrowserHook includes a small interactive command system.

Command	Description
help	Display the command menu
modules	List available scripts
load <module>	Load and execute a module
clear	Clear the terminal
quit	Stop the server
exit	Stop the server

Anything that isn't recognized as a command is treated as JavaScript.

Example
javascript> document.title = "BrowserHook"

javascript> document.body.style.backgroundColor = "black"

javascript> console.log("Hello from Python")

🧩 Script Modules

BrowserHook supports reusable JavaScript modules through the scripts package.

For example:

javascript> modules

    example
    demo
    test


A module can then be loaded with:

javascript> load example


The module's generated JavaScript is sent to every connected browser.

This makes it possible to keep commonly used browser actions organized instead of typing them manually every time.

🌐 Remote Hosting

The WebSocket server can potentially be exposed through a tunneling service such as ngrok.

For example:

ngrok http 8765

You must start ngrok first before running the script.

Then configure the browser client with the resulting WebSocket callback address.

⚠️ Security warning: Exposing this server to the public internet gives anyone who can connect the ability to send JavaScript to connected browsers. Do not expose it publicly without implementing authentication, authorization, encryption, and other appropriate security controls.

For local development, keeping the server bound to 127.0.0.1 is strongly recommended.


Multiple connected clients are maintained through the CLIENTS collection, allowing commands to be broadcast to connected browsers.

⚠️ Security

BrowserHook intentionally provides a powerful mechanism: remote JavaScript execution in a connected browser.

The current implementation should therefore be considered a development / experimental project, not a production-ready remote browser-control system.

In particular:

There is currently no authentication mechanism.
WebSocket traffic may be unencrypted.
Received browser messages are not authenticated.
Public exposure can allow unauthorized users to interact with connected clients.
You should only connect browsers and networks you control.

<div align="center">
🛰️ BrowserHook

Control the browser. From the terminal.

> connected
> waiting for javascript...
> javascript> _


⭐ If you find the project interesting, consider starring the repository.

</div>
