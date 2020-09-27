
function EnviarJugada(color, X, Y)
{
    var csrftoken = '{{csrf_token}}';
    var data = JSON.stringify({ x: X, y: Y, Color: color })

    $.ajax(
    {
        headers: {"X-CSRFToken": csrftoken}, 
        url: "/ajax/Jugada/",
        type: "POST",
        dataType: "json",
        data: data
    });  
}

function RealizarJugada(event)
{       
    var coordenadas = getCursorPosition(canvas, event);
    EnviarJugada(color_to_paint, coordenadas[0], coordenadas[1]);
    pintar(coordenadas[0], coordenadas[1], canvas, color_to_paint);
}