export function parseCustomJSON(jsonString) {
    // Add double quotes around the keys
    //let validJSONString = jsonString.replace(/(\w+)\s*:/g, "\"$1\":");

    console.log(JSON.stringify(jsonString))
    // Now parse it with JSON.parse
    return JSON.parse(validJSONString);
}