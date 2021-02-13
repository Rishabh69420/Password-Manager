const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require("path");
const url = require("url");
const fs = require("fs");

let data = fs.readFileSync("help.json", {encoding: "utf-8"});

// fs.writeFile("help1.json", `${data.slice(0, data.length - 1)}, "brhouh": "nijeaivn"}`, function(err){
//     if (err) {
//         console.log(err)
//     } else {
//         console.log("it worked somehow")
//     };
// });

console.log(JSON.parse(data));

console.log("does this work");

let win;

function CreateWindow() {
    win = new BrowserWindow();
    win.loadURL(url.format({
        pathname: path.join(__dirname, "index.html"),
        protocol: "file",
        slashes: true
    }));

    win.on("closed", () => {
        win = null;
    })
}

app.on("ready", CreateWindow);
