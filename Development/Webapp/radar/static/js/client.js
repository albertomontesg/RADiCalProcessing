$(document).ready(function(){
    var socket = io.connect('localhost', {port: 4000});
      
    socket.on('connect', function(){
        console.log("connect");
    });
    
    var speed = document.getElementById('speed')

    socket.on('message', function(message) {
        var data = message
        console.log(data)
        speed.innerHTML = data
    })
});