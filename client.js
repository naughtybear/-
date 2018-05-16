var net = require('net');

var client = new net.Socket();
client.connect(9999, '127.0.0.1', function() {
    console.log('Connected');
    client.write('蘇辰搖廢物');
});

client.on('data', function(data) {
    console.log('Received: ' + data);
    client.destroy(); // kill client after server's response
});