let intervalId = null;

function inicializarTimer(seconds){
    if (intervalId) {
            clearInterval(intervalId);
            intervalId = null;
    }
    var counter = seconds + 1;
    var max_counter = 0;
    intervalId = setInterval(() => {
      counter -= 1;
      document.getElementById('text-timer').innerHTML= 'Tiempo restante para la siguiente jugada: '+formatTime(counter);
    if (counter === max_counter) {
        document.getElementById('text-timer').innerHTML= '¡Puede pintar!';
        clearInterval(intervalId);
      }
    }, 1000);
}

function formatTime(time) {
  const minutes = Math.floor(time / 60);
  const hours = Math.floor(minutes / 60);
  let minutes_hours = minutes;
  let seconds = time % 60;

  if (seconds < 10) {
    seconds = `0${seconds}`;
  }

  if (hours == 0){ return `${minutes}:${seconds}`; }
  else {
    while (minutes_hours > 60)
        minutes_hours -= 60;

    if (minutes_hours == 60){ return `${hours}:00 HS.`; }
    if (minutes_hours < 10) { minutes_hours = `0${minutes_hours} HS.`; }
    return `${hours}:${minutes_hours} HS.`;
  }
}

function consultarTiempoJugada(data){
  if (data["Resultado"]) {
    tiempo_restante = data["Espera"];
    inicializarTimer(tiempo_restante);
  }
}


window.onload=$.ajax({url: "/ajax/Espera/", type: "GET"}).done(consultarTiempoJugada);
