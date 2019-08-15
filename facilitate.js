

let key = async () => {
    const fs = require('fs');
    let contents = fs.readFileSync('./testcipher.txt','utf8');
    let engine = require("./engine");
    let theKey = await engine(contents);
    console.log("The key is: " + theKey);
};
   

key();