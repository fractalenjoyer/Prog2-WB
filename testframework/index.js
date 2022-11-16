const { spawn } = require("node:child_process");
const fs = require("fs");

async function runTest(file, input, output) {
	const process = spawn("python", [file], { shell: true });
	process.on("exit", (code) => {
		if (code !== 0) {
			console.error(`Process exited with code ${code}`);
			return;
		}
	});
	let i = 0;
	let resolves = [];
	let promises = Array.from(
		{ length: output.length },
		() => new Promise((resolve) => resolves.push(resolve))
	);
	process.stdout.on("data", (data) => {
		let str = data.toString().replace(/(\r\n|\n|\r)/gm, "");
		resolves[i]();
		console.assert(str === output[i], `Expected: ${output[i++]}, got: ${str}`);
	});
	for (let a of input) {
		process.stdin.write(a + "\n");
	}
	await Promise.all(promises);
    return
}

runTest(
	"./testframework/test.py",
	[
		"10",
		"too high",
		"3",
		"too low",
		"4",
		"too high",
		"2",
		"right on",
		"5",
		"too low",
		"7",
		"too high",
		"6",
		"right on",
		"0",
	],
	["Stan is dishonest", "Stan may be honest"]
);
