const { Server } = require("socket.io");

class Users {
	constructor() {
		this.users = {};
	}
	add(socket, data) {
		if (this.find("name", data.name)) return false;
		let token;
		while (this.find("token", (token = btoa(Math.random()*Date.now()))));
        this.users[socket.id] = new User(data.name, socket, token);
		io.emit("chatUpdate", { sender: "[Server]", message: `${data.name} has joined the chat` });
		return token;
	}
	find(field, query) {
		for (let [key, value] of Object.entries(this.users))
			if (value[field] == query) return key;
	}
	login(token, socket) {
		let user = this.users[this.find("token", token)]
		if (user) {
			io.emit("chatUpdate", { sender: "[Server]", message: `${user.name} has joined the chat` });
			user.addListeners(socket);
			return user.name;
		} 
		return false
	}
}

class User {
	constructor(name, socket, token) {
		this.name = name;
		this.token = token
		this.clicks = 0;
		this.addListeners(socket);
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
	addListeners(socket) {
		socket.onAny((event, ...args) => {
            if (typeof this[event] === "function")
                this[event](...args);
		});
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
		let token;
		if (token = users.add(socket, data)) {
			callback({
				message: "User registered",
				token: token
			});
            socket.removeAllListeners("registerUser");
        } else
			callback({
				message: "Username not available",
			});
		    
	});
	socket.on("login", (data, callback) => {
		let name = users.login(data.token, socket);
		callback({
			name: name,
			message: "User logged in",
			success: name ? true : false
		})
		socket.removeAllListeners("login");
	});
});
