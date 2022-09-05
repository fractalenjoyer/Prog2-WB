const { Server } = require("socket.io");

const io = new Server(3000);

let users = {};


io.on("connection", (socket) => {
    users[socket.id] = new User(socket);
    setTimeout(() => {
        users[socket.id].addCards([4, 5, 6]);
    }, 2000);
    socket.on("disconnect", () => {
        delete users[socket.id];
        console.log("User disconnected", users);
    })
})

class User {
    constructor(socket) {
        this.name
        this.cards = [1, 2, 3];
        this.socket = socket;
        socket.on("registerUser", (data) => {
            this.name = data.name;
            console.log("User " + this.name + " registered");
        });
    }
    addCards(cards) {
        this.cards.push(cards);
        this.socket.emit("newCards", {cards: cards});
    }
}