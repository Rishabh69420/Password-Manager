const electron = require("electron");
const app = electron.app;
const BrowserWindow = electron.BrowserWindow;
const path = require("path");
const url = require("url");

console.log(JSON.parse(data));

console.log("does this work");

let win;

function CreateWindow() {
    win = new BrowserWindow({
        width: 1280,
        height: 720
    });
    win.loadURL(url.format({
        pathname: path.join(__dirname, "index.html"),
        protocol: "file",
        slashes: true
    }));

    win.on("closed", () => {
        win = null;
    });
};

app.on("ready", CreateWindow);
