<div align="center">

# 🛰️ BrowserHook

### A lightweight Python WebSocket controller for executing JavaScript in a connected browser.

<br>

`Python` • `WebSockets` • `JavaScript` • `AsyncIO` • `Browser Automation`

<br>

---

</div>

<div align="center">

## ✨ What is BrowserHook?

</div>

<div align="center">

BrowserHook is a small Python-based WebSocket server that allows a connected browser page to receive JavaScript commands and execute them remotely.

<br>

The project combines:

</div>

<table align="center">
<tr>
<td align="center">🐍<br><strong>Python WebSocket server</strong></td>
<td align="center">🌐<br><strong>A lightweight browser client</strong></td>
<td align="center">⚡<br><strong>AsyncIO for communication</strong></td>
</tr>
<tr>
<td align="center">🧩<br><strong>A simple module/script system</strong></td>
<td align="center">🖥️<br><strong>An interactive terminal interface</strong></td>
<td align="center">🎧<br><strong>A customizable browser page</strong></td>
</tr>
</table>

<div align="center">

<br>

Once a browser connects, commands entered into the Python terminal can be sent directly to the browser and executed as JavaScript.

<br><br>

## 🎬 Demo Flow

</div>

```text
╭──────────────────────────────────────────────────────────────╮
│                                                              │
│  $ python3 bhook.py                                          │
│                                                              │
│  Hosting IP: 127.0.0.1                                       │
│  Port: 8765                                                  │
│                                                              │
│  Browser hook hosting IP: 127.0.0.1                          │
│  Port: 8080                                                  │
│                                                              │
│  Browserhook full websocket call back address:               │
│  ws://127.0.0.1:8765                                         │
│                                                              │
│  Hosting server at: 127.0.0.1:8765.                          │
│                                                              │
│  Browser can have false positives and vice versa.            │
│  Type "help" to load help menu                               │
│                                                              │
│  CLIENTS: 1                                                  │
│                                                              │
│  javascript> document.body.style.background = "black"        │
│  javascript> alert("Hello from BrowserHook!")                │
│                                                              │
╰──────────────────────────────────────────────────────────────╯
