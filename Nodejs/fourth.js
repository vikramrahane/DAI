var http=require('http')

http.createServer(function(req, res){
    res.write("welcom to Hell..");
    res.end()

}).listen(9005)