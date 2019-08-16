
async function key(textElement, outputElement){
    console.log("HELLO");
    let engine = require("./engine");
    let theKey = await engine(textElement.value);
    console.log("The key is: " + theKey);
    outputElement.innerHtml = theKey;

};