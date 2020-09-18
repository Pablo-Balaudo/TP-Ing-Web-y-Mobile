

function getCursorPosition(canvas, event, color)
{
    var rect = canvas.getBoundingClientRect();

    var x = Math.ceil(((event.clientX - rect.left) -1) / 20);
    var y = Math.ceil(((event.clientY - rect.top) -1) / 20);

    document.getElementById("x").innerHTML = "Coord X " + x;
    document.getElementById("y").innerHTML = "Coord Y " + y;

    if (((x >= 1) && (x <= 50)) && ((y >= 1) && (y <= 50)))
    { pintar(x, y, canvas, color); }
    else
    {  alert("Has clickeado muy cerca del borde"); }
}