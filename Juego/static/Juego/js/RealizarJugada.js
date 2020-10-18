

function EnviarJugada(color, X, Y, canvas) {
    var datos = JSON.stringify({ x: X, y: Y, Color: color });
    $.ajax( {
        headers: {"X-CSRFToken": csrftoken}, 
        url: "/ajax/Jugada/",
        dataType: "json",
        type: "POST",
        data: datos,
    }).done(ImprimirJugada);
}

function ImprimirJugada(data)
{
    if (data["Resultado"]) {
        var x = data["X"];
        var y = data["Y"];
        pintar(x, y, canvas, data["Color"]);
        // aquí iría el tiempo restante en segundos
        tiempo_restante = 60;
        inicializarTimer(tiempo_restante);
    }                    
}