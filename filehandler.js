function ReadData(){
    const fs = require("fs");
    var crude = fs.readFileSync("help.json", {encoding: "utf-8"});
    var data = JSON.parse(crude);
    var data1 = "";
    for (var i in data){
        data1 += `Email: ${data[i].email}<br>`;
        data1 += `Username: ${data[i].username}<br>`;
        data1 += `Password: ${data[i].password}<br><br>`;
    };
    document.getElementById("lol").innerHTML = data1;
};
