const fs = require("fs");

function ReadData(){
    let data = fs.readFileSync("help.json", {encoding: "utf-8"});
};