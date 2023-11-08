import io from 'socket.io-client';

// You might want to change this to wss://plutonication-acnha.ondigitalocean.app/
// or other URL, if you want to use your own endpoint.
const socket = io("ws://127.0.0.1:8000");

// Register on pong event handler
socket.on("pong", (message) => { console.log("pong: " + message) })

// Wait for the client to connect
await new Promise((resolve) => {
    socket.on("connect", () => {
        console.log("Connected")
        resolve()
    })
})

// Overwhelm the limiter by calling it multiple times in quick succesion
for (let i = 0; i < 50; i++) {
    // console.log(i)
    socket.emit("ping", i)
    await new Promise(resolve => setTimeout(resolve, 50));
}

if (!socket.connected) {
    console.log("Client has been banned and disconnected.")
}
