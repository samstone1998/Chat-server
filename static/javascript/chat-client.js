$(document).ready(function(){


    var socket = io.connect(window.location.hostname + ':' + window.location.port);

    socket.on('connect', function(){
        socket.send("User connected");
    });

    socket.on('message',function(message){
        $('#messages-container').append(`<p class="message m-0">${message}</p>`)
    });

    $('#user-message-submit').on('click',function(){
        socket.send($('#user-message').val());
        $('#user-message').val('');
    });

});