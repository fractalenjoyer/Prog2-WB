const { Server } = require("socket.io");

class Users {
	constructor() {
		this.users = {};
	}
	add(socket, data) {
		if (this.find("name", data.name) || String(data.name).length > 15) return true;
		socket.on("disconnect", () => {
			delete this.users[socket.id];
		});
        this.users[socket.id] = new User(data.name, socket);
        io.emit("chatUpdate", { sender: "[Server]", message: `${data.name} has joined the chat` });
	}
	find(field, query) {
		for (let [key, value] of Object.entries(this.users))
			if (value[field] == query) return key;
	}
}

class User {
	constructor(name, socket) {
		this.name = name;
		this.clicks = 0;
		socket.onAny((event, ...args) => {
            if (typeof this[event] === "function")
                this[event](...args);
		});
	}
	chatSent(data) {
		io.emit(
			"chatUpdate",
			(messages[Date.now()] = {
				sender: this.name,
				message: data.message,
			})
		);
	}
    click(callback) {
        callback(this.clicks++);
    }
}

const messages = {};
const users = new Users();
const io = new Server(3000, {
	cors: {
		origin: "*",
		methods: ["GET", "POST"],
	},
});

io.on("connection", (socket) => {
	socket.on("registerUser", (data, callback) => {
		if (users.add(socket, data)) {
            callback("Username not available");
        } else
		    callback("User registered");
            socket.removeAllListeners("registerUser");
	});
});
