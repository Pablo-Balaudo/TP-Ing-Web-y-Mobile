var Time = new Date();

function TraerJugadas(){
    
    $.ajax(
    {
        url: "/ajax/Jugadas/",
        type: "GET",
        data: { "time": Time.toString() },
    }).done(cargarPixeles);
    Time = new Date(); 
}

window.setInterval(TraerJugadas, 5000);
