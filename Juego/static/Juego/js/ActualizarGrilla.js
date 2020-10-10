var Time = new Date();

function TraerJugadas(){
    
    var datos = JSON.stringify({ time: Time.toString() });
    $.ajax(
    {
        headers: {"X-CSRFToken": csrftoken}, 
        url: "/ajax/Jugadas/",
        dataType: "json",
        type: "POST",
        data: datos,
    }).done(cargarPixeles);
    Time = new Date(); 
}

window.setInterval(TraerJugadas, 5000);
