var fs = require('fs'),
    Lazy = require('lazy');
var mongo_uri = process.env.MONGO_URI;
var filename = process.argv[1];

if (!filename) {
  console.error('filename is not available');
  process.exit(1);
}

var regex = /[^,]*,[^,]*,(\w+),(\w+),(\w+),[^,]*,(\w+),([^,]*),[^,]*,[^,]*,[^,]*,([^,]*),([^,]*)/;
var readStream = fs.createReadStream(filename);
Lazy(readStream).lines.forEach(function(l) {
  l
});


