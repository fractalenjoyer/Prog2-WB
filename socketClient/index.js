const socket = io(window.location.hostname + ":3000");

let userInput = document.querySelector("#inp");
let output = document.querySelector("#output");

let chat = document.querySelector("#chat");
let chatInput = document.querySelector("#chatInput");
let chatButton = document.querySelector("#btn2");

const Notification = {
	Error: 0,
	Warning: 1,
	Info: 2,
};

socket.on("notify", (e) => {
	switch (e.status) {
		case Notification.Error:
			// bör endast ändra id på en div
			// medelandet borde sättas utanför switch
			alert(e.message);
		case Notification.Info:
			console.log(e.message);
	}
});

socket.on("chatUpdate", (data) => {
	let element = document.createElement("div");
	element.innerText = data.sender + ": " + data.message;
	chat.innerHTML += `<div class="chatMessage">${element.innerHTML}</div>`;
	chat.scrollTop = chat.scrollHeight
});


userInput.addEventListener("keyup", (e) => {
	if (e.key === "Enter") {
		socket.emit("registerUser", { name: userInput.value }, (callback) => {
			window.localStorage.setItem("token", callback.token);
			output.innerText = callback.message;
		});
		userInput.style.display = "none";
	}
});

chatButton.onclick = () => {
	window.localStorage.removeItem("token");
	window.location.reload();
}

chatInput.addEventListener("keyup", (e) => {
	if(chatInput.value && e.key == "Enter") {
		socket.emit("chatSent", { message: chatInput.value });
		chatInput.value = "";
	}
});

if (window.localStorage.getItem("token")) {
	socket.emit("login", { token: window.localStorage.getItem("token") }, (callback) => {
		output.innerText = callback.message;
		if (callback.success) {
			userInput.style.display = "none";
		} else {
			console.assert(callback.success, "Login failed");
		}
	});	
}