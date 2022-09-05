import {io} from 'socket.io-client';

class User {
    constructor(socket, name) {
        this.name = name;
        this.cards = [];
        this.socket = socket;
        socket.emit("registerUser", {name: name});
    }
    addCards(cards) {
        this.cards.push(cards);
        console.log("New cards: " + cards);
    }
}

const socket = io('ws://localhost:3000');

let user = new User(socket, "Board");

socket.on("newCards", (data) => {
    user.addCards(data.cards);
    socket.disconnect();
})

