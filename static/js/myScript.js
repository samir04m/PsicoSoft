function showSpinner() {
    elemento = document.getElementById("buttonText");
    elemento.classList.add("d-none");
    elemento = document.getElementById("buttonSpinner");
    elemento.classList.remove("d-none");
}

function btnUpdatePaciente() {
    nombres = document.getElementById("nombres").value;
    apellidos = document.getElementById("apellidos").value;
    tipoDocumento = document.getElementById("tipoDocumento").value;
    numeroDocumento = document.getElementById("numeroDocumento").value;
    fechaNacimiento = document.getElementById("fechaNacimiento").value;
    celular = document.getElementById("celular").value;
    motivoConsulta = document.getElementById("motivoConsulta").value;
    diagnostico = document.getElementById("diagnostico").value;
    nuevoDiagnostico = document.getElementById("nuevoDiagnostico").value;
    analisis = document.getElementById("analisis").value;
    planTrabajo = document.getElementById("planTrabajo").value;

    mensaje = "";
    if (nombres == "") mensaje += " - Nombres.\n";
    if (apellidos == "") mensaje += " - Apellidos.\n";
    if (tipoDocumento == "") mensaje += " - Tipo de documento.\n";
    if (numeroDocumento == "") mensaje += " - Número de documento.\n";
    if (fechaNacimiento == "") mensaje += " - Fecha de nacimiento.\n";
    if (celular == "") mensaje += " - Celular.\n";
    if (motivoConsulta == "") mensaje += " - Motivo de consulta.\n";
    if (diagnostico == "" && nuevoDiagnostico == "") mensaje += " - Diagnóstico.\n";
    if (analisis == "") mensaje += " - Análisis.\n";
    if (planTrabajo == "") mensaje += " - Plan de trabajo.\n";

    if (mensaje != "") {
        mensaje = "Debe diligenciar los siguentes campos:\n" + mensaje;
        alert(mensaje);
    } else {
        form = document.getElementById("formUpdatePaciente");
        form.submit();
    }
}