var server,
port=2018,
http=require('http');

server=http.createServer(function(req,res){
    res.writeHead(200,{'Content-type':'text/plain'});
    res.end('Hello World');
    console.log('guest visited');
})

server.listen(port);
console.log('server is running');