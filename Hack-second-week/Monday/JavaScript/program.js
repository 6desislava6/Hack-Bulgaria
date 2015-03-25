// trigger them to do npm install
var u = require("underscore")

// Load the http module to create an http server.
var http = require('http');

// Configure our HTTP server to respond with Hello World to all requests.
var server = http.createServer(function (request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end(new Buffer("RG91Z2xhcyBDcm9ja2ZvcmQ=", "base64").toString('ascii'));
});

var port = 8000

// Listen on port 8000, IP defaults to 127.0.0.1
server.listen(port);

// Put a friendly message on the terminal
console.log("Okay, you got it now!");
console.log("Open up your browser and type:")
console.log("http://localhost:" + port)
console.log("This is your answer!")
console.log("When you see the answer, press Ctrl + C to kill me.")
