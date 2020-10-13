function hacerDenuncia(){
    // Pixeles denunciados
    var datos = JSON.stringify(remove_duplicates(pixelesdenuncia));
    // Descripcion de la denuncia
    var descripcion = document.getElementById('texto-denuncia').value;

    if (datos == "[]"){
        alert("No se seleccionó ningún pixel. Intentelo de nuevo.");
    }
    else if (descripcion == "") {
        alert("Agregue una descripción a su denuncia.");
    }
    else{
        alert("Tu denuncia fue enviada.");
        // Acá iría el POST
        salirModoDenuncia();
    }
}

function SeleccionarPixel(x,y, data){
    var context = canvas.getContext("2d");
    strokeLine(context, x, y);
    data.push({x, y});
}

function strokeLine(ctx, x, y) {
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.strokeStyle = 'rgba(255,180,200,255)';
    ctx.strokeRect(x*20-17, y*20-17, 17, 17);
    ctx.stroke();
}

function remove_duplicates(array) {
    var unicos = [];
    var itemsEncontrados = {};
    for(var i = 0, l = array.length; i < l; i++) {
        var stringified = JSON.stringify(array[i]);
        if(itemsEncontrados[stringified]) { continue; }
        unicos.push(array[i]);
        itemsEncontrados[stringified] = true;
    }
    return unicos;
}

function modoDenuncia()
{
    if (modo) { modo = false;
    document.getElementById("btn-denunciar").innerHTML = "Cancelar";
    document.getElementById("form-denuncia").style.display = "block";
}
    else { salirModoDenuncia(); }
}
function salirModoDenuncia(){
    modo = true;
    document.getElementById("btn-denunciar").innerHTML = "Denunciar";
    document.getElementById("form-denuncia").style.display = "none";
    pixelesdenuncia = [];
    $(on_pagina_cargada);
}