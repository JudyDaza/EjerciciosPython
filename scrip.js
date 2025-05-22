/* Plantilla JS: script.js */
function verMas(boton) {
  const descripcion = boton.previousElementSibling;
  if (!boton.disabled) {
    descripcion.textContent += " ¡Reserva ya tu cupo para esta experiencia inolvidable!";
    boton.disabled = true;
    boton.textContent = "Gracias por tu interés";
  }
}
