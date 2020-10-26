var canvas = document.querySelector('Canvas');

function pintar(x, y, canvas, color_RGBA)
{
    var c = canvas
    var context = c.getContext("2d");
    var imageData = context.createImageData(20, 20);       

    // Iterate through every pixel
    for (let i = 0; i < imageData.data.length; i += 4)
    {
        // Modify pixel data
        imageData.data[i + 0] = color_RGBA[0];  // R value
        imageData.data[i + 1] = color_RGBA[1];  // G value
        imageData.data[i + 2] = color_RGBA[2];  // B value
        imageData.data[i + 3] = color_RGBA[3];  // A value
        
    }
    // Draw image data to the canvas

    context.putImageData(imageData, x*20-20, y*20-20);
}

function cargarPixeles(data) {
    
    for (let index = 0; index < data.length; index++) {             
        var x = data[index]["X"];
        var y = data[index]["Y"];
        var color_RGBA = data[index]["color"];  
        pintar(x, y, canvas, color_RGBA);
    }
}

function drawBoard(data) {
    var c = document.getElementById("Canvas");
    var context = c.getContext("2d");
    var imageData = context.createImageData(1000, 1000);
    cargarPixeles(data);  
}

