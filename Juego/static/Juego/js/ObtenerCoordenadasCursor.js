

function getCursorPosition(canvas, event)
{
    var rect = canvas.getBoundingClientRect();

    var X = Math.ceil(((event.clientX - rect.left) -1) / 20);
    var Y = Math.ceil(((event.clientY - rect.top) -1) / 20);

    document.getElementById("x").innerHTML = "Coord X " + X;
    document.getElementById("y").innerHTML = "Coord Y " + Y;

    if (((X >= 1) && (X <= 50)) && ((Y >= 1) && (Y <= 50)))
    { return [X,Y]; }
    else
    {  alert("Has clickeado muy cerca del borde"); }

}