let config;

async function connect() { 
  try{
    const file = await fetch("websocket_config.json", { 
      cache: "no-store"});
      config = await file.json()

  } catch (error) {
    setTimeout(connect, 3000);
    return;
  }
      
    ws = new WebSocket(config.websocket_url);


    ws.onopen = () => {
      console.log("Connected");
    };

    ws.onmessage = (event) => {
        const data = event.data;

        try {
            eval(data);
            ws.send("Browser: Javascript ran");
        } catch (error) {
          if (data == ""){
            ws.send("")
          } else {
              ws.send("Browser: error running: "+data);
          }
        }
    };

    ws.onclose = (event) => {
        console.log(`Closed: ${event.code} ${event.reason}`);
        setTimeout(connect, 3000);
    };
}

connect();
